import os

def download(LibcNameList):
    for item in LibcNameList:
        os.system("./download {}".format(item))

def mkDir(name):
    for item in name:
        os.system("sudo mkdir -p /glibc/{}/64/lib/".format(item))
        os.system("sudo mkdir -p /glibc/{}/32/lib/".format(item))

def getName(LibcNameList):
    name=[]
    for item in LibcNameList:
        if item.split("-")[0] in name or item.split("-")[0]=="" :
            continue
        else:
            name.append(item.split("-")[0])
    print("name:",name)
    return name

os.system("./update_list")

f=open("./list","r")
content=f.read()

print(content)
LibcNameList=content.split("\n")

name=getName(LibcNameList)
mkDir(name)


download(LibcNameList)
for LibcName in LibcNameList:
    

    for item in name:
        
        if (item in  LibcName) and ("amd64" in LibcName):
            
            os.system("sudo cp ./libs/{}/* /glibc/{}/64/lib/".format(LibcName,item))
        if (item in LibcName) and ("i386" in LibcName):
            os.system("sudo cp ./libs/{}/* /glibc/{}/32/lib/".format(LibcName,item))
