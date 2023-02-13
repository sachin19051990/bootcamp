import streamlit as st
import pickle
model = pickle.load(open('model.pkl', 'rb'))

def predict(sl,sw,pl,pw):
    prediction=model.predict([[sl,sw,pl,pw]])
    return prediction

def main():
    st.title("IRIS Prediction")
html_temp = """ <div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit IRIS Predictor </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
