import csv
import re
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import random
import pickle
import os

stop_words = list(set(stopwords.words('english')))

nc=0
pc=0
fields=['Comment','Polarity','Subjectivity']
dict=[]
with open('reddit_data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open('new_data.csv', mode='w') as write_file:
        csv_writer=csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
        csv_writer.writerow(fields)
        for row in csv_file:
            analysis=TextBlob(row)
            dict=[row,analysis.sentiment.polarity,analysis.sentiment.subjectivity]
            if analysis.sentiment.polarity!=0 and analysis.sentiment.subjectivity!=0:
                csv_writer.writerow(dict)
            dict=[]

with open('new_data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csv_file:
        print(row)





        # if analysis.sentiment.polarity <-0.5:
        #     nc=nc+1
        #     #print(row)
        #     #print(analysis.sentiment)
        # elif analysis.sentiment.polarity==0:
        #     continue
        # else:
        #     pc=pc+1

# print("Negative Counts in Preliminary Dataset = ",nc)
# print("Positive Counts in Preliminary Dataset = ",pc)
# negposratio=nc/pc
# print("Negative to Positive Ratio = ",negposratio)
