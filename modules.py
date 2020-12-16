#Define the modules
from datetime import date
import requests
import json
import math

weather_api_url = "http://api.openweathermap.org/data/2.5/"
api_key = "bc28e60abe708474d1372b006e323ed6"

def home():
    home = {
        "Message":"My Weather App",
        "Author": "Sanje Divakaran",
        "Date": date.today()
    }
    return home

def todays_weather(city):
    weather_api = weather_api_url + "forecast?q=" + city + "&APPID=" + api_key
    
    resp = requests.get(weather_api)
    resp_content = json.loads(resp.content)
    #print(resp_content)
    weather_resp = {
        "city": {
            "name": resp_content["city"]["name"],
            "country": resp_content["city"]["country"]
        }
    }
    weather_data = resp_content["list"]
    weather_day = []
    i = 0
    for data in weather_data:
        #print(data)
        #print("----------------")
        jday = {
            'date':data['dt_txt'],
            'temp':round(data['main']['temp'] - 273.15, 2),
            'feels_like':round(data['main']['feels_like'] - 273.15, 2),
            'temp_min':round(data['main']['temp_min'] - 273.15, 2),
            'temp_max':round(data['main']['temp_max'] - 273.15, 2),
            'description':data['weather'][0]['description'],
            'icon':data['weather'][0]['icon']
        }
        weather_day.append(jday)
        i = i + 1
        if (i == 5):
            break
    
    weather_resp['data'] = weather_day
    print(weather_resp)
    #print(weather_data)
    if resp.status_code != 200:
        return {"error": true, "message": "unable to access weather API"}
    else:
        return weather_resp

def todays_weather_raw(city):
    weather_api = weather_api_url + "forecast?q=" + city + "&APPID=" + api_key
    
    resp = requests.get(weather_api)
    resp_content = json.loads(resp.content)

    return resp_content

