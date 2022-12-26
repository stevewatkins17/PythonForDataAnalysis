# pytest test_retry_userinput_class.py
from .. src import retry_userinput_class as retry_ui
import pytest

@pytest.fixture
def get_retry_userinput_class():
    retry_count ,prompt = 3, "please pick a letter"
    myuserinput = retry_ui.UserInput(retry_count ,prompt)
    return myuserinput

@pytest.fixture
def get_retry_userinput_class_reassign(get_retry_userinput_class):
    myuserinput2 = get_retry_userinput_class
    myuserinput2.retry_count = -17
    myuserinput2.prompt = "DO NOT pick a letter"
    return myuserinput2

def test_retry_userinput_class(get_retry_userinput_class):
    """since our key is private and only locally stored, we make the test conditional
    """
    user_input = get_retry_userinput_class
    assert get_retry_userinput_class.retry_count == 3
    assert get_retry_userinput_class.prompt == "please pick a letter"

def test_retry_userinput_reassign_prompt(get_retry_userinput_class_reassign):
    myuserinput2 = get_retry_userinput_class_reassign
    assert myuserinput2.prompt == "DO NOT pick a letter"

def test_retry_userinput_reassign_count(get_retry_userinput_class_reassign):
    myuserinput2 = get_retry_userinput_class_reassign
    assert myuserinput2.retry_count == -17


