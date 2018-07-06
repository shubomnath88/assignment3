import pandas as pd
#ques1
data = {'name':['shubom','varun'],'age':[20,22],'mail_id':['shubomnath88@gmail.com','varun@email.com']}
df=pd.DataFrame(data)
print(df)

#ques2
#1.
df = pd.read_csv("sample.csv")
print(df.head())
#2
df = pd.read_csv("sample.csv",nrows=10)
print(df)
#3
print(df.describe())
#4
df = pd.read_csv("sample.csv",skiprows=366-5)
print(df)
#5
df = pd.read_csv("sample.csv",skiprows=1,nrows=1)
print(df)
print(df.describe())
