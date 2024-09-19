import requests
import json


# Make a GET request to the OpenWeatherMap API
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')

# Save the JSON response to a file
with open('weather.json', 'w') as file:
    output_json = json.dumps(result.json(),indent=4,sort_keys=True)
    file.write(output_json)

with open('weather.json', 'r') as file:
    result_dict = json.load(file)
    

for i in result_dict['temperature']['data']:
    print('location: ',i['place'])
    print('temperature: ',i['value'])