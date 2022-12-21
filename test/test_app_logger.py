import pytest ,os
from ..src import app_logger

logfile = "data/test.log"

@pytest.fixture
def get_log():
    #log = python_logging.persist_sample_log("../data/test.log")
    log = app_logger.get_logger("mylogger",logfile)
    return log

@pytest.fixture
def delete_log():
    os.remove(logfile)
    return 0

def test_get_log(get_log):
    #log = get_log
    get_log.info("mytest 0")
    assert os.path.isfile(logfile) == True

def test_logwrite(get_log):
    count = 0
    # open file in read mode
    with open(logfile, 'r') as f:
        count = sum(1 for line in f)
    assert count > 0

def test_delete_log(delete_log):
    assert os.path.isfile(logfile) == False
