from flask import Flask, url_for, render_template, request, redirect, session
from markupsafe import escape
from jinja2 import Template
from datetime import timedelta
import pandas  as pd #Data manipulation
import numpy as np #Data manipulation
import matplotlib.pyplot as plt # Visualization
import os
import csv
from sklearn import linear_model
app = Flask(__name__)



@app.route('/', methods=["POST", "GET"])
def home():
    if request.method=="POST":
        bed=int(request.form['bed'])
        bath=int(request.form['bath'])
        floor=int(request.form['floor'])
        sqm=int(request.form['sqm'])

        lot=int(request.form['lot'])
        con=int(request.form['con'])
        grade=int(request.form['grade'])
        year=int(request.form['year'])

        dataset = pd.read_csv("argument.csv",  header=None, skiprows=[0])
        w = np.array(dataset.values)
        price= w[0][0]*bed+ w[0][1]*bath+w[0][2]*sqm+w[0][3]*lot+w[0][4]*floor+w[0][5]*con+w[0][6]*grade+w[0][7]*sqm*1.1+w[0][8]*0+w[0][9]*year+w[0][10]*sqm*1.2+w[0][11]*lot*0.9+ w[0][12]
        return render_template("index.html", price=round(price,2))
    else:
        return render_template("index.html")

if __name__ == '__main__':
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


    app.run()