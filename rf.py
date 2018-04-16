fileName=input("File name to open? ")
readLine=input("Read line? ")
readFile=open(fileName,'r')
rf=readFile.readlines()
nl=rf[int(readLine)]
print(nl[0:5],nl[68:73])
readFile.close()
    
