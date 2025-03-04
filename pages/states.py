import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt


df = pd.read_csv("states.csv")



st.dataframe(df)

states = df["name"]

st.sidebar.header("Filter options")

#create a histogram for Weather distrinution
fig = px.histogram(df, x='country_id', title="Weather Distribution", nbins=20)
st.plotly_chart(fig)

#pie chart
fig = px.pie(df, names="country_name",title="Weather Report by Country Name")
st.plotly_chart(fig)

#bar graph
fig = px.bar(df, x="country_id", y="country_name", title="Weather Distribution Category")
st.plotly_chart(fig)

#line plot
fig = px.line(df, x='country_id', y='id', title="Weather Distribution with Country id and id")
st.plotly_chart(fig)

#Pie plot
fig = px.pie(df, names="latitude", title="Pointing Weather data")
st.plotly_chart(fig)

#box plot
fig = px.box(df, x="country_code", y="name", title="Weather category by country Code")
st.plotly_chart(fig)

#Box lot
fig = px.box(df, x="state_code", y="longitude", title="Visualing Distribution of Weather Data")
st.plotly_chart(fig)

#Line plot
fig = px.histogram(df, x="country_code", nbins=20, title="Weather data by Country Code")
st.plotly_chart(fig)

#Line plot
fig = px.line(df, x="country_name", y="latitude", title="Weather data by Country Code")
st.plotly_chart(fig)






