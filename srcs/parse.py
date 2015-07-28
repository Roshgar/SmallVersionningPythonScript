import argparse
from gooey import Gooey
from gooey import GooeyParser

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
'''

def get():
	print("get")

def push():
	print("Push")

@Gooey
def initOptParser():
	defaultFolderPath = "./THISISSMALLTEST"
	archivePath = "./Archives"

	#parser= argparse.ArgumentParser(description='Copy files to specified location. ')
	parser = argparse.ArgumentParser(description="Copy files to specified location")
	# Option for the path of files to move (can be a full directory).

	parser.add_argument('files', metavar='file', type=str, nargs='+',
                  		 help='file(s) or directory that you wish to copy' )
	#''', widget="MultiFileChooser"'''
	# Option to specify which project said files go to.

	parser.add_argument('-p', '--path', metavar='path',dest='path',  type=str, 
						help='Path which will be considered as root of all projects. Default is currently : ' + defaultFolderPath, 
						default=defaultFolderPath)
	#''', widget="FileChooser"'''

	parser.add_argument('projectName', metavar='projectName', type=str, 
						help='The project you wish to retrieve/add files to/from.')
	# Option to specify the version name of the commit.

	parser.add_argument('-v', '--version', metavar='versionName', type=str,
						help='The name of the directory which will be created during an update. By default, this will be : DATE_TIME.')
	# Option allowing overwrite of current version.

	parser.add_argument('-o', '--overwrite',
						help='Overwrites the files in the current version of specified project. (no new directory creation)', action="store_true")
	# Commit message. Stores it in a default file if no specific one specified.

	parser.add_argument('-m', '--message', metavar='logMessage', type=str, help='Use to specify a log message which will be put in a .txt file. (default : commit.txt)')
	# Specify --get to retrieve files instead of commiting them.

	parser.add_argument('-g', '--get', dest='method', action='store_const', help='Retrieve files from project (last version by default)', const=get, default=push)
	# Allows 'locking'. Not really a lock. Basically a warning message to all users who try to check out if a user checked out without commiting his files.
	
	parser.add_argument('-l', '--lock', action="store_true",
						help='Locks the current project. Can be overriden/ignored on demand. (Will ask other users if they want to pull files)'+ 
							'Unlocked when next push from the locking user is made')
	# User name. Just to allow 'locking'/'unlocking'
	
	parser.add_argument('user', metavar='userName', type=str, help='Specify your name.')


	parser.add_argument('-a', '--archive', metavar='archivePath', type=str, help='Use to specify a directory which will be used as an archive. Current default is : ' + archivePath)
	# Will pop up a windows fileselector to choose which files will be copied.
	#parser.add_argument('-fs', '--fileSelector', 
	#					help="Will ignore files given by commandLine (One still necessary. Enter a factice NULL for example) and popup a window for selecting.", 
	#					action="store_true")
	parser.add_argument('-s', '--store', metavar="destPath", help='Use to specify where you want the files retrieved from the project to be copied.')
	# Function to call to get all arguments.
	args = parser.parse_args()
	#print(args.files)
	#print(args.user)
	#print(args.projectName)
	#printOptions(args)
	#args.method()
	print("The following files/directories will be copied (along with all sub-directories) :")
	for myFile in files:
		print("- [" + myFile + "]")
	return (args)
