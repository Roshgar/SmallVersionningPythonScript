import os
import pip
import shutil

pythonPath = r"C:\Python27\"
gooeyPath = r"Lib\site-packages\gooey\"

def addMyGooeyFiles():
	shutil.copy2("./widget_pack.py", pythonPath + gooeyPath + r"gui\widgets\")
	shutil.copy2("./components.py", pythonPath + gooeyPath + r"gui\widgets\")
	shutil.copy2("./argparse_to_json.py", pythonPath + gooeyPath + r"python_bindings\")


def install(package):
    pip.main(['install', package])

#os.system("python get-pip.py")
#install("argparse")
#install("gooey")
addMyGooeyFiles()
