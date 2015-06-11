# -*- coding: utf-8 -*-
import utils
import archiving
import os


'''
The main function for pushing files.
Starts out checking the lock, then behaviour changes depending on that. If it is locked, user will have no access whatsoever via the script. Only the user who locked is able to push and unlock.

'''
def push(args, currPath):
	if (os.path.exists(os.path.join(currPath, args.projectName))):
		ret, user = utils.lockCheck(os.path.join(currPath, args.projectName), args.user)
		if (ret and user != args.user):
			print ("It is, at the moment, impossible to commit the files. This project is currently locked by user : " + user)
			return (False)
		elif (user == args.user and not args.lock):
			utils.setLock(user, False)
	commitObjs = initFolders(args.projectName, args, currPath)
	versNb, versNames = utils.countVersions(os.path.join(currPath, args.projectName))
	if (versNb > 5):
		print (os.path.join(currPath, args.projectName) + " : more than 5 versions. Must be archived.")
		#print (versNames)
		archiving.archiving(args, args.projectName, versNames, commitObjs)
	print("Pushing files!")

'''
Called at each push/commit. Just updates the commit/versions + currentVersion info.
'''
def updateHeader(header, args):
	if not (args.version):
		header.defaultVersions += 1
		header.currentVers = "VERSION_" + str(header.defaultVersions)
	else:
		header.currentVers = args.version
	header.versions += 1
	header.commits += 1	
	return (header)

'''
Adds the commitObj to the list of all and also check that the size is not superior to 
MAX_COMMITLOG_SIZE. If it is, removes the oldest entry 
(first entry if reading the file from beginning to end).
Adds the new entry whatever happens.
'''

def addCommitObj(commitObjs, args, currentVers, projectName):
	commitObjs.append(utils.createCommitObj(projectName, args, currentVers))
	return (commitObjs)

'''
Prepares all files for copying and then copies.
'''

def updateVersFile(path, args, projectName):
	header, commitObjs = utils.getHeaderAndCommit(path + 'versFile')
	updateHeader(header, args)
	# Adds the current commit information
	commitObjs = addCommitObj(commitObjs, args, header.currentVers, projectName)
	version = header.currentVers
	versFile = open(path+'versFile', 'w')
	versFile.write(header.serialize())
	for commit in commitObjs:
		versFile.write(commit.serialize())
	versFile.close()
	return (commitObjs, version)

def initFolders(projectName, args, currPath):
	path = currPath + projectName + "/"
	# This if is for the case where the project has not be initialised. (No folder in root with : [projectName])
	if not os.path.exists(path):
		# Create directory with projectName inside of the "root" directory
		os.makedirs(path)
		version = utils.setUpFiles(projectName, args, currPath)
		os.makedirs(path + version)
		commitObjs = []
		lockFile = open(path + ".lockFile", 'w+')
		lockFile.write("unlocked:None")
		lockFile.close()
	else:
		# Parse information from versFile. (Header + all commits stored)
		commitObjs, version = updateVersFile(path, args, projectName)

		if not (os.path.exists(path + version)):
			os.makedirs(path+version)
		
	# Copies all files (And directories) specified by the user in the command line
	utils.copyAll(path+version, args.files)
	return (commitObjs)