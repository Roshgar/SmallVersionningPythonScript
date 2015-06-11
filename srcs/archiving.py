# -*- coding: utf-8 -*-
import utils
import shutil
import os
import sys

'''
Checks the archives to know if the version already exists in the project. If so the user has 3 choices : Overwriting, renaming and ignoring.
'''
def checkArchives(projectName, versName, projectPath, archPath):
	path = archPath + "/" + projectName + "/"
	nbVers, versNames = utils.countVersions(utils.archivePath + "/" + projectName)
	if versName in versNames:
		choice = input("A directory with the name " + versName + " already exists in the archives for project : " + projectName + ".\nEither a manual copy was made, or a version name was specified (with --version) with a name like the default : VERSION_X\nChoose what to do : 1 - Overwrite or 2 - Rename or 3 - Ignore. [1\2\3] : ")
		if choice == 1:
			shutil.rmtree(path + versName)
			shutil.move(projectPath + versName, path)

			# overwrite
		elif choice == 1:
			#rename directory
			newName = input("Please enter the new name for the version to be archived : ")
			shutil.copytree(projectPath + versName, path + newName)
			shutil.rmtree(projectPath + versName)
		elif choice == 1:
			print ("Ignored for this time. The question will be asked each time.\nYou can modify the number of accepted versions by editing the file [fileRelocation.py] with the variable MAX_VERS_NUMBERS.")
			return (0)
		else:
			print ("Ignored for this time. The question will be asked each time.\nYou can modify the number of accepted versions by editing the file [fileRelocation.py] with the variable MAX_VERS_NUMBERS.")
			return (0)

	else:
		shutil.move(projectPath + versName, path + versName)
			# Ignore. Not sure I'm keeping this option.

		# Diplay prompt for user and make him choose his method.

'''
Archiving function, it checks if the number of directories (versions) in the project is superior to 5. 
If so, it will figure out which one is the oldest 
(Last time committed. So if Version_1 Was just overwritten by previous commit, and we are at version_6, version_2 will go to archives.)
And copy that one to the archives.
If somehow the user recreated a version name that already exists in the archives, 
it will ask him to cancel, overwrite anyways, or choose a new name for the version to be copied.
Then execute the corresponding choice.
'''
def archiving(args, projectName, versNames, commitObjs, currPath):
	removed = 0
	tmpVers = versNames
	if args.archive:
		archivePath = args.archive + "/"
	else:
		archivePath = utils.archivePath
	for commit in reversed(commitObjs):
		tmp = commit.getVers()
		if (tmp in tmpVers and removed < 5):
			tmpVers.remove(tmp)
			removed += 1
	print ("The intruder(s) is : " + str(tmpVers))
	projectPath = currPath + projectName + "/" # will be changed. Need a more generic way for this. (Accepting a user defined directory as root folder.)
	if (len(tmpVers) >= 1):
		if not (os.path.exists(archivePath + projectName)):
			os.makedirs(archivePath + projectName)
		for moveVers in tmpVers:
			checkArchives(projectName, moveVers, projectPath, archivePath)
		print("Archiiiiiive")