import numpy as np
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv 
load_dotenv()

def get_key(key_name):
    """returns the value of the key"""
    key_value = os.getenv(key_name)
    return key_value

def do_nothing_yet():
    """we demo 'pass' """
    pass
  
def get_darksky_daily_weather(url):
    daily_weather = requests.get(url).json()
    daily_weather_json = json.dumps(daily_weather, indent = 4, sort_keys=True)
    return daily_weather ,daily_weather_json

def get_darksky_url(DARKSKY_API_KEY ,latitude ,longitude ,YYYYMMDD ,TimeOffset):
    url = f"https://api.darksky.net/forecast/{DARKSKY_API_KEY}/{latitude},{longitude},{YYYYMMDD}T{TimeOffset}?exclude=currently,flags"
    return url

def main(mydictionary):  # "**kwargs" 
    """"we demo a variety of functions """
    if "DARKSKY_API_KEY" in mydictionary:
        url = get_darksky_url(mydictionary["DARKSKY_API_KEY"] ,mydictionary["latitude"] ,mydictionary["longitude"] ,mydictionary["YYYYMMDD"] ,mydictionary["TimeOffset"])
        daily_weather ,daily_weather_json = get_darksky_daily_weather(url)
        print(type(daily_weather))
        print(daily_weather_json)

    if "Amex_CSV" in mydictionary:
        return "Amex_CSV string"

    return 0

if __name__ == "__main__":
    main({"DARKSKY_API_KEY":get_key("DARKSKY_API_KEY") ,"latitude":"38.178164" ,"longitude":"-85.793976" ,"YYYYMMDD":"2002-02-20" ,"TimeOffset":"11:00:00-0400"})
