#import dves_scan
import pandas as pd
from datetime import datetime
import csv
from csv import *
now = datetime.now()
#from csv import writer 
sensor_range=65
def entry_check(text):
    resDb=pd.read_csv('resDB.csv')
    flag=0
    row1=0
    for i in resDb['Vehicle No.']:
          row1+=1
          if(i==text):
                  flag=1
                  break
    if(flag==1):
        print("\nIs a Resident")
        with open('res_log.csv','r+',newline='') as f:
            
            for row in f:
                j=row.split(",")
                if j[0]==text and len(j[3])<3:
                    print("Vehicle Already Inside ,Please try Exit Scan")
                    return -1
            cw=writer(f)
            
            cw.writerow([text,resDb['Flat No.'][row1-1],datetime.now().replace(microsecond=0),""])
        
    else:
        print("\nIs a Visitor")
        with open('vis_log.csv','r') as f:
            print("Hey")
            for row in f:
                i=row.split(",")
                #print(i[0]+" "+i[4])
                if i[0]==text and i[4]=="\n":
                    print("Vehicle Already Inside ,Please try Exit Scan")
                    return -1
    return flag

def vis_entry_log(vno,name,flat):
      print(vno,name,flat)
      
      with open('vis_log.csv','a+',newline='') as f:
            cw=writer(f)
            cw.writerow([vno,name,flat,datetime.now().replace(microsecond=0),""])

      return 1


            
def exit_log(text):
    #resDb=pd.read_csv('resDB.csv')
    rl_in=open("res_log.csv","r")
    
    rlreader=reader(rl_in)
    
    rl_out=open("temp.csv","w",newline='')
    
    rlwriter=writer(rl_out)
    resflag=0
    flag=0
    #print("Hey")
    for row in rlreader:
        #print(row)
        if row[0]==text:
            resflag=1
            if(row[3]==""):
                flag=1
                row[3]=datetime.now().replace(microsecond=0)
            
        rlwriter.writerow(row)
    rl_in.close()
    rl_out.close()

    if(resflag==1 and flag==0):
        print("\nVehicle already outside,Please try Entry Scan")
        return -1
    
            
    if(resflag!=1):
        flag=-1
        vl_in=open("vis_log.csv","r")
        vlreader=reader(vl_in)
        vl_out=open("temp.csv","w",newline='')
        vlwriter=writer(vl_out)
        
        for row in vlreader:
            if not row:
                continue
            #print(row)
            if row[0]==text and row[4]=="":
                flag=1
                row[4]=datetime.now().replace(microsecond=0)
            vlwriter.writerow(row)
        vl_in.close()
        vl_out.close()
        if(flag==-1):
            print("\nVehicle already outside,Please try Entry Scan")
            return -1

    in_file=open("temp.csv","r")
    out_file=open("res_log.csv" if resflag==1 else "vis_log.csv","w",newline='')
    newreader=reader(in_file)
    newwriter=writer(out_file)
    for row in newreader:
        newwriter.writerow(row)
    return 1
            
def getRepData(log,date,start,end):
    start=datetime.strptime(date+" "+start,'%Y-%m-%d %H:%M:%S')
    end=datetime.strptime(date+" "+end,'%Y-%m-%d %H:%M:%S')
    repList=[]
    if(log=="Resident Log"):
        file=open("res_log.csv","r")
        idx=2
    else:
        file=open("vis_log.csv","r")
        idx=3
    k=0
    for rows in file:
        if not rows:
            continue
        if(k==0):
            k=1
            continue
        row=rows.split(",")
        print(row[idx]+" "+row[idx+1])
        entrydt=datetime.strptime(row[idx],'%Y-%m-%d %H:%M:%S')
        """
        if(entrydt.date()==date):
            if(entrydt.time()>=start and entrydt.time()<=end):
                repList.append(row)
                continue
        """
        if(entrydt>=start and entrydt<=end):
            repList.append(row)
            continue
        if(len(row[idx+1])>2):
            
            exitdt=datetime.strptime(row[idx+1],'%Y-%m-%d %H:%M:%S ')
            if(exitdt>=start and exitdt<=end):
                repList.append(row)
                continue
            
    return repList

#print(getRepData("Resident Log","2020-05-20","00:00:00","05:00:00"))    
#entry_check("MH06AJ8034")  
#exit_log("A7M9590")
#print("Success")
#vis_entry_log("AM1234","Strange","B221")
#print("Success")
            
            
