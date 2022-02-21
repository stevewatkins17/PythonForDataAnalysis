import numpy as np
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv 
load_dotenv()

def get_key_env(key_name):
    """returns the value of the key - from OS env file """
    key_value = os.getenv(key_name)
    return key_value

def get_local_env_key(key_name ,myfilepathname):
    """returns the value of the key - from local project file """
    # we connect tp .env file, iterate the lines till we get to key_name
    try:
        with open(myfilepathname, "r") as read_file:
            env_vars =  dict(json.load(read_file))
        key_value = env_vars[key_name]                            
    except:
        key_value = None
 
    return key_value

def create_json_from_dict(mydict ,myfilepathname):
    """ writes a dictionary object to local project as a json file """
    try:
        with open(myfilepathname, "w+") as fileToSave:
            json.dump(mydict, fileToSave, ensure_ascii=True, indent=4, sort_keys=False)
            return 0
    except:
        return 1

def convert_json_to_dict(myfilepathname):
    """Parse a json file and convert to dictionary object"""  
    try:
        with open(myfilepathname, "r") as read_file:
            my_new_dict =  dict(json.load(read_file))            
    except:
        my_new_dict = {}
    return my_new_dict

def do_nothing_yet():
    """we demo 'pass' """
    pass
  
def get_darksky_daily_weather(url):
    """ return weather data as dict and formatted string """
    daily_weather = requests.get(url).json()
    daily_weather_json = json.dumps(daily_weather, indent = 4, sort_keys=True)
    return daily_weather ,daily_weather_json

def get_darksky_url(DARKSKY_API_KEY ,latitude ,longitude ,YYYYMMDD ,TimeOffset):
    """ return darksky formatted url string """
    url = f"https://api.darksky.net/forecast/{DARKSKY_API_KEY}/{latitude},{longitude},{YYYYMMDD}T{TimeOffset}?exclude=currently,flags"
    return url

def main(mydictionary):  # same as "import_type ,**kwargs" 
    """we demo a variety of data import functions """
    if mydictionary["import_type"] == "weather_on_date":
        url = get_darksky_url(mydictionary["DARKSKY_API_KEY"] ,mydictionary["latitude"] ,mydictionary["longitude"] ,mydictionary["YYYYMMDD"] ,mydictionary["TimeOffset"])
    
        daily_weather ,daily_weather_json = get_darksky_daily_weather(url)
        print(type(daily_weather))
        #next: FN to persist json to file system
        print(daily_weather_json)
        create_json_from_dict(daily_weather ,"Data/daily_weather.json")
 
    # you can also derive the import_type with a key or value existence chk, but that is error-prone and generally a bad practice
    if "Amex_CSV" in mydictionary:
        pass

    return 0

if __name__ == "__main__":
    #DARKSKY_API_KEY = get_key_env("DARKSKY_API_KEY") #requires root user
    DARKSKY_API_KEY = get_local_env_key("DARKSKY_API_KEY" ,".env")
    mydictionary = {"import_type":"weather_on_date" ,"DARKSKY_API_KEY":DARKSKY_API_KEY ,"latitude":"38.178164" ,"longitude":"-85.793976" ,"YYYYMMDD":"2002-02-20" ,"TimeOffset":"11:00:00-0400"}
    main(mydictionary)
