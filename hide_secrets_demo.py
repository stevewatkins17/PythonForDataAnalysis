import json

def get_local_env_key(key_name ,myfilepathname):
    """returns the value of the key - from local project file """
    # we connect tp .env file, iterate the lines till we get to key_name
    with open(myfilepathname, "r") as read_file:
        env_vars =  dict(json.load(read_file))
    key_value = env_vars[key_name]                            
    return key_value

def main():  # same as "import_type ,**kwargs" 
    """we demo a variety of data import functions """
    MY_SECRET_API_KEY = get_local_env_key("MY_SECRET_API_KEY" ,".env2")
    print(MY_SECRET_API_KEY)

if __name__ == "__main__":
    """we demo how to use a secret value and keep it from being pushed to github/origin"""
    main()