import hashlib
import os
import sys

__author__ = 'sbilyi'

def loadFileInfo(path):
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    size = 0
    with open(path, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        if len(buf) > 0: #first time we are doing has from first block to get faster results
            size += len(buf)
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)

    result = {'name': path, 'size': os.stat(path).st_size, 'sha1': hasher.hexdigest(), 'type': 'FILE'}

    #print result
    return result


def loadFolder(path, outputFile):
    print path

    files = []
    subfolders = []

    for afile in os.listdir(path):
        if os.path.isdir(os.path.join(path, afile)):
            loadFolder(os.path.join(path, afile), outputFile)

        else:
            outputFile.write(str(loadFileInfo(os.path.join(path, afile))))
            #files.append()

    # print "Files: " + str(files)
    # print "SubFolders are: " + str(subfolders)
    return {"files": files, "folders": subfolders}


print "start"

# starting with determining source folder

if len(sys.argv) != 2:
    print "Program usage is: mergefolders.py path"
    exit()

outputFileName = os.path.join(os.path.dirname(os.path.realpath(sys.argv[1])), "mergefolder.txt")
#if os.path.exists(outputFileName):
#    outputFileName.join(1);

print outputFileName

print str(os.listdir(os.path.realpath(sys.argv[1])))
with open(outputFileName, 'w') as outputFile:
    loadFolder(os.path.realpath(sys.argv[1]), outputFile)


md = hashlib.sha1()
md.update("Some text message")
print md.hexdigest()

print os.path.dirname(os.path.realpath(__file__))
print os.listdir(os.path.dirname(os.path.realpath(__file__)))

print "end"
