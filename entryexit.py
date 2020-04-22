import pandas as pd
import numpy as np
import time

global res_log
global residential
global vis_log
residential=pd.read_csv('resDB.csv',names=['VehicleNo.','FlatNo.','Name','MobileNo.'])
res_log=pd.read_csv('res_log.csv')
vis_log=pd.read_csv('vis_log.csv')

def add_entry(number):
    flag=1
    named_tuple = time.localtime() # get struct_time
            
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    for i in range(1,len(residential)):
        if (residential.iloc[i][0]==number):
            
            data=pd.DataFrame({"VehicleNo.":[number],"FlatNo.":[residential.iloc[i][1]],"EntryTime":[str(time_string)],"ExitTime":np.NaN})
            r=res_log.append(data,sort=True)
##            res_log.loc[len(res_log.index)]=list(res_log[0].values())
            r.to_csv('res_log.csv',index=False)
            flag=0
            break
    if flag==1:
        name=input("Enter the name")
        flat=input("Enter the flat no")
        data=pd.DataFrame({"VehicleNo.":[number],"NameofVisitor":[name],"FlatNo.Visiting":[flat],"EntryTime":[str(time_string)],"ExitTime":np.NaN})
        r=vis_log.append(data,sort=True)
        r.to_csv('vis_log.csv',index=False)


def exit(number):
    flag=1
    named_tuple = time.localtime() # get struct_time
            
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    for i in range(len(res_log)):
        if res_log.iloc[i][3]==number:
            print(res_log.iloc[i][3])
            s=str(time_string)
##            print(s[11])
            data=list(res_log.iloc[i])
            print(data)
##            res_log.iloc[i]=pd.DataFrame[{"ExitTime":[str(time_string)]}]
            res_log.iloc[i]=res_log.iloc[i].replace(np.NaN,str(time_string))
##            print(abc+"j")
##            data2=pd.DataFrame({[],"FlatNo.":[data[1]],"EntryTime":[data[2]],"ExitTime":[str(time_string)]})
##            res_log.iloc[i]=data2
            res_log.to_csv('res_log.csv',index=False)
            flag=0
            break
    if flag==1:
        for i in range(1,len(vis_log)):
            if vis_log.iloc[i][4]==number:
                vis_log.iloc[i]=vis_log.iloc[i].replace(np.NaN,str(time_string))
                vis_log.to_csv('vis_log.csv',index=False)
                break
                

##add_entry('MH04SD3241')
##data=list(res_log.iloc[1])
##print(data)
##data=pd.DataFrame({"VehicleNo.":["MH08DF3423"],"FlatNo.":["A223"],"Name":["Sid"],"MobileNo.":["23424232"]})
##exit('MH06AY8034')


add_entry('MH06AJ7781')

print(res_log)
##print(residential)
##residential=residential.append(data)
##residential.to_csv('res_log.csv',index=False)
##print(residential)
