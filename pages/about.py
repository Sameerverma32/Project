import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt




st.markdown('''The weather dataset is a time-series data set with per hour information about the weather conditions at a particular locaton. It records the following information

Temperature: The measure of how hot or cold the atmosphere is at a specific time and location, typically recorded in degrees Celsius (°C).
Dew Point Temperature: The temperature at which air becomes saturated with moisture and dew forms, indicating the amount of moisture in the air.
Relative Humidity: The percentage of moisture in the air relative to the maximum amount of moisture the air can hold at that temperature, crucial for understanding precipitation likelihood.
Wind Speed: The speed at which air is moving horizontally through the atmosphere, measured in kilometers per hour (km/h)
Visibility: The distance one can clearly see, measured in kilometers (km) important for transportation safety.
Pressure: The force exerted by the weight of the air above a specific point, measured in kPa, indicating weather patterns.
Conditions: A qualitative description of the overall weather at a specific time, such as sunny, cloudy, or rainy, providing a quick summary of the weather.''')