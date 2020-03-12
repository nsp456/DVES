import ages_scan
import pandas as pd

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
      with open('visitor_log.csv','a') as f:
            df.to_csv(f,header=False)
            df.append([vno,name,flat])
            
            
