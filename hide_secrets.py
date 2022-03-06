import json
import os
from dotenv import load_dotenv 
#load_dotenv("/etc/environment") # uses linux environment file
load_dotenv() # uses local .env

def get_key_env(key_name):
    """returns the value of the key - from OS env file -- BEST PRACTICE METHOD """
    key_value = os.getenv(key_name)
    return key_value

def get_local_env_key(key_name ,myfilepathname):
    """returns the value of the key - from local project file --  NOT a best practice """
    # we connect tp .env file, iterate the lines till we get to key_name
    with open(myfilepathname, "r") as read_file:
        env_vars =  dict(json.load(read_file))
    key_value = env_vars[key_name]                            
    return key_value

def main():
    """we demo how to use a secret value and keep it from being pushed to github/origin"""
    
    MY_SECRET_API_KEY = get_local_env_key("MY_SECRET_API_KEY" ,".env_demo")
    print(f"MY_SECRET_API_KEY = {MY_SECRET_API_KEY}")

    DARKSKY_API_KEY = get_key_env("DARKSKY_API_KEY")
    DARKSKY_API_KEY_demo = DARKSKY_API_KEY.replace(DARKSKY_API_KEY[0:9], "**********", 1)
    print("BEST Practice using OS 'environment' variable")
    print(f"DARKSKY_API_KEY = {DARKSKY_API_KEY_demo}")

if __name__ == "__main__":
    main()