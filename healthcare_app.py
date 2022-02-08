
import jsonify
import requests
import pickle
import numpy as np
import sys
import os
import re
import sklearn
from flask import Flask, render_template, url_for, flash, redirect, request, send_from_directory
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model_heartdisease = pickle.load(open('heartdisease.pkl', 'rb'))
model_liverdisease = pickle.load(open('liverdisease.pkl', 'rb'))

@app.route('/',methods=['GET'])
@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/heartdisease', methods=['GET','POST'])
def heartdisease():
    if request.method == 'POST':
        Age=int(request.form['age'])
        Gender=int(request.form['sex'])
        ChestPain= int(request.form['cp'])
        BloodPressure= int(request.form['trestbps'])
        ElectrocardiographicResults= int(request.form['restecg'])
        MaxHeartRate= int(request.form['thalach'])
        ExerciseInducedAngina= int(request.form['exang'])
        STdepression= float(request.form['oldpeak'])
        ExercisePeakSlope= int(request.form['slope'])
        MajorVesselsNo= int(request.form['ca'])
        Thalassemia=int(request.form['thal'])
        prediction=model_heartdisease.predict([[Age, Gender, ChestPain, BloodPressure, ElectrocardiographicResults, MaxHeartRate, ExerciseInducedAngina, STdepression, ExercisePeakSlope, MajorVesselsNo, Thalassemia]])
        if prediction==1:
            return render_template('heartdisease_prediction.html', prediction_text="Oops! You seem to have a Heart Disease.", title='Heart Disease')
        else:
            return render_template('heartdisease_prediction.html', prediction_text="Great! You don't have any Heart Disease.", title='Heart Disease')
    else:
        return render_template('heartdisease.html', title='Heart Disease')

    
@app.route('/liverdisease', methods=['GET','POST'])
def liverdisease():
    if request.method == 'POST':
        Age=int(request.form['Age'])
        Gender=int(request.form['Gender'])
        Total_Bilirubin= float(request.form['Total_Bilirubin'])
        Direct_Bilirubin= float(request.form['Direct_Bilirubin'])
        Alkaline_Phosphotase= int(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase= int(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase= int(request.form['Aspartate_Aminotransferase'])
        Total_Protiens= float(request.form['Total_Protiens'])
        Albumin= float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio= float(request.form['Albumin_and_Globulin_Ratio'])
        prediction=model_liverdisease.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
        if prediction==1:
            return render_template('liverdisease_prediction.html', prediction_text="Oops! You seem to have Liver Disease.", title='Liver Disease')
        else:
            return render_template('liverdisease_prediction.html', prediction_text="Great! You don't have any Liver Disease.", title='Liver Disease')
    else:
        return render_template('liverdisease.html', title='Liver Disease')

if __name__=='__main__':
	app.run(debug=True)
