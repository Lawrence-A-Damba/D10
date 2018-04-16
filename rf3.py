import os
import fnmatch
readFile=open('totalFile','w')
dirFile=os.listdir(path='.')
file2read=open('fileTwoRead','w')
files=[]
for file in dirFile:
    if fnmatch.fnmatch(file,'*.txt'):
        files.append(file)
    else:
        pass
print(files)

for name in files:
    print(name)
    rf=open(name,'r')
    for line in rf:
        try:
            num=float(line[68:73])
            print(line[0:5],num)
        except:
            pass

readFile.close()
file2read.close()
