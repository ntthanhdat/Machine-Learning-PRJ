import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import matplotlib.pyplot as plt # Visualization
import os
import csv



path = 'house_Datasets.csv'
dataset = pd.read_csv(path)
#print('\nNumber of rows and columns in the data set: ',dataset.shape)
#print('')
Y = dataset[['price']]

X = dataset.drop(['price', 'id', 'year'],  axis=1)

X.info()
#print(X)
x = np.array(X.values)
y = np.array(Y.values)
#print(type(x))
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
w_0 = w[0][0]
w_1 = w[1][0]
w_2 = w[2][0]
w_3 = w[3][0]
w_4 = abs(w[4][0])
#print('tham so ham mat mat w = ', w)
#print to argument file
if os.path.exists("argument.csv"):
  os.remove("argument.csv")
#f = open("argument.csv", "a")

#stringdata=str(w_0)+","+str(w_1)+","+str(w_2)+","+str(w_3)+","+str(w_4)
dataInt=pd.DataFrame([[w_0, w_1, w_2, w_3, w_4]], columns=['w_0','w_1','w_2','w_3','w_4'])
dataInt.to_csv("argument.csv", index=False)
#f.write(stringdata)
#f.close()

