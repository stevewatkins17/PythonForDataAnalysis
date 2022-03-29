import time
import pyodbc

def get_MSSQL_connection(mssql_instance ,mssql_DB):
    """MSSQL connection with retry and timeout management"""
    retry ,wait ,cn_timeout ,qry_timeout = 2 ,30 ,15 ,0
    for _ in range(retry):
        try:
            cn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={mssql_instance};"
                f"DATABASE={mssql_DB};"
                "trusted_connection=Yes;"
                "Encrypt=no;"
                "APP=MyAppName;"
                ,timeout=cn_timeout)
            cn.timeout = qry_timeout
        except:
            #log.warning(f"Failed to connect to [{mssql_instance}].[{mssql_DB}]", exc_info=True)
            print(f"Failed to connect to [{mssql_instance}].[{mssql_DB}]")
            time.sleep(wait)
            continue
        else:
            return cn
    else:
        #log.warning(f"After {retry} attempts, failed to connect to [{mssql_instance}].[{mssql_DB}]")
        print(f"After {retry} attempts, failed to connect to [{mssql_instance}].[{mssql_DB}]")

# format: SQL Server ODBC Driver 17 for linux (requires mssql port number)
mssql_fq_instance_name ,DBname = "MyServerName.example.org,1433" ,"MyDb"

conn = get_MSSQL_connection(mssql_fq_instance_name ,DBname)

if not conn:
    print("Fail: mssql connection")
else:
    """ we stub in a 'pass' msg in place of executing SQL stmt"""
    print("Pass: mssql connection")

