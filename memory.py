import pandas as pd
import docx
from fnreadfilename import readfilesname
path = '/Users/admin/Documents/Time/THP 2023-2024/12Apr'
x = readfilesname(path)
print(x)
a=0
df = pd.DataFrame(columns=['DB Name', 'Use','Total'])
while a<(len(x)):
    df1 = pd.read_csv(path+'\\'+x[a],header=None)
    df1 = df1.rename(columns={0: 'DB Name',1:'Use',2:'Total'})
    df1.iloc[0,0]= x[a]
    frames = [df,df1]
    df = pd.concat(frames)
    a=a+1
print(df)