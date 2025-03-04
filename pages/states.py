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

#scatterplot
fig = px.pie(df, x="latitude", title="Pointing Weather data")
st.plotly_chart(fig)

#boxplot
fig = px.box(df, x="country_code", y="name", title="Weather category by country Code")
st.plotly_chart(fig)

#striplot
fig = px.strip(df, x="state_code", y="longitude", title="Visualing Distribution of Weather Data")
st.plotly_chart(fig)

#violin plot
fig = px.line(df, x="country_code", y="state_code", title="Weather data by Country Code")
st.plotly_chart(fig)

#swarmplot
fig = px.choropleth(df, geojson="country_name", locations="country_id", title="Weather data by Country Code")
st.plotly_chart(fig)






