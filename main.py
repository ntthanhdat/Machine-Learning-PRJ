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
        return render_template("index.html", price=round(price,2), bed=bed, bath=bath,floor=floor,sqm=sqm,lot=lot,con=con,grade=grade,year=year)
    else:
        return render_template("index.html")

if __name__ == '__main__':

    app.run()