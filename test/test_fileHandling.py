import pytest
import zipfile as z
import pathlib
import os
import shutil
from .. src import fileHandling as fh

@pytest.fixture
def get_current_wd_path():
    path = os.getcwd()
    return path

@pytest.fixture
def get_zip_names():
    zip_pathfilename = "/data/trips.csv.zip"
    extract_foldername = "myziptest"
    unzip_filename = "trips.csv"
    return zip_pathfilename ,extract_foldername ,unzip_filename

@pytest.fixture
def UnzipFile(get_current_wd_path,get_zip_names):
    """we test unzip; the lack of a return code or value makes testing more complicated"""
    filePath = get_current_wd_path + get_zip_names[0]
    destinationDirectory = get_current_wd_path + f"/imported_projects/{get_zip_names[1]}"
    fh.UnzipFile(filePath ,destinationDirectory)
    print(filePath)
    print(destinationDirectory)
    return filePath ,destinationDirectory

def test_GetDirs(get_current_wd_path):
    dirlist = fh.GetDirs(get_current_wd_path)
    dirname = [d.name for d in dirlist if "src" in d.name]

    assert len(dirname) == 1
    assert dirname[0] == "src"

    dirname_not = [d.name for d in dirlist if "xsrc" in d.name]
    assert len(dirname_not) == 0
    assert "xsrc" not in dirname_not

def test_UnzipFile(UnzipFile,get_zip_names):
    """we test unzip; the lack of a return code or value makes testing more complicated"""
    assert os.path.isdir(UnzipFile[1]) == True
    assert os.path.isfile(UnzipFile[1] + f"/{get_zip_names[2]}") == True
 
def test_DeleteFile(UnzipFile,get_zip_names):
    result = fh.DeleteFile((UnzipFile[1] + f"/{get_zip_names[2]}"))

    assert result == 0
    assert os.path.isfile(UnzipFile[1] + f"/{get_zip_names[2]}") == False

    failresult = fh.DeleteFile((UnzipFile[1] + f"/biscuit.pet"))
    assert failresult == 1

def test_DeleteDir(UnzipFile):
    """ we test the FN and also cleanup test"""
    result = fh.DeleteDir(UnzipFile[1])

    assert result == 0
    assert os.path.isdir(UnzipFile[1]) == False
