from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

# Import required libraries 
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# importing pickle
import pickle


app = Flask(__name__)
app.secret_key = '9sda01133na-djm1'

@app.route('/')
def index():
    return render_template('submission.html')


@app.route('/prediction', methods = ['POST', 'GET'])
def prediction():
    bigbudget = float(request.form['BigBudget'])
    unpickled = pickle.load(open('linearModel.pkl', 'rb'))
    prediction = unpickled.predict([[bigbudget]])
    # print(prediction)
    return render_template('prediction.html', prediction = prediction[0][0].round(2))

if __name__ == '__main__':
    app.run(debug = True)
