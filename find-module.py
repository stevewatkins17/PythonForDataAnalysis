try:
    import pyodbc
except ModuleNotFoundError as err:
    # Error handling
    print(err)