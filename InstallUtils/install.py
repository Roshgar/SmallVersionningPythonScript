import os
import pip

def install(package):
    pip.main(['install', package])

os.system("python get-pip.py")
install("argparse")
install("gooey")
