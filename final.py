import pandas as pd
from sklearn.cluster import KMeans
df1 = pd.read_csv('df_final.CSV')
df2=pd.read_csv('bike_latlong.csv')
print(df1.head())
print(df2.head())
list1=[]
df1['bike_num']=df2['qr_code']
df1.to_csv('finalx1.csv')

