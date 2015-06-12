# SmallVersionningPythonScript
## Table of contents
  1 - [Description](#description)
  
  2 - [Requirements](#requirements)
  
  3 - [Usage](#usage)
  
  4 - [Contact](#contact)
  
## Description
A small utility script that allows basic project versionning functionnalities (I.e : Copy to and from source/dest folders, "versionning" of revisions, "archiving"... Etc.

## Requirements
#### Python 2.7
This program uses python 2.7 64 bit for windows. To download and install, either click [here](https://www.python.org/downloads/release/python-279/ ), navigate down the page and click on `Windows x86-64 MSI Installer`, **or** click on [this link](https://www.python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi). Once it is downloaded, launch it and wait for the installation to complete.
##### To avoid some issues :
It should by default install to `C:\Python27`. You will also be able to specify this during the install process. If you chose a different path, remember where this install went, note it down. From now on i will refer to where python was installed as PYTHONPATH

After being able to choose a directory to install python, you will see a display with `Customize Python` written at the top. Scroll down the menu until you see `Add python.exe to Path`. Click on the menu to its left, select `will be installed on local hard drive`. This will remove a few complications that could arise afterwards.

#### WxPython (Graphical library)
The next step is to take care of the graphical library. Click [here](http://downloads.sourceforge.net/wxpython/wxPython3.0-win64-3.0.2.0-py27.exe), download, follow the instructions.

If an issue arises at this step (I.e : No installation of python2.7 found in the registry), you did not  just do `ok > I Accept > Next`
You will then be shown a window with an input. Said input should look like `C:\put a directory on the PYHTONPATH here\Lib\site-packages`. Simply change it to your PYTHONPATH from earlier. On a default python installation, you should thus have `C:\Python27\Lib\site-packages`.

#### Setting up the modules
Once that is done, you normally have finished the most manual part of the work. Downhill from here.
Download the .zip of this project, extract it wherever you want, and navigate to it with your console (cmd and powershell will be on all Windows systems.)
Once there, go into InstallUtils, and simply type `python install.py`. You may now go take a 5 minute break. Once you come back, everything should be installed. Then, all that is left to do is type `python launch.py` and follow the usage.

You can also manually install this with the information below. (But why?)

It makes use of the following python modules :
  - WXPython 
      - http://sourceforge.net/projects/wxpython/files/wxPython/3.0.2.0/wxPython3.0-win64-3.0.2.0-py27.exe/download?use_mirror=iweb
  - Gooey (Beta)
      - git clone https://github.com/chriskiehl/Gooey.git then run a `python setup.py install` from inside gooey's directory
      
      OR
      - `pip install gooey`

  - Shutil (Should be included with a default version of python)
  - argparse
      - `pip install argparse`

####Side Note
If there is an issue when you launch it (I.e It spits out a traceback about multiDirChooser not being present), wait one or two days. A merge is pending on one of the libraries I use, i can add another script for the install but by 06/12/15 evening it should be merged.

##Usage
Open a terminal (cmd, powershell, cmder... Whatever you have on your system and/or prefer), navigate to wherever you placed the files of this, and simply type `python launch.py`.

Another solution is available that takes away the hassle of the command line if you are on a windows system. Simply right-click on any file with the `.py` extension then, `Open With` > `Choose default program` > `Python`

Once that is done, you can double click the `launch.py` file, and it will start the script. This thus allows you to make a shortcut out of it, and place it on the desktop. (Or wherever the H*** you want)

A window looking quite like this one should show. If not, there was an issue with one of the previous steps. Write down the error and add it in the issue section of this project, or else send me an [e-mail](#contact)
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
