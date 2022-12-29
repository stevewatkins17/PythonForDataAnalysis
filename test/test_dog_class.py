from ..src import dog_class as d
import pytest

@pytest.fixture
def get_biscuit():
    biscuit = d.Dog("Biscuit" ,14)
    return biscuit

def test_name(get_biscuit):
    assert get_biscuit.name == "Biscuit"

def test_age(get_biscuit):
    assert get_biscuit.age == 14

def test_Dog():
    biscuito = d.Dog("Biscuito" ,2)
    assert biscuito.name == "Biscuito" 
    assert biscuito.age == 2 

def test_age2(get_biscuit):
    biscuito = d.Dog("Biscuito" ,2)
    biscuito.age = 5
    assert biscuito.age != 2 
    assert get_biscuit.age == 14 
