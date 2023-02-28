#!/usr/bin/env python3
import os


# Get the list of all files and directories
for file in os.listdir(r'/home/wangbi/mapped_reads'):
     # check the files which are end with specific extension
    if file.endswith(".vcf"):
        print(os.path.join("/home/wangbi/mapped_reads", file))
        wsize = 500

        rid = []
        counts = 0
        num =0;

        f = open(os.path.join("/home/wangbi/mapped_reads", file), "r")
        fw = open("/home/wangbi/output/"+file+".out", "w")
        myline = f.readline()
        fw.writelines("START" + '\t' +"END"+'\t'+ "COUNTS" + '\n');
        while myline:
            if (myline[0] != '#') :

                num+=1;
                cols = myline.split("\t")
                if (cols[4] != "<*>"):
                       # print(cols[4])
                        counts+=1
                        rid.append(num)
                if (num >=wsize) :
                        if (len(rid)>0):
                                if (num-rid[0]) >= wsize:
                                        rid.pop(0)
                                        counts-=1
                        if ((num % 250) == 0):
                            fw.writelines(format(num-499) + '\t'+format(num)+'\t' + "{}".format(counts)+'\n' )
            myline=f.readline()
        f.close()
        fw.close()
