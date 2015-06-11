# -*- coding: utf-8 -*-
'''
Please, do not be ridiculous, do not name a version with -v to be VERSION_X    with X being a number. 
Just... Don't. You're creating conflicts for no reason. It will update itself to the versions. 
Actually, if you don't know what you are doing, ignore all options. 

Commit your files with : [python fileRelocation.py -fs RANDOM USER_NAME PROJECTNAME] and just select your files/directories.

Pull them with : [python fileRelocation.py -g RANDOM USER_NAME PROJECTNAME]


RANDOM : just character(s). Useless. Will be ignored in both scenarios. But need a file parameter so hey.
USER_NAME : The name you will use (try always) for commits/pulls. It allows locking and notification to other users.
PROJECTNAME : The name of the directory that will be used for the project.
'''

import parse
import get
import push
import utils
import datetime
import os

MAX_VERS_NUMBERS = 5

def main(args):
	if (args.path):
		currPath = args.path + "/"
	else:
		currPath = utils.defaultFolderPath
	args.method(args, currPath)