import numpy as np #Data manipulation
import pandas  as pd #Data manipulation
dataset = pd.read_csv("argument.csv",  header=None, skiprows=[0])
w = np.array(dataset.values)
print(w)
w_0 = w[0][0]
w_1 = w[0][1]
w_2 = w[0][2]
w_3 = w[0][3]
w_4 = w[0][4]
y1 = w_0+ w_1*2+w_2*1+w_3*1+w_4*100
print( u'Du doan gia nha co dien tich 537 m2: %.2f (USD)' %(y1))
