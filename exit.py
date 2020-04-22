import csv
from datetime import datetime

now = datetime.now()

with open("res_log.csv", 'a+') as g, open("vis_log.csv", 'a+') as h:
    reader = csv.reader(g)
    next(reader, None)
    writerR = csv.writer(g, delimiter=',')
    writerV = csv.writer(h, delimiter=',')
    file1 = open("myfile.txt","r+") #myfile.txt contains scanned vehicle no.
    flag=0
    fr=file1.read()
    for row in reader:
        if (row[0] == fr):
            flag=1
            row[3] = now.strftime("%d/%m/%Y %H:%M:%S")
            writerR.writerow(row)
            print("Exit Time noted Successfully in Resident's Log")
            break

    reader2 = csv.reader(h)
    next(reader2, None)
    if flag==0:
        for row in reader2:
            if (row[0] == fr):
                row[4] = now.strftime("%d/%m/%Y %H:%M:%S")
                writerV.writerow(row)
                print("Exit Time noted Successfully in Resident's Log")
                break       
    


