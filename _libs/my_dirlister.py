import os
import csv

##global
fsize = {}
size_mb = 1024*1024

##lib
def pathcheck(path, ptype):
    status = False
    if(ptype == 'f'):
        if(os.path.isfile(path)):
           #print('file exists')
           status = True
        else:
            #print('no file exists => {}'.format(path))
            pass
    else:
        if (os.path.isdir(path)):
            #print('path exists')
            status = True
        else:
            print('no path exists => {}'.format(path))
    return status

##process
def dirlister_p(srcpath):

    for cfolder,sfolders,filenames in os.walk(srcpath):
        fsize.setdefault(cfolder,0)
        #print(cfolder)

    for cfolder,sfolders,filenames in os.walk(srcpath):
        foldersize = 0
        for files in os.listdir(cfolder):
            foldersize = foldersize + os.path.getsize(os.path.join(cfolder,files))
        foldersize = foldersize/size_mb
        #print("cf:{}".format(cfolder))
        for keys in fsize:
            if keys in cfolder:
                #print("=> key:{}".format(keys))
                fsize[keys] += foldersize

##output
def dirlister_o(srcpath, txtpath, csvpath):

    txtfile = open(txtpath, 'a')
    csvfile = open(csvpath,'a',newline='')
    csvwriter = csv.writer(csvfile)

    for cfolder,sfolders,filenames in os.walk(srcpath):
        text = cfolder.replace(srcpath,'')
        text = text.replace('\\',',')
        #print(text)
        #print("{},{:.2f}{}".format(cfolder,fsize[cfolder],text))

        ##text file write
        data = "{},{:.2f}{}\n".format(cfolder,fsize[cfolder],text)
        #print(data)
        txtfile.write(data)

        ##csv file write
        data = "{},dir,{:.2f}{}".format(cfolder,fsize[cfolder],text)
        #print(data)
        csvdata = data.split(',')
        #print(csvdata)
        csvwriter.writerow(csvdata)

        for file in os.listdir(cfolder):
            if(pathcheck(os.path.join(cfolder,file),'f') == True):
                size = os.path.getsize(os.path.join(cfolder,file))/size_mb
                data = "{},{:.2f}\n".format(file,size)
                txtfile.write(data)
                data = "{},file,{:.2f}".format(file,size)
                #print(data)
                csvdata = data.split(',')
                #print(csvdata)
                csvwriter.writerow(csvdata)

    txtfile.close()
    csvfile.close()


##input
def dirlister_i():
    iofile = open('_io_dirlister.csv','r')
    csv_reader = csv.DictReader(iofile)
    outputlist = []

    for line in csv_reader:
        #print(line)
        src = line['input path']
        dst = line['output path']
        ##check for input path
        if(pathcheck(src,'d') == False):
            continue;
        ##check for empty output path
        if dst == '':
            dst = os.getcwd()
        ##check for empty output file
        if line['output file'] == '':
            line['output file'] = 'o_dirlister'
        dst_text = dst + '\\' + line['output file'] + '.txt'
        dst_csv = dst + '\\' + line['output file'] + '.csv'
        #print(src)
        #print(dst_text)
        #print(dst_csv)

        ##process
        dirlister_p(src)

        if dst_text not in outputlist:
            outputlist.append(dst_text)
            ##pre-condition text
            txtfile = open(dst_text, 'w')
            txtfile.write('dir lister\n')
            txtfile.close()
            ##pre-condition csv
            csvfile = open(dst_csv,'w',newline='')
            csvwriter = csv.writer(csvfile)
            header = ['path','type','size']
            csvwriter.writerow(header)
            csvfile.close()

        ##output
        dirlister_o(src,dst_text, dst_csv)

##main
def dirlistermain():
    print("start dir lister")

    dirlister_i()

    print("end dir lister")

dirlistermain()

