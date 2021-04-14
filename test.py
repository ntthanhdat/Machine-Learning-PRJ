import numpy as np #Data manipulation
import pandas  as pd #Data manipulation

dataset = pd.read_csv("argument.csv",  header=None, skiprows=[0])
w = np.array(dataset.values)
print(w)
price= w[0][0]*2+ w[0][1]*1+w[0][2]*181+w[0][3]*5650+w[0][4]*floor+ w[0][12]
print( u'Du doan gia nha co dien tich 537 m2: %.2f (USD)' %(y1))
