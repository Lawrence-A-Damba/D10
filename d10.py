import os
import fnmatch
readFile=open('totalFile','w')
dirFile=os.listdir(path='.')
     
for file in dirFile:
    if fnmatch.fnmatch(file,'*.txt'):
        print(file,file=readFile)
    else:
        pass
    
readFile.close()
