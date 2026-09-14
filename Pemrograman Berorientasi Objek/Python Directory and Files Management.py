# Get Current Directory in Python
import os
import shutil


print(os.getcwd())

# Output: C:\Program Files\PyScripter

# Changing Directory in Python
# change directory
os.chdir(r'C:\Users\aqila\OneDrive\Dokumen\Pemrograman Berorientasi Objek')

print(os.getcwd())

# Output: C:\Users\aqila\OneDrive\Dokumen\Pemrograman Berorientasi Objek

# List Directories and Files in Python
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

# Making a New Directory in Python
# os.mkdir('test')

# os.listdir()
# ['test']

# Renaming a Directory or a File
# os.listdir()
# ['test']

# rename a directory
# os.rename('test','new_one')

# os.listdir()
# ['new_one']

# Removing Directory or File in Python
# delete "myfile.txt" file
# os.remove("myfile.txt")

# delete the empty directory "mydir"
# os.rmdir("mydir")

# delete "mydir" directory and all of its contents
# shutil.rmtree("mydir")