import csv
import re
import os

files_pos = os.listdir('Dataset/neg/Parameters/')
#files_pos = [open('test/pos/'+f, 'r',errors='ignore').read() for f in files_pos]

with open('neg_textblob_data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
    i=0
    for row in csv_file:
        #row=row.split(",",2)
        if i==0:
            i=i+1
            continue
        filename=str(i)+'.txt'
        file_txt=open('Dataset/neg/Parameters/'+filename,'w')
        file_txt.write(row+'\n')
        i=i+1



# file_txt=open('testfile.txt','r+')
# print(file_txt.readlines())
