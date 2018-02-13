import pandas as pd
df = pd.read_csv('finalx1.csv')
df.drop('Unnamed: 0',axis=1,inplace=True)
x = int(input('enter bike number'))
df1 = pd.read_csv('bike_latlong.csv')
df['bike_no'] = df1['qr_code']
df.to_csv('labelfinder.csv')
y=df.loc[df['bike_no']==x]
df2=pd.read_csv('usercentdata.csv')
t1=df2['lat'][y['labels']]
t2=y['latitude']
t4=df2['long'][y['labels']]
t5=y['longitude']
t3=float(t1)-float(t2)
t6=float(t4)-float(t5)
print(t3)
print(t6)
