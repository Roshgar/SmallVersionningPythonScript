#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
#For reference and documentation, code will be commented appropriately.

import sys
#Allows fetching of my other files as modules.
sys.path.insert(0, './srcs/')
from gooey import Gooey
from gooey import GooeyParser
#Main file
import fileRelocation
#Utilitaries that (generally) aren't specific and have more than one use.
import utils
#File for the "get" part of the script
import get
#FIle for the "Push" part of the script
import push
#File used to take care of archiving.
import archiving

#Argparse module. Cf lower down
import argparse
#Module used to generate the GUI.


def printOptions(args):
		if args.version:
			print("versionName : " + args.version)
		if (args.overwrite):
			print("overwrite activated.")
		if (args.message):
			print("We have a message : " + args.message)
		if (args.path):
			print("Specified path is : " + args.path)

'''
	Basic option Parser below. 
	Cf. argparse module from python library. Decently explicit stuff. Should take about 5 minutes (tops) to get quite a good grasp of this.
			https://docs.python.org/2/library/argparse.html#nargs
	Quick recap : 
		- add_argument(name, metavar=name_in_help, type=type_of_variable, nargs=number_of_variables, help=help_message) Does exactly what it says. How surprising huh? :) 
		- parse_args() Just picks them up from the command line and set everything up.
	Gooey is what pops up the GUI. Simply adds itself over argparse module.
'''

@Gooey
def initOptParser():
	parser = GooeyParser(description="Copy files to specified location")

	# Option for the path of files to move (can be a full directory).

	parser.add_argument('--files', metavar='file', nargs='*', 
                 		 help='file(s) you wish to copy', widget="MultiFileChooser")

	parser.add_argument('--directories', metavar='dir', nargs='*', help="The directorie(s) you wish to copy.", widget="MultiDirChooser")
	# Option to specify which project said files go to.
	

	parser.add_argument('-p', '--path', metavar='path',dest='path',  type=str, 
						help='Path which will be considered as root of all projects. Default is currently : ' + utils.defaultFolderPath, 
						default=utils.defaultFolderPath, widget="DirChooser")

	parser.add_argument('projectName', metavar='projectName', type=str, 
						help='The project you wish to retrieve/add files to/from.')
	# Option to specify the version name of the commit.

	parser.add_argument('-v', '--version', metavar='versionName', type=str,
						help='The name of the directory which will be created during an update. By default, this will be : VERSION_X.')
	# Option allowing overwrite of current version.



	parser.add_argument('-m', '--message', metavar='logMessage', type=str, help='Use to specify a log message which will be put in a versFile at the root of the project directory.')
	# Specify --get to retrieve files instead of commiting them.

	parser.add_argument('-g', '--get', dest='method', action='store_const', help='Retrieve files from project (last version by default)', const=get.get, default=push.push)
	# Allows 'locking'. Not really a lock. Basically a warning message to all users who try to check out if a user checked out without commiting his files.
	
	parser.add_argument('-l', '--lock', action="store_true",
						help='Locks the current project. '+ 
							'Unlocked when next push from the locking user is made')
	# User name. Just to allow 'locking'/'unlocking'
	
	parser.add_argument('user', metavar='userName', type=str, help='Specify your name.')


	parser.add_argument('-a', '--archive', metavar='archivePath', type=str, help='Use to specify a directory which will be used as an archive. Current default is : ' + utils.archivePath, widget="DirChooser")
	# Will pop up a windows fileselector to choose which files will be copied.
	parser.add_argument('-s', '--store', metavar="destPath", help='Use to specify where you want the files retrieved from the project to be copied.', widget="DirChooser")
	# Function to call to get all arguments.
	
	args = parser.parse_args()
	#print(args.files)
	#print(args.directories)
	if (args.files == None and args.directories == None):
		return (None)
	if (args.files and args.directories):
		args.files = args.files + args.directories#args.files[0].split(";")  + args.directories[0].split(";")
	elif (args.directories):
		args.files = args.directories
	print("The following files/directories will be copied (along with all sub-directories) :")
	for myFile in args.files:
		print("- [" + myFile + "]")
	return (args)

def start():
	args = initOptParser()
	#print(args.files)
	if (args.files == None):
		print("Not copying anything does not seem to warrant the use of this script. Ignoring and closing.")
		return (0)
	fileRelocation.main(args)

start()