# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 21:22:25 2023

@author: Sathiya A K
"""

import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open(r'C:\Users\Sathiya A K\Downloads\ML\insurance_model.sav',"rb"))


def insurance_prediction(input_data):
    x_data=np.asarray(input_data)
    x_data=x_data.reshape(1,-1)
    prediction=loaded_model.predict(x_data)
    #print(prediction[0])
    return prediction
    
    
    
    
def main():
    st.title("WANT TO KNOW YOUR INSURANCE AMOUNT?")
    st.image("https://cdn-ccofj.nitrocdn.com/egjTjcapaIUryXYtMcEvzZpvESYVtgkq/assets/static/optimized/rev-749623b/images/2020/07/17-01.jpg")
    st.header("ENTER THE DETAILS:")
    age=st.slider("Choose your Age",0,130,25)
    gender=st.selectbox("Choose your gender",['male','female'])
    if gender=='male':
        new_gender=0
    else:
        new_gender=1
    
    bmi=st.text_input("Enter the bmi")
    children=st.text_input("Enter the number of children")
    smoker=st.selectbox("Enter the smoking status",['smoker','non-smoker'])
    if smoker=='smoker':
        new_smoker=1
    else:
        new_smoker=0
    region=st.selectbox("Choose your region",['Southeast','Southwest','Northeast','Northwest'])
    if region=='North':
        new_region=0
    elif region=='South':
        new_region=1
    elif region=='West':
        new_region=2
    else:
        new_region=3
    pred=""
    if st.button("CHECK"):
     pred= insurance_prediction([age,new_gender,bmi,children,new_smoker,new_region])
     st.success(f'Your predicted medical insurance cost is $.{pred[0]:.2f} USD ')
     
     
     
     
if __name__=='__main__':
    main()
    

    
    