from flask import Flask, url_for, render_template, request, redirect, session
from markupsafe import escape
from jinja2 import Template
from datetime import timedelta

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()