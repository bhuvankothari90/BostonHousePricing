# Creating this App to use it as Flask API and afterwards as web application

import pickle
import json
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

# Defining the Flask app and adding the code as a starting point
app=Flask(__name__)
model=pickle.load(open('regmodel.pkl','rb'))

# Load the model and Scaler
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

# Adding the below code to use the app further for the Web Application
@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text=f"The predicted House price is {output}")
# To run the app
if __name__=="__main__":
    app.run(debug=True)