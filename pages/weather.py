import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("weatherdata.csv")

st.dataframe(df)

#class filter
Temp=st.sidebar._multiselect('Temp',
                               options=sorted(df["Weather"].unique()),
                               default=sorted(df['Weather'].unique()))

fig = px.bar(df, x= 'Date/Time', y= 'Temp_C', title="Temperature Distribution by Month")
st.plotly_chart(fig)

fig = px.bar(df, x = 'Wind Speed_km/h', y = 'Weather', title="Relationship between Weather and Windspeed")
st.plotly_chart(fig)

fig = px.histogram(df, x="Dew Point Temp_C", y='Temp_C', title='Weather distribution', nbins=20)
st.plotly_chart(fig)

fig = px.pie(df, names="Weather", title="Weather EDA Distribution")
st.plotly_chart(fig)

fig = px.bar(df, x="Weather", y="Temp_C", title="Frequency of Different Weather Conditions by Season")
st.plotly_chart(fig)