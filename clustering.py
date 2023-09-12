from sklearn.datasets import make_blobs
import pandas as pd
import numpy as np
import math
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 


sns.set_palette("Set2")


x,y = make_blobs(n_samples=100,centers=4,n_features=2,random_state=6)
points = pd.DataFrame(x,y).reset_index(drop=True)
points.columns=['x','y']
points.head()

# k-means clustering 실행
kmeans = KMeans(n_clusters=4)
kmeans.fit(points)

# 결과 확인
result_by_sklearn = points.copy()
result_by_sklearn["cluster"] = kmeans.labels_
result_by_sklearn.head()











sns.scatterplot(x="x", y="y", data=points, palette="Set2")

centroids = points.sample(4, random_state=1)
centroids

# 각 데이터에 대하여, 각 중심점과의 유클리드 거리 계산
distance = sp.spatial.distance.cdist(points, centroids, "euclidean")

# 가장 거리가 짧은 중심점의 cluster로 할당
cluster_num = np.argmin(distance, axis=1)

# 결과 확인
result = points.copy()
result["cluster"] = np.array(cluster_num)
result.head()