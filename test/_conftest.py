# conftest.py
# _conftest.py --> disabled
import pytest
from .. src import fileHandling as fh

@pytest.fixture(scope="session")
def get_firstsecond_files():
    myfile = "data/orders.csv"
    mysecondfile = "data/orders2.csv"
    return (myfile ,mysecondfile)

@pytest.fixture(scope="session")
def delete_firstsecond_files(get_firstsecond_files):
    for f in get_firstsecond_files:
        try:
            fh.DeleteFile(f)
            return 0
        except:
            print(f"file not exist: '{f}'")
            return 1