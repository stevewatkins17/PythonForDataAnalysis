# find_module.py
# given an input module name, we test its existence by importing it
# note this is an intientionally simple & immature script for demo purposes
import importlib

def import_mod(module_name):
    try:
        target_module = importlib.import_module(module_name, package=None)
        return 0
    except ModuleNotFoundError as err:
        return 1

module_name = "pyodbc"
mod_exist = import_mod(module_name)

if mod_exist == 0:
    print("module exists")
else:
    print("module NOT exist")
