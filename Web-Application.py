# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 10:29:53 2025

@author: Admin
"""

import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('C:/Users/Admin/Downloads/train_model.sav', 'rb')) 
def heart_prediction(input_data):
    input_data_as_numpy_arrays = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_arrays.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
        print("The person does not have a heart disease")
    else: 
        print("The person has a heeart disease")
def main():
    st.title('Heart Disease Prediction Web App')
    Age = st.text_input('Age of the person')
    Sex = st.text_input('Gender of the person')
    CP = st.text_input('Chest pain type') #Chest pain
    trestbps = st.text_input('Blood pressure') 
    chol = st.text_input('Cholestrol Level')
    fbs = st.text_input('fasting blood sugar')
    restecg = st.text_input('Resting Electrocardiographic Measure') 
    thalach = st.text_input('Max Heart Rate')
    exang = st.text_input('Exercise induced engine')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('calcium score')
    thal = st.text_input('Iran score')
    diagnosis = ''
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_prediction(Age, Sex, CP, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    st.success(diagnosis)
if __name__=='__main__':
    main() 
    