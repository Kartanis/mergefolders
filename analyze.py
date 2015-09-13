import hashlib
import os
import sys

__author__ = 'sbilyi'


def loadFolder(path):
    print os.path.isdir(path)

    files = []
    subfolders = []

    for afile in os.listdir(path):
        if os.path.isdir(os.path.join(path, afile)):
            subfolders.append(afile)
            afile += "[D]"
        else:
            files.append(afile)
            afile += "[F]"

    # print "Files: " + str(files)
    # print "SubFolders are: " + str(subfolders)
    return {"files": files, "folders": subfolders}


print "start"

# starting with determining source folder

if len(sys.argv) != 2:
    print "Program usage is: mergefolders.py path"
    exit()

print loadFolder(os.path.dirname(os.path.realpath(sys.argv[1])))

BLOCKSIZE = 65536
hasher = hashlib.sha1()
with open('test1', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())

md = hashlib.sha1()
md.update("Some text message")
print md.hexdigest()

print os.path.dirname(os.path.realpath(__file__))
print os.listdir(os.path.dirname(os.path.realpath(__file__)))

print "end"
