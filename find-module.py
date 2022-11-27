
def import_mod():
    try:
        import pyodbc
        return 0
    except ModuleNotFoundError as err:
        return 1

mod_exist = import_mod()

if mod_exist == 0:
    print("module exists")
else:
    print("module NOT exist")
