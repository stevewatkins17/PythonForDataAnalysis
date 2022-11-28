from .. src import fileHandling as fh
from .. src import fn_demo as fd
import pytest
import requests ,os

@pytest.fixture
def get_dict_filename():
    mydict = dict({"mykey":"myvalue"})
    myfilepathname = os.getcwd() + f"/imported_projects/myfile.json"
    #return mydict ,myfilepathname
    yield mydict ,myfilepathname
    fh.DeleteFile(myfilepathname)

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

def test_create_json_from_dict(get_dict_filename):
    import collections.abc
    returncode = fd.create_json_from_dict(get_dict_filename[0] ,get_dict_filename[1])
    print(type(get_dict_filename[0]))
    assert returncode == 0
    assert os.path.isfile(get_dict_filename[1]) == True

    """ we test that obj is dictionary """
    assert isinstance(get_dict_filename[0], dict) == True
    #assert True == False

