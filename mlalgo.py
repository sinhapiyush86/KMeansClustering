from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('finalx1.csv')
df.drop('Unnamed: 0',axis=1,inplace=True)
df.drop('Unnamed: 0.1',axis=1,inplace=True)
df.drop('bike_num',axis=1,inplace=True)
print(df.head())
var=int(input("enter no of cluster to make"))
kmeans=KMeans(n_clusters=var)
kmeans.fit(df)
centroids=kmeans.cluster_centers_
labels=kmeans.labels_
df['labels'] = labels
df.to_csv('finalx1.csv')
print(df.head())
long=[]
lat=[]
print(centroids)
for i in centroids:
    lat.append(i[0])
    long.append(i[1])
df1 = pd.DataFrame({'lat':lat,'long':long})
df1.to_csv('usercentdata.csv')
print(labels)
plt.scatter(df['latitude'],df['longitude'],c=kmeans.labels_,cmap='rainbow')
plt.show()
