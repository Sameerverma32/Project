import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt


#st.markdown('''Weather Data💧 🌊💦Understanding and Utilizing Weather Data💧 🌊💦''')

st.markdown('<h1 style="color: black; font-size: bold; text-align: center; background-color:grey; margin:20px: border: 2px dashed yellow; font-family:sans serif">Weather EDA With Python<h1>', unsafe_allow_html=True)

image_url = "https://image.shutterstock.com/z/stock-vector-set-weather-icons-all-icons-for-weather-with-sample-of-use-for-print-web-or-mobile-app-vector-1430484773.jpg"

st.markdown(f"<div style=''text-align:center;'><img src='{image_url}'></div>", unsafe_allow_html=True)