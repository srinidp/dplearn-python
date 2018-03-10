import os

srcpath = "D:\\Users\\srinivasandp\\Downloads\\srinivasan\\learn"
cwdpath = os.getcwd()

sizemax = 1024*1024
print(sizemax)

wpath = os.path.join(cwdpath,"dirlist.txt")
wfile = open(wpath, 'w')
wfile.write('Dir List\n')
wfile.close()

wfile = open(wpath, 'a')

for cfolder,sfolders,filenames in os.walk(srcpath):
    foldersize = 0
    for files in os.listdir(cfolder):
        foldersize = foldersize + os.path.getsize(os.path.join(cfolder,files))

    if foldersize/sizemax < 1:
        foldersize = 0
    else:
        foldersize = foldersize/sizemax

    #print(cfolder, "," ,foldersize)
    data = cfolder + "," + str(foldersize) + "\n"
    wfile.write(data)

wfile.close()

print("")