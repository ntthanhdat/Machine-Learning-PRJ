from flask import Flask, url_for, render_template, request, redirect, session
from markupsafe import escape
from jinja2 import Template
from datetime import timedelta
import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import matplotlib.pyplot as plt # Visualization
import os
import csv

app = Flask(__name__)



@app.route('/', methods=["POST", "GET"])
def home():
    if request.method=="POST":
        bed=int(request.form['bed'])
        bath=int(request.form['bath'])
        floor=int(request.form['floor'])
        sqm=int(request.form['sqm'])
        dataset = pd.read_csv("argument.csv",  header=None, skiprows=[0])
        w = np.array(dataset.values)
        print(w)
        w_0 = w[0][0]
        w_1 = w[0][1]
        w_2 = w[0][2]
        w_3 = w[0][3]
        w_4 = w[0][4]
        price= w_1*bed + w_2*bath + w_3*floor+ w_4*sqm +w_0
        return render_template("index.html", price=price,bed=bed, bath=bath,floor=floor,sqm=sqm)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    path = 'dataset.csv'
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
    #print to argument file
    if os.path.exists("argument.csv"):
        os.remove("argument.csv")
    #f = open("argument.csv", "a")

    #stringdata=str(w_0)+","+str(w_1)+","+str(w_2)+","+str(w_3)+","+str(w_4)
    dataInt=pd.DataFrame([[w_0, w_1, w_2, w_3, w_4]], columns=['w_0','w_1','w_2','w_3','w_4'])
    dataInt.to_csv("argument.csv", index=False)
    #f.write(stringdata)
    #f.close()


    app.run()