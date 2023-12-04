import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np
from sklearn.naive_bayes import GaussianNB
movie_dict = pickle.load(open('NBClassifier.pkl', 'rb'))
# movies = pd.DataFrame(movie_dict)
st.title("Crop Recommender")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
def recommend(a,b,c,d,e,f,g):
    data = np.array([[a,b,c,d,e,f,g]])
    prediction = movie_dict.predict(data)
    return prediction
a=st.number_input('Enter Nitrogen')
b=st.number_input('Enter Phosphorus')
c=st.number_input('Enter Pottasium')
d=st.number_input('Enter Temperature')
e=st.number_input('Enter Humidity')
f=st.number_input('Enter Ph')
g=st.number_input('Enter Rainfall')

if st.button('Recommend'):
    p=recommend(a,b,c,d,e,f,g)
    st.text(p[0])