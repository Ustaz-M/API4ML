# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 18:15:48 2024

@author: User
"""

 

import pickle 
import json 
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input (BaseModel):
    
    
    age      :  int
    sex      :  int  
    cp       :  int
    trestbps :  int
    chol     :  int  
    fbs      :  int  
    restecg  :  int  
    thalach  :  int
    exang    :  int
    oldpeak  :  float
    slope    :  int  
    ca       :  int  
    thal     :  int 
    
    
    
#Loading saved model 
heart_model = pickle.load ( open ('trained_heart.pxl', 'rb'))

#creating api 
@app.post('/heart_prediction')

def heart_prediction (input_parameters : model_input ):
    input_data = input_parameters.json ()
    input_dict = json.loads (input_data)
    
    ag = input_dict ['age']
    se = input_dict ['sex']
    cep = input_dict ['cp']
    tres = input_dict ['trestbps']
    ch = input_dict ['chol']
    fb = input_dict ['fbs']
    re = input_dict ['restecg']
    th = input_dict ['thalach']
    ex = input_dict ['exang']
    ol = input_dict ['oldpeak']
    sl = input_dict ['slope']
    cab = input_dict ['ca']
    th = input_dict ['thal']
    
  
    
    input_list= [ ag , se , cep , tres , ch , fb , re ,th , ex,  ol , sl ,cab , th ]
    
    prediction = heart_model.predict([input_list])
    
    if (prediction[0]==0):
       return('The loan is not approved')
    else:
       return('The loan is approved')
    
  
  
  
  