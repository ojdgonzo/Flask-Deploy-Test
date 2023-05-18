# Importing the proper flask libraries
from flask import Flask, render_template, request

# importing pickle
import pickle

# Creating our flask project
app = Flask(__name__)
app.secret_key = '9sda01133na-djm1'

# homepage
@app.route('/')
def index():
    return render_template('submission.html')

# prediction page
# it will take in any numerical value to see what the possible revenue value
# using pickle to "unpickle" our file and pull our linear regression prediction 
@app.route('/prediction', methods = ['POST', 'GET'])
def prediction():
    bigbudget = float(request.form['BigBudget'])
    unpickled = pickle.load(open('linearModel.pkl', 'rb'))
    prediction = unpickled.predict([[bigbudget]])
    # print(prediction)
    return render_template('prediction.html', prediction = prediction[0][0].round(2))

# running our project
if __name__ == '__main__':
    app.run(debug = True)
