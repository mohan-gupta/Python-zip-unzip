#importing all the functions from zipfile library
from zipfile import *


#--------CREATING ZIP FILE---------
#initialising Zipfile constructor
# arguments: file Path, mode(w:write), ZIP_DEFLATED(since we want to compress the file)
z = ZipFile("file path","w",ZIP_DEFLATED)

#Add the file, which you want to zip by passing its path
z.write("file path")

#closing the zipfile
z.close()
print("File Saved")

#-------EXTRACTING ZIP FILE--------

#opening the zipfile by using ZipFile constructor in read mode('r')
with ZipFile("file path (extension: .zip)","r") as z:
    # extracting all the file in a folder in which you want the files.
    z.extractall("folder name")
    #to extract single file --  z.extract("filename to be extracted")

print("files extracted")
