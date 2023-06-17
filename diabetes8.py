import json
import streamlit as st
import numpy as np
import requests
import pandas as pd
import warnings
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings('ignore')

#get input data from streamlit:
Age =st.sidebar.slider('choose you age group: 0=1-24 or younger, 2=25-29, 3=30-34, 4=35-39, 5=40-44, 6=45-49, 7=50-54, 8=55-59, 9=60-64, 10=65-69, 11=70-74, 12=75-79, 13=80 or order', 1, 13, 1)
Sex =st.sidebar.slider('Are you a male,0=female,1=male', 0, 1, 0)
HighChol =st.sidebar.slider("have you had HighChol? 0=No, 1=high", 0, 1, 0)
CholCheck =st.sidebar.slider("Have you checked Chol in 5 years? 0=No, 1=yes", 0, 1,0)
BMI = st.sidebar.slider('What your Body Mass Index', 1, 100, 1)
Smoke =st.sidebar.slider("Have you smoked at lease 100 sigarettes in your entire life? 0=No, 1=yes", 0, 1,0)
HeartDiseaseorAttack =st.sidebar.slider('Have had a HeartDiseaseorAttack? 0=No, 1=yes', 0, 1, 0)
PhysActivity = st.sidebar.slider("Have you illness or injury in past 30 days?, 0=No, 1=yes", 0, 1, 0)
Fruits =st.sidebar.slider("Have you had consume fruit 1 or more time per day?, 0=No, 1=yes", 0,1, 0)
Veggies =st.sidebar.slider( "Have you eat 1 or more per day? 0=No, 1=yes", 0,1, 0)
HvyAlcoholConsump= st.sidebar.slider("adult men>= 14 drink/weeks, women>= 7 drink per day, 0=No, 1=yes", 0, 1, 0)
GenHlth= st.sidebar.slider("Genhlth scale, 1=excellent, 2=very good, 3=good, 4=fair, 5=poor", 1, 5, 1)
MentHlth=st.sidebar.slider("how many days in past 30 days of poor health scale 1-30 days", 0, 30, 0)
PhysHlth=st.sidebar.slider("have you had physhlth inpast 30 days, not including job", 0, 30, 0)
DiffWalk =st.sidebar.slider("have you had difficulty walk or climbing stairs? 0=No, 1=yes", 0, 1, 0)
Stroke =st.sidebar.slider(" Have you had smoke? 0=No, 1=yes", 0, 1, 0)
HighBP =st.sidebar.slider("Have had a High BP? 0=No highBP, 1=highBP", 0, 1, 0)

# conbine input to dictionary
data={'Age':Age,
      'Sex':Sex,
      'HighChol':HighChol,
      'CholCheck':CholCheck,
      'BMI':BMI,
      'Smoke':Smoke,
      'HeartDiseaseorAttack':HeartDiseaseorAttack,
      'PhysActivity':PhysActivity,
      'Fruits':Fruits,
      'Veggies':Veggies,
      'HvyAlcoholConsump':HvyAlcoholConsump,
      'GenHlth':GenHlth,
      'MentHlth':MentHlth,
      'PhysHlth':PhysHlth,
      'DiffWalk':DiffWalk,
      'Stroke':Stroke,
      'HighBP':HighBP,
      }

#create json data from dictionary
datajson =json.dumps(data)

# make prediction by requesting to the API
pred =requests.post(url= "http://127.0.0.1:8000/prediction",json=data)

#display prediction
image = Image.open("C:\\Users\\maxin\\DTSC691\\rnd_model_Feature_Importances_1.png")
st.image(image, use_column_width=True)
          
# page title
st.title('Model prediction for Diabetes')
st.markdown('Please fill out this form')
st.button('Please fill out this form')
 
if st.button('prediction'):
  st.subheader(f"Based on provided data, you are")
  result =' '
  if pred ==0:
    result = ({'healthy'})
  else:
    result = ({"not healthy"})
  st.write(result)   
    
if st.checkbox("show details"):
  st.write("The data retreived from streamlit frontend:", 'the user input is converted into a json object and sent to the endpoint of the API') 
  st.write(data)
  
  
