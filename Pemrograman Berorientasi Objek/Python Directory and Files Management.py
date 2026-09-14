#Get Current Directory in Python
import os

print(os.getcwd())

# Output: C:\Program Files\PyScripter

#Changing Directory in Python
import os

# change directory
os.chdir(r'C:\Users\aqila\OneDrive\Dokumen\Pemrograman Berorientasi Objek')

print(os.getcwd())

# Output: C:\Users\aqila\OneDrive\Dokumen\Pemrograman Berorientasi Objek

#List Directories and Files in Python
import os

print(os.getcwd())
# C:\Users\aqila\OneDrive\Dokumen\Pemrograman Berorientasi Objek

# list all sub-directories
os.listdir()
# ['DLLs',
# 'Doc',
# 'include',
# 'Lib',
# 'libs',
# 'LICENSE.txt',
# 'NEWS.txt',
# 'python.exe',
# 'pythonw.exe',
# 'README.txt',
# 'Scripts',
# 'tcl',
# 'Tools']

# os.listdir('G:\\')
# ['$RECYCLE.BIN',
# 'Movies',
# 'Music',
# 'Photos',
# 'Series',
# 'System Volume Information']

#Making a New Directory in Python
# os.mkdir('test')

# os.listdir()
# ['test']

#Renaming a Directory or a File
import os

# os.listdir()
# ['test']

# rename a directory
# os.rename('test','new_one')

# os.listdir()
# ['new_one']

#Removing Directory or File in Python
import os

# delete "myfile.txt" file
# os.remove("myfile.txt")

import os

# delete the empty directory "mydir"
# os.rmdir("mydir") 

import shutil

# delete "mydir" directory and all of its contents
# shutil.rmtree("mydir")