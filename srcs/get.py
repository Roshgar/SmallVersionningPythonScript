# -*- coding: utf-8 -*-
import utils
import os
import shutil

def get(args, currPath):
	destPath = "./"
	header, commitObjs = utils.getHeaderAndCommit(currPath + args.projectName + "/versFile")
	ret, user = utils.lockCheck(os.path.join(currPath, args.projectName), args.user)
	path = currPath + args.projectName + "/" + header.currentVers
	if (args.store):
		destPath = args.store
	if (ret):
		print("This project was locked by the user " + user + ". It is advised to not touch the files related with this project as said person is probably planning on modifying and putting them back after. You can still manually retrieve the files.")
		return (False)
	dirName = header.currentVers
	tmpName = dirName
	cnt = 1
	while (os.path.exists(os.path.join(destPath, tmpName))):
		tmpName = dirName + "-" + str(cnt)
		cnt += 1
	if (ret == False):
		shutil.copytree(path, os.path.join(destPath, tmpName))
		if (args.lock):
			print("went to utils.setlock")
			utils.setLock(os.path.join(currPath, args.projectName), user, True)
	print("Last three prints :")
	print (args.store)
	print (ret)
	print (user)	