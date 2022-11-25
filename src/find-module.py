try:
    import pyodbc
    print("import module success")
except ModuleNotFoundError as err:
    # Error handling
    print(err)