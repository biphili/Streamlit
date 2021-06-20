# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:35:59 2021

@author: Binu
"""
import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#from plotly import graph_objs as go

data = pd.read_csv("Salary_Data.csv")
x= np.array(data['YearsExperience']).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data['Salary']))

st.title("Salary Prediction")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])
if nav == "Home":
    st.image("salary.jpg",width=300)
    if st.checkbox("Show Table"):
        st.table(data)
        
        
    graph = st.selectbox("What kind of Graph ?",["Non-Interactive","Ineractive"])
    
    val =st.slider("Filter data using years",0,20)
    data= data.loc[data["YearsExperience"]>=val     ]
    if graph =="Non-Interactive":
        st.set_option('deprecation.showPyplotGlobalUse',False)
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()
        
    

if nav == "Prediction":
    st.header("Know your Salary")
    val = st.number_input("Enter your experience",0.00,20.00,step=0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]
    
    if st.button("Predict"):
        st.success(f"Your predicted salary is{round(pred)}")
        
        
if nav == "Contribute":
    st.header("Contribute to our Dataset")
    ex = st.number_input("Enter your Experience",0.0,20.0)
    sal = st.number_input("Enter your Salary",0.00,1000000.00,step=1000.0)
    if st.button("submit"):
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("Salary_Data.csv",mode='a',header=False,index=False)
        st.success("Submitted")
    
    
    
    
    
