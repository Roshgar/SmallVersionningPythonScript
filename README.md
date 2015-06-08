# SmallVersionningPythonScript
## Table of contents
  1 - [Description](description)
  
  2 - [Requirements](requirements)
  
  3 - [Usage](usage)
  
  4 - [Contact](contact)
  
## Description
A small utility script that allows basic project versionning functionnalities (I.e : Copy to and from source/dest folders, "versionning" of revisions, "archiving"... Etc.

## Requirements
This program uses python 2.7 64 bit for windows. 
These installs should not be necessary. Python 2.7 should be installed and that will suffice to run the program.
It also makes use of a few python modules :
  - WXPython 
      - http://sourceforge.net/projects/wxpython/files/wxPython/3.0.2.0/wxPython3.0-win64-3.0.2.0-py27.exe/download?use_mirror=iweb
  - Gooey (Beta)
      - git clone https://github.com/chriskiehl/Gooey.git then run a `python setup.py install` from inside gooey's directory
      
      OR
      - `pip install gooey`

  - Shutil (Should be included with a default version of python)
  - argparse
      - `pip install argparse`


##Usage
Double click the executable. You're good to go!
![Image of The Gooey GUI](images/VersionningGui.jpg)


First of all, there are a few definitions to be made. Project refers to the directory that will be used for one specific project. Then come versions. These refer to the directories that are in your project folder, and that store each of your commits for each "version".

The first two arguments are mandatory. 
#####ProjectName
ProjectName should be the name you want your projects main folder to have. Inside of said folder will be your different versions of the project.
#####User
User should be the name you will (always) use with this script. This is what will be used to know who you are and who, if anyone, is modifying the project at the moment.
#####Files/Directories
Then we have the optionnal arguments. The first two are Files and Directories. As their names indicate, they are the inputs you will use to select the files and/or directories to copy. You can use either or both. If both fields are empty, the program will not do anything and exit.
#####Path
Then we have Path, It will be used to choose a specific location to copy to instead of using the default directory destination. (Which is represented in the code by the variable `defaultFolderPath`, defined in `srcs/utils.py l.8`)
#####Version
Version is simply there to allow specification of the Version name, by that meaning the name of the folder that will reside in your projects folder
#####Message
The message option is simply to allow specifications on what has been done. (I.e : "Made a small graphical change", "Implemented a new functionnality", "Fixed a glitch"... And so on. These messages are logged into a file named versFile at the root of your project Folder with the associated user, date, and version.
#####Method
The method option is simply to allow copying to and from. Leave it unchecked if you wish to push the files to your project directory, check it if you wish to retrieve the files that constitute your latest version.
#####Store
Store is used to select a folder to be used as a destination when retrieving the files from your project.
#####Archive
Archive is to specify a folder that will be used as an "Archive". The default is the variable `archivePath`, defined in `srcs/utils.py l.9`
#####Lock
This option is used to "Lock" the project. This will prevent other users from modifying the source of the project you have previously checked out. Once you push the files back in, (if you did not specify this option again) the project becomes unlocked and everybody has access again. (You may still retrieve the files if the project was locked by another user. However, all pushing of the files will be forbidden. So just wait until the person pushes everything, and then only retrieve what you want.)

##Contact
If any issues/bugs/questions/other arise, please feel free to either create an issue on this page, or contact me at `calapitook@gmail.com`
