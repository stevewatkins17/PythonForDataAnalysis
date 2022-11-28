from .. src import fileHandling as fh
from .. src import fn_demo as fd
import pytest
import requests ,os ,collections.abc as ca

@pytest.fixture
def get_dict_filename():
    mydict = dict({"mykey":"myvalue"})
    myfilepathname = os.getcwd() + f"/imported_projects/myfile.json"
    #return mydict ,myfilepathname
    yield mydict ,myfilepathname
    fh.DeleteFile(myfilepathname)

@pytest.fixture
def create_json_from_dict(get_dict_filename):
    returncode = fd.create_json_from_dict(get_dict_filename[0] ,get_dict_filename[1])
    return returncode

@pytest.fixture
def get_darksky_key():
    key_name = "DARKSKY_API_KEY"
    darksky_key = fd.get_key_env(key_name)
    return darksky_key

@pytest.fixture
def get_darksky_url(get_darksky_key):
    latitude ,longitude = "38.178164" ,"-85.793976" 
    YYYYMMDD = "2002-02-20"
    TimeOffset = "11:00:00-0400"
    """ return darksky formatted url string """
    url = fd.get_darksky_url(get_darksky_key ,"38.178164" ,"-85.793976" ,"2002-02-20" ,"11:00:00-0400")
    return url

@pytest.fixture
def get_darksky_result(get_darksky_key):
    darksky_result = None
    if get_darksky_url != None:
        darksky_result = requests.get(get_darksky_url).json()
    return darksky_result

def test_get_key_env(get_darksky_key):
    """since our key is private and only locally stored, we make the test conditional
    """
    if get_darksky_key != None:
        assert len(get_darksky_key) == 32
        assert get_darksky_key[0:4] == "3913"

def test_get_darksky_url(get_darksky_url):
    """since our key is private and only locally stored, we make the test conditional
    """
    print(get_darksky_url[0:23])
    if get_darksky_url != None:
        assert get_darksky_url[0:23] == "https://api.darksky.net"

def test_create_json_from_dict(get_dict_filename ,create_json_from_dict):
    assert create_json_from_dict == 0
    assert os.path.isfile(get_dict_filename[1]) == True

    """ we test that obj is dictionary """
    assert isinstance(get_dict_filename[0], dict) == True
    #assert True == False

def test_convert_json_to_dict(get_dict_filename ,create_json_from_dict):
    """Parse a json file and convert to dictionary object"""
    if create_json_from_dict == 0:
        my_new_dict = fd.convert_json_to_dict(get_dict_filename[1])
        print(get_dict_filename[1])
        print(my_new_dict)
        
        assert os.path.isfile(get_dict_filename[1]) == True
        assert isinstance(my_new_dict, dict) == True
        assert my_new_dict["mykey"] == "myvalue"
        #assert 1 == 0
    
def test_do_nothing_yet():
    returncode = fd.do_nothing_yet()
    assert returncode == None

def test_get_darksky_daily_weather(get_darksky_url):
    """ return weather data as dict and formatted string """
    daily_weather ,daily_weather_json = fd.get_darksky_daily_weather(get_darksky_url)
    #print(type(daily_weather))   
    print(daily_weather_json)
    assert daily_weather["timezone"] == "America/Kentucky/Louisville"
    #assert 1 == 0

def test_main():
    returncode = fd.main()
    assert returncode == 0