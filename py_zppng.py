#importing all the functions from zipfile library
from zipfile import *


#--------CREATING ZIP FILE---------
#initialising Zipfile constructor

# arguments: file Path(file in which you want to save the zip files/folders),
                                                                # mode(w:write), ZIP_DEFLATED(since we want to compress the file)
z = ZipFile("file.zip","w",ZIP_DEFLATED)

#Add the file which you want to zip by passing its path
z.write("py_zip")

#closing the zipfile
z.close()
print("File Saved")

