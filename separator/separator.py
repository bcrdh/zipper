import os
import shutil

def segregate(source, destination):
    # Changing current working directory
    os.chdir(source)
    # Get a list of files
    files = os.listdir(os.getcwd())
    new = 0
    size = 0
    newDestination = createDirectory(destination,new)
    new += 1

    while files:
        file1 = source + "/" + files[0]
        file2 = source + "/" + files[1]
        size = size+os.path.getsize(file1)+os.path.getsize(file2)
        print(size)
        #while size is less than 2.5 GB
        if size <= 451711331:#137935131:#2684354560:
            shutil.move(file1, newDestination)
            shutil.move(file2, newDestination)
            del files[0:2]
            print(files)
        else:
            newDestination = createDirectory(destination, new)
            new += 1
            size=0
            print("seze: "+str(size))

def createDirectory(destination, new):
    os.chdir(destination)
    os.mkdir(str(new))
    destination = destination + "/" + str(new)
    return destination

#Defining the directory with XML and TIFF as source
source="C:/Users/yoits/OneDrive/Desktop/Trial/012058"
#Defining the destination to move files as dest
dest="C:/Users/yoits/OneDrive/Desktop/Trial"
#Calling segregate()
segregate(source, dest)
