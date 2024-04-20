import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

model = pickle.load(open('result_model.pkl', 'rb'))

app = Flask(__name__,template_folder='C:/Users/amrut/major/Real/template')

st.title('Home')
col1, col2, col3 = st.columns(3)
with col1:
    N = st.text_input('Enter Nitrogen')
        
with col2:
    P = st.text_input('Enter Phosphorous')
    
with col3:
    K = st.text_input('Enter Potassium')
        
with col1:
    Temp = st.text_input('Enter temperature')
        
with col2:
    pH = st.text_input('Enter pH')
    
with col3:
    Humidity = st.text_input('Enter Humidity')
        
with col1:
    Rainfall = st.text_input('Enter rainfall')
    

if st.button('Recommend'):
    crop_prediction = model.predict([[N,P,K,Temp,pH,Humidity,Rainfall]])

st.success(crop_prediction)
    
















