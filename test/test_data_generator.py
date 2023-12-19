import pytest
from .. src import data_generator as dg
from .. src import fileHandling as fh

@pytest.fixture
def myfiles():
    myfile = "data/orders.csv"
    mysecondfile = "data/orders2.csv"
    return myfile ,mysecondfile

@pytest.fixture
def delete_files(myfiles):
    result = 0
    for f in myfiles:
        try:
            fh.DeleteFile(f)
        except:
            print(f"file not exist: '{f}'")
            result = 1
    return result

def test_main_dg(myfiles ,delete_files):
    linecount = 17
    csv_create_result =  dg.main(myfiles[0] ,linecount)
    assert csv_create_result == 0

def test_create_csv(myfiles ,delete_files):
    mysecondfile = myfiles[1]
    linecount = 10
    list0 = ["red" ,"green" ,"blue" ,"magenta" ,"fuscia" ,"yellow"]
    list1= ["1","3","5","7","11","13","17","19","23","29","31","37","41","43","47"]
    list2= ["Bonjour" ,"Creatio ex nihilo" ,"hello squirrel"]
    myreturn = dg.create_csv(mysecondfile ,linecount ,list0 ,list1 ,list2) 
    assert myreturn == 0

def test_cleanup(delete_files):
    result = delete_files
    assert result == 0
