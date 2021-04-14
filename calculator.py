import pandas  as pd #Data manipulation
from sklearn import linear_model
import numpy as np #Data manipulation
import matplotlib.pyplot as plt # Visualization
import os

plt.rcParams['figure.figsize'] = [8,5]
plt.rcParams['font.size'] =14
plt.rcParams['font.weight']= 'bold'
#path ='dataset/'
path = 'datafull.csv'
dataset = pd.read_csv(path)
#print('\nNumber of rows and columns in the data set: ',dataset.shape)

Y = dataset[['price']]

X = dataset.drop(['price'],  axis=1)

#X.info()
#print(Y)
x = np.array(X.values)
y = np.array(Y.values)
#print(type(x))
regr = linear_model.LinearRegression()
regr.fit(x, y)
w=regr.coef_
#=============
#print to argument file

if os.path.exists("argument.csv"):
  os.remove("argument.csv")
#f = open("argument.csv", "a")


#stringdata=str(w_0)+","+str(w_1)+","+str(w_2)+","+str(w_3)+","+str(w_4)
dataInt=pd.DataFrame([[ w[0][0],w[0][1],w[0][2],w[0][3],w[0][4],w[0][5],w[0][6],w[0][7],w[0][8],w[0][9],w[0][10],w[0][11],regr.intercept_[0]]], columns=['w_0','w_1','w_2','w_3','w_4','w_5','w_6','w_7','w_8','w_9','w_10','w_11','w_12'])
dataInt.to_csv("argument.csv", index=False)
#f.write(stringdata)
#f.close()

