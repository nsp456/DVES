import pandas as pd
import numpy as np
import time

global res_log
global residential
global vis_log
residential=pd.read_csv('C:\\Users\\Siddharth\\Desktop\\DBMS IA A\\resDB.csv',names=['VehicleNo.','FlatNo.','Name','MobileNo.'])
res_log=pd.read_csv('C:\\Users\\Siddharth\\Desktop\\DBMS IA A\\res_log.csv')
vis_log=pd.read_csv('C:\\Users\\Siddharth\\Desktop\\DBMS IA A\\vis_log.csv')

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


def exit_(number):
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
        for i in range(len(vis_log)):
            if vis_log.iloc[i][4]==number:
                vis_log.iloc[i]=vis_log.iloc[i].replace(np.NaN,str(time_string))
                vis_log.to_csv('vis_log.csv',index=False)
                break
                

##Detection of fraud

# print(res_log)
def fraudentry(number):
    for i in range(len(res_log)):
        if (res_log.iloc[i][3]==number and np.isnan(res_log.iloc[i][1])):
            print(res_log.iloc[i][3])
            return False
    for i in range(len(vis_log)):
        if vis_log.iloc[i][4]==number and np.isnan(vis_log.iloc[i][1]):
            return False
    return True


##eg:
##if vehicle is inside an a fraud vehicle comes and tries to enter then this function is used
##the logic is to find the fraud is:
##    the vehicle with same number will have entry time but not exit time because its np.NaN
##to use this function
##
##////////////
##if fraudentry(number):
##    add_entry(number)

def fraudexit(number):
    for i in range(len(res_log)):
        if (res_log.iloc[i][3]==number and np.isnan(res_log.iloc[i][1])):
            print(res_log.iloc[i][3])
            return True
    for i in range(len(vis_log)):
        if vis_log.iloc[i][4]==number and np.isnan(vis_log.iloc[i][1]):
            return True
    return False
    




##how to use function to catch fraud:
#     if fraudentry('MH12AD2324'):
#         add_entry('MH12AD2324')

#     if fraudexit('MH12AD2324'):
#         exit('MH12AD2324')
