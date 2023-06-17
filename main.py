import uvicorn
import sys
import joblib
from fastapi import FastAPI
from pydantic import BaseModel 
from fastapi import Query
import numpy as np
from fastapi import FastAPI, Request, status

class diabetes(BaseModel):
  Age: int
  Sex: int
  HighChol:int
  CholCheck:int
  BMI:int
  Smoke:int
  HeartDiseaseorAttack:int
  PhysActivity:int
  Fruits:int
  Veggies:int
  HvyAlcoholConsump:int
  GenHlth:int
  MentHlth:int
  PhysHlth:int
  DiffWalk:int
  Stroke:int
  HighBP:int
  
main =FastAPI()
with open('C:\\Users\\maxin\\DTSC691\\rnd_model.joblib', "rb") as f:
  model=joblib.load(f)

@main.get("/")
def index():
   return{"message": "This is my home page of the API. "}

@main.post("/prediction")
def get_response(data:diabetes): 
    received =data.dict()
    a = received['Age']
    b = received['Sex']
    c = received['HighChol']
    d = received['CholCheck']
    e = received['BMI']
    f = received['Smoke']
    g = received['HeartDiseaseorAttack']
    h = received['PhysActivity']
    i = received['Fruits']
    j = received['Veggies']
    k = received['HvyAlcoholConsump']
    l = received['GenHlth']
    m = received['MentHlth']
    n = received['PhysHlth']
    o = received['DiffWalk']
    p = received['Stroke']
    q = received['HighBP']
    
#making a prediction system
    pred = model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q]]).tolist()[0]
    if pred ==0:
      result = "your are health"
    else:
      result = "your are no health"
    
    return {"prediction": pred}

if'__name__'== "__main__":
  uvicorn(main, host='127.0.0.1', part=8000, debug=True)
