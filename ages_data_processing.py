import ages_scan
import pandas as pd
from csv import writer 

def entry_check(text):
    resDb=pd.read_csv('Resident Database.csv')
    flag=0
    for i in resDb['Vehicle No.']:      
          if(i==text):
                  flag=1
                  break
    if(flag==1):
        print("\nIs a Resident")
    else:
        print("\nIs a Visitor")
    return flag

def vis_entry_log(vno,name,flat):
      print(vno,name,flat)
      
      with open('visitor_log.csv','a+',newline='') as f:
            cw=writer(f)
            cw.writerow([vno,name,flat,"",""])

      return 1
            

#vis_entry_log("AM1234","Strange","B221")
#print("Success")
            
            
