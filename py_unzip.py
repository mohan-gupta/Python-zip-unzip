#importing all the functions from zipfile library
from zipfile import *

#-------EXTRACTING ZIP FILE--------

#opening the zipfile by using ZipFile constructor in read mode('r')
with ZipFile("file.zip","r") as z:

    # extracting all the file in a folder in which you want the files.
    z.extractall("folder")

print("files extracted")
