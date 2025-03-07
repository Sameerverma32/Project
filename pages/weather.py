import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("weatherdata.csv")
st.dataframe(df)

df.isnull().sum()

df.nunique()


df[['Date', 'Time']] = df['Date/Time'].str.split(' ', expand = True)

df['Date'] = pd.to_datetime(df['Date'])

# Getting seasons and seperating the month into a new column
def get_season(month):
    if month >=3 and month <= 5:
        return 'Spring'
    elif month>= 6 and month <= 8:
        return 'Summer'
    elif month >= 9 and month <= 11:
        return 'Autumn'
    else:
        return 'Winter'

df['Month'] = df['Date'].dt.month
df['Season'] = df['Month'].apply(get_season)

# Rearrange columns
df = df[['Date', 'Month', 'Time', 'Temp_C','Dew Point Temp_C','Rel Hum_%','Wind Speed_km/h','Visibility_km' ,'Press_kPa', 'Weather', 'Season']]
df = df.reset_index()

weather_count = len(df['Weather'].unique())

print('There are {} different weathers'.format(weather_count))

# Making the month their name value
import calendar

df['Month'] = df['Month'].apply(lambda x: calendar.month_name[x])

# Rearranging the columns
df = df[['Date', 'Month', 'Time', 'Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 
             'Visibility_km', 'Press_kPa', 'Weather', 'Season']]

# Replacing the column name weather with weather comdition
df.rename(columns = {'Weather': 'Weather Condition'}, inplace = True)

sf = df.head(2000)
sf
#class filter
# Temp=st.sidebar._multiselect('Temp',
weather_filter=st.sidebar.multiselect('Weather',
                               options=sorted(df["Weather Condition"].unique()),
                               default=sorted(df['Weather Condition'].unique()))

filtered_data = df[
    (df['Weather Condition'].isin(weather_filter))
]

fig = px.pie(filtered_data, names='Season', title="Season Distribution")
st.plotly_chart(fig)
st.markdown('''The goal is to visualize the distribution of different seasons in your weather dataset. A pie chart shows the proportion of each season within the data, which is useful to understand the frequency of each season's occurrence.
''')

fig = px.box(filtered_data, x='Temp_C', title='Temperature Distribution')
st.plotly_chart(fig)
st.markdown('''A Box Plot (also known as a Box-and-Whisker Plot) is a great way to visualize the distribution of a dataset. In the context of weather data, a box plot can help you understand the spread of temperature data, as well as identify outliers, the median, and the quartiles.''')

fig = px.bar(filtered_data, x= 'Month', y= 'Temp_C', title="Temperature Distribution by Month")
st.plotly_chart(fig)
st.markdown('''A Bar Chart is a great way to visualize and compare the temperature for each month in your dataset. You can use a bar chart to show the average temperature (or any other measure) for each month.''')

fig = px.bar(filtered_data, x='Weather Condition', y='Season', title='Frequency of Different Weather Conditions by Season')
st.plotly_chart(fig)
st.markdown('''Creating a Bar Chart for Weather Conditions by Season can help you visualize how often different weather conditions occur across various seasons (such as Winter, Spring, Summer, and Fall). This chart allows you to compare the frequency of different weather conditions (like sunny, rainy, cloudy, etc.) in each season.''')

fig = px.histogram(filtered_data, x="Dew Point Temp_C", y='Temp_C', title='Weather distribution', nbins=20)
st.plotly_chart(fig)
st.markdown('''A Histogram is a great way to visualize the distribution of a dataset and understand how the values are spread across different ranges. In your case, a histogram of the Dew Point Temperature (Temp_C) by Temperature can show the relationship between these two variables. Specifically, it will help you see how the dew point temperature changes as the regular temperature varies.''')

fig = px.bar(filtered_data, x = 'Wind Speed_km/h', y = 'Weather Condition',title=('Relationship between Weather Condition and Windspeed'))
st.plotly_chart(fig)
st.markdown('''Creating a Bar Chart for Wind Speed by Weather Condition allows you to visualize how the wind speed varies with different weather conditions (such as sunny, rainy, cloudy, etc.). This can provide insights into whether certain weather conditions are associated with higher or lower wind speeds.''')

