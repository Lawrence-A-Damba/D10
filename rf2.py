fileName=input("File name to open? ")
readFile=open(fileName,'r')
rf=readFile.readlines()

for line in rf:
    try:
        num=float(line[68:73])
        print(line[0:5],num)
    except:
        pass

readFile.close()
