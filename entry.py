import csv
from datetime import datetime

now = datetime.now()

with open("resDB.csv") as f, open("res_log.csv", 'a+') as g, open("vis_log.csv", 'a+') as h:
    reader = csv.reader(f)
    next(reader, None)
    writerR = csv.writer(g, delimiter=',')
    writerV = csv.writer(h, delimiter=',')
    file1 = open("myfile.txt","r+")
    flag=0
    fr=file1.read()
    for row in reader:
        if (row[0] == fr):
            flag=1
            break
    if flag==1:
        writerR.writerow([row[0],row[1],now.strftime("%d/%m/%Y %H:%M:%S")])
        print("Entry Done Successfully in Resident's Log")
    else:
        name=input("Enter Name of Visitor: ")
        fno=input("Enter Flat No. Visiting: ")
        writerV.writerow([fr,name,fno,now.strftime("%d/%m/%Y %H:%M:%S")])
        print("Entry Done Successfully in Visitor's Log")

       
    


