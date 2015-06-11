# -*- coding: utf-8 -*-
import sys
import os
import time
import parse
import argparse
import shutil
import re

defaultFolderPath = "./projectFolder/"
archivePath = "./Archives/"

# Class used to take care of the versionning information
class versionHeader:
	# All commits excluding overwrites.
	versions = 1
	# Commits which used default folder name (VERSION_X) with X being the value of defaultVersions
	defaultVersions = 1
	# Number of commits
	commits = 1
	# Number of times a user asked for the files of this project
	pulls = 0
	# Current version name
	currentVers = "VERSION_1"
	# This function takes as first parameter, a list with the first three lines of the .versFile : The Header.
	# It will return a versionHeader object with all the file information included in the header.
	def initFromFile(self, tab):
		versLine = tab[0] 
		changeLine = tab[1]
		currentVers = tab[2]
		# Split on semicolons to get all information
		tab = versLine.split(':')
		# Fairly explicit
		self.versions = int(tab[1])
		self.defaultVersions = int(tab[3])
		tab2 = changeLine.split(':')
		self.commits = int(tab2[1])
		self.pulls = int(tab2[3])
		# Just removes the last character of the string which would otherwise be a carriage return.
		self.currentVers = currentVers[:-1]
	# Pretty much doest what it ways. Serializes the object into a string.
	def serialize(self):
		return ("Versions:"+str(self.versions)+":DefaultVersions:"+str(self.defaultVersions)+
			"\nCommits:"+str(self.commits)+":pulls:"+str(self.pulls)+"\n"+self.currentVers+"\n")

#Class used to represent one commit.
class commitObj:
	def __init__(self, tab):
		self.info = tab.pop(0)
		self.message = ""
		for line in tab:
			self.message += line
	def getVers(self):
		tmp = self.info.split(':')
		return (tmp[1])
	def __str__(self):
		return ("commitObj with info : " + self.info + " and message : " + self.message)
	def serialize(self):
		return ("<commit>\n\t" + self.info + "\n\t" + self.message + "\n</commit>\n")

'''
Parses the header information from the file .versFile, 
located in the project specified by the user
'''

def getCommitObjs(tab):
	commitObjs = [];
	tmpTab = []
	for i in tab:
		if (i == "</commit>\n"):
			commitObjs.append(commitObj(tmpTab))
			tmpTab = []
		elif (i != "<commit>\n"):
			tmpTab.append(i.strip())
	return (commitObjs)

# Does what it says using shutil functionnalities. 
# os.path.basename just gets the last folder. (i.e `os.path.basename("hello/foo/bar")` would return "bar")
def copyAll(dest, srcs):
	for toCopy in srcs:
		if (os.path.isfile(toCopy)):
			shutil.copy2(toCopy, dest)
		else:
			shutil.copytree(toCopy, dest + "/" + os.path.basename(toCopy))

#Retrieves the header information, updates it, and commits it.
def getHeaderAndCommit(path):
	if (os.path.isfile(path)):
			myFile = open(path)
	else:
		print("From getHeaderAndCommit : [" + path + "] does not exists or is not a file.")
		return (None, None)
	header = versionHeader()
	lines = myFile.readlines()
	headerLines = []
	for i in range(0, 3):
		headerLines.append(lines.pop(0))
	header.initFromFile(headerLines)
	commitObjs = getCommitObjs(lines)
	myFile.close()
	return (header, commitObjs)



'''
Self explanatory. But it checks if the user is asking for an overwrite or specified 
a version. This allows to get the actual name of the version being pushed.
'''

def getVersionName(args, header):
	if (args.overwrite):
		return (header.currentVers)
	elif (args.version):
		return (args.version)
	else:
		return ("VERSION_" + str(header.defaultVersions + 1))

def createCommitObj(projectName, args, versionName):
	tab = []
	date = time.asctime( time.localtime(time.time()) )
	tab.append(args.user + ':' + versionName + ':' + date)
	tab.append(str(args.message))
	return (commitObj(tab))

'''
Creates the string for a given commit. in form :
<commit>
	USER:VERSIONNAME:DATE
	COMMIT_MESSAGE
</commit>
'''
def countVersions(path):
	cnt = 0
	versionNames = []
	for f in os.listdir(path):
		if (os.path.isdir(os.path.join(path, f))):
			versionNames.append(f)
			cnt += 1
	return (cnt, versionNames)

def commitLog(projectName, args, versionName):
	date = time.asctime( time.localtime(time.time()) )
	return ("<commit>\n\t" + args.user + ":" + versionName + ":" + date + "\n\t" + 
			str(args.message) + "\n</commit>\n")

'''
Sets up the .versFile on first commit of a project.
	Creates a header and then writes everything to the file.
'''

def setUpFiles(projectName, args, currPath):
	# Object representing the "Header" of the .versFile
	header = versionHeader()
	# If a version was specified
	if (args.version):
		# set that version as currentVersion and, since this is a first time for a project,
		# defaultVersions is set to 0
		header.currentVers = args.version
		header.defaultVersions = 0
	# Just sets the correct 
	version = header.currentVers
	# Opening the versFile to update it with the newly created header.
	versFile = open(currPath + projectName + "/" + "versFile", 'w')
	# Write the header object in a string format ( returned by header.serialize() ) to the .versFile
	versFile.write(header.serialize())
	# Write the commit information to the .versFile Seeing as it is a new version, just a call to commitLog is sufficient.
	versFile.write(commitLog(projectName, args, version))
	# Not explaining this. :)
	versFile.close()
	return (version)

def setLock(path, user, lock):
	print(path)
	lockFile = open(path + '/.lockFile', 'w+')
	print(lockFile)
	if (lock):
		print("Wrote to file.")
		ret = lockFile.write("locked:" + user)
		#lockFile.write("IM A HIPPO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		print(ret)
	else:
		lockFile.write("unlocked:" + user)
		lockFile.write("NOOOOO")
	lockFile.close()


'''
Simple function, opens .lockFile from the requested project, verifies if a user previously checked out the file(s) and returns :
	- True, userName IF it is 'locked'.
	- False, "" IF EITHER the project isn't 'locked' or if it's the user who 'locked' that is requesting the files.
'''

def lockCheck(path, user):
	if not (os.path.exists(path + '/.lockFile')):
		if (os.path.exists(path)):
			tmpFile = open(path + '/.lockFile', 'w+')
			tmpFile.write("unlocked:" + user)
			tmpFile.close()
			print ("The lockFile was previously deleted. Restored.")
		else:
			print ("!! An error occured. Currently in lockCheck (utils.py Line 185) with no path to specified project. Something went terribly wrong previously. If this message is showing up there is a real problem. !!")
		return (False, user)
	lockFile = open(path + '/.lockFile', 'r+')
	line = lockFile.readline()
	line.strip()
	lockFile.close()
	info = line.split(':')
	locked, lockUser = info[0], info[1]
	if (locked == "locked"):
		if (user == lockUser):
			#print ("In user == lockUser with user : " + user + " and lockUser : " + lockUser)
			return False, lockUser
		else:
			return True, lockUser
	return False, ""
