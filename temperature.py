import requests
import json
import streamlit as st
import pandas as pd


# Make a GET request to the OpenWeatherMap API
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')

# Save the JSON response to a file
with open('weather.json', 'w') as file:
    output_json = json.dumps(result.json(),indent=4,sort_keys=True)
    file.write(output_json)

with open('weather.json', 'r') as file:
    result_dict = json.load(file)
    

# Create a temperature dictionary to store the temperature data
temperature_dict = []
    

for i in result_dict['temperature']['data']:
    # add location
    temperature_dict.append({'place': i['place'], 'value': i['value']})


# Streamlit app
st.set_page_config(layout="wide")

# Layout with two columns
col1, col2 = st.columns(2)

# Left column: Selectbox for selecting the locaion
with col1:
    selected_place = st.selectbox('Select a location', [entry['place'] for entry in temperature_dict])

# Right column: Display the weather data
with col2:
    st.markdown("**Hong Kong Weather Data**")
    st.write(f"Location: {selected_place}")
    st.markdown('<p style="opactiy:0.5;">Temperature(°C)</p>', unsafe_allow_html=True)

    # Find the temperature for the selected location
    selected_temp = next(item['value'] for item in temperature_dict if item['place'] == selected_place)
    st.markdown(f"<h1 style='text-align: center; color: #ff6347;'>{selected_temp}°C</h1>", unsafe_allow_html=True)

    # Bar chart of all temperatures
    df = pd.DataFrame({
        'Location': [entry['place'] for entry in temperature_dict],
        'Temperature': [entry['value'] for entry in temperature_dict]
    })
    st.bar_chart(df.set_index('Location'))
