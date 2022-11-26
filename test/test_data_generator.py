import pytest
from .. src import data_generator as dg
from .. src import fileHandling as fh

myfile = "data/orders.csv"
mysecondfile = "data/orders2.csv"

@pytest.fixture
def test_data_generator_file_cleanup():
    try:
        fh.DeleteFile(myfile)
        fh.DeleteFile(mysecondfile)
        return 0
    except:
        print(f"file not exist: '{myfile}'")
        return 1
        
def test_main_dg(test_data_generator_file_cleanup):
    csv_create_result =  dg.main(myfile)
    assert csv_create_result == 0

def test_create_csv(test_data_generator_file_cleanup):
    myfile = mysecondfile
    linecount = 10
    list0 = ["red" ,"green" ,"blue" ,"magenta" ,"fuscia" ,"yellow"]
    list1= ["1","3","5","7","11","13","17","19","23","29","31","37","41","43","47"]
    list2= ["Bonjour" ,"Creatio ex nihilo" ,"hello squirrel"]
    myreturn = dg.create_csv(myfile ,linecount ,list0 ,list1 ,list2) 
    assert myreturn == 0

def test_cleanup(test_data_generator_file_cleanup):
    return 0
