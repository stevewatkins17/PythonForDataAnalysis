# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import zipfile as z
import pathlib
import os
import shutil


# %%
def GetDirs(path):
    p = pathlib.Path(path)
    dirlist = [x for x in p.iterdir() if x.is_dir()]
    return dirlist
        
    
def UnzipFile(filePath, destinationDirectory):    
    zf = z.ZipFile(f"{filePath}","r")
    zf.extractall(f"{destinationDirectory}")
    zf.close()

## Context Manager version of above 
#with z.ZipFile("Data/trips.csv.zip","r") as zf:
#    zf.extractall("Data")

# using os, we delete the big csv, if exists
def DeleteFile(target_file):
    if os.path.isfile(target_file):
        os.remove(target_file)
        return 1
    else:
        return 0
    
def DeleteDir(target_dir_to_delete):
    try:
        shutil.rmtree(target_dir_to_delete)
        return 1
    except OSError as e:
        return 0    
    


# %%
# test script
dirs_before_unz = GetDirs("Data")
#UnzipFile("Data/trips.csv.zip" , "Data")
UnzipFile("Data\\trips.csv.zip" , "Data")
dirs_after_unz = GetDirs("Data")
dir_unz = (list(set(dirs_after_unz) - set(dirs_before_unz)))
target_dir_to_delete = dir_unz[0]
DeleteFile("Data/trips.csv")
DeleteDir(target_dir_to_delete)


