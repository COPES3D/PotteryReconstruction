import matplotlib.pyplot as plt

#from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE

import umap

import numpy as np
import matplotlib.patches as mpatches



#iris = datasets.load_iris()
#X = iris.data
#print(type(X))
#y = iris.target

X = []
y = []

f = open("/home/jeff/data_visualization.txt", "r")
for line in f:
  #print(line)
  label,features = line.split(";") 
  #print(label)
  features = features.split(",")
  #print(type(features))
  features = np.asarray(features)
  features = np.resize(features, features.size - 1)
  features = features.astype(np.float)
  #print(features)
  X.append(features)
  y.append(int(label))


X = np.asarray(X)
#print(X)
y = np.asarray(y)
#print(y)


categories = ['Alabastron','Amphora','Hydria','Kalathos','Krater','Kylix','Lekythos','Native-American-Bottle','Pelike','PicherShaped','Psykter']

#generate random colors
colors = []
for i in range(len(categories)):
	colors.append(np.random.rand(3,))


#Create Legends
patches = []
for i in range(len(categories)):
	patch = mpatches.Patch(color=colors[i], label=categories[i])	
	patches.append(patch)



pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)



# Percentage of variance explained for each components
#print('explained variance ratio (first two components): %s'
#      % str(pca.explained_variance_ratio_))


lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)



tsne = TSNE(n_components=2)
X_r3 = tsne.fit_transform(X)


reducer = umap.UMAP()
X_r4 = reducer.fit_transform(X)

print(X_r4)



plt.figure()
plt.title('PCA MeshCNN 48%')
plt.legend(handles=patches)
#plotear
for i in range(len(X_r)):
	plt.scatter(X_r[i][0],X_r[i][1], marker='o',color=colors[y[i]])



plt.figure()
plt.title('LDA MeshCNN 48%')
plt.legend(handles=patches)
#plotear
for i in range(len(X_r2)):
	plt.scatter(X_r2[i][0],X_r2[i][1], marker='o',color=colors[y[i]])


plt.figure()
plt.title('TSNE MeshCNN 48%')
plt.legend(handles=patches)
#plotear
for i in range(len(X_r3)):
	plt.scatter(X_r3[i][0],X_r3[i][1], marker='o',color=colors[y[i]])


plt.figure()
plt.title('UMAP MeshCNN 48%')
plt.legend(handles=patches)
#plotear
for i in range(len(X_r4)):
	plt.scatter(X_r4[i][0],X_r4[i][1], marker='o',color=colors[y[i]])




plt.show()


