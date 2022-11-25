#from PythonForDataAnalysis.src.hide_secrets import *
from .. src import hide_secrets

def test_get_key_env():
    key_value = hide_secrets.get_key_env("DARKSKY_API_KEY")
    assert key_value[4] == "f"
    assert len(key_value) == 32

def test_get_local_env_key():
    key_value = hide_secrets.get_local_env_key("myfakePW" ,"src/.env_demo")
    assert key_value == "jdkaslfgha;sdkhjfskj"
