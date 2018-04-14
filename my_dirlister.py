import os
import csv

srcpath = r'D:\Users\srinivasandp\Downloads\srinivasan\dropit\Dropbox'
size_mb = 1024*1024

print("start dir lister")

if (os.path.isdir(srcpath)):
    print('path exists')
else:
    print('path does not exists')
    exit

fsize = {}
for cfolder,sfolders,filenames in os.walk(srcpath):
    fsize.setdefault(cfolder,0)
    #print(cfolder)

for cfolder,sfolders,filenames in os.walk(srcpath):
    foldersize = 0

    for files in os.listdir(cfolder):
        foldersize = foldersize + os.path.getsize(os.path.join(cfolder,files))

    foldersize = foldersize/size_mb

    print()
    #print("cf:{}".format(cfolder))
    for keys in fsize:
        if keys in cfolder:
            #print("=> key:{}".format(keys))
            fsize[keys] += foldersize

cwdpath = os.getcwd()

wpath = os.path.join(cwdpath,"dirlist.txt")
wfile = open(wpath, 'w')
wfile.write('Dir List\n')
wfile.close()

csvpath = os.path.join(cwdpath,"dirlist.csv")
csvfile = open(csvpath,'w',newline='')
csvwriter = csv.writer(csvfile)
header = ['path','size']
csvwriter.writerow(header)

wfile = open(wpath, 'a')

for cfolder,sfolders,filenames in os.walk(srcpath):
    text = cfolder.replace(srcpath,'')
    text = text.replace('\\',',')
    #print(text)
    #print("{},{:.2f}{}".format(cfolder,fsize[cfolder],text))

    ##text file write
    data = "{},{:.2f}{}\n".format(cfolder,fsize[cfolder],text)
    #print(data)
    wfile.write(data)

    ##csv file write
    data = "{},{:.2f}{}".format(cfolder,fsize[cfolder],text)
    #print(data)
    csvdata = data.split(',')
    #print(csvdata)
    csvwriter.writerow(csvdata)

wfile.close()
csvfile.close()

print("end dir lister")