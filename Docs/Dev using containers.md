This is an in-progress help doc for development using Anaconda & vscode inside a docker container.

# GIT

cd /Users/stevewatkins/Downloads/CodeLouisville
git clone https://github.com/stevewatkins17/unittest_mssql.git
cd unittest_mssql
git checkout feature/01
# we fork for CL the most up-to-date branch
git checkout -b feature01/02



# RESOURCES
[Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)

## Start SQL Server 2019 container
``` docker container start festive_ellis ```

Python container that mounts a local file path into the container, and opens bash CLI.
```
docker run --rm -it --entrypoint bash -v /Users/stevewatkins/Downloads/CodeLouisville/PythonForDataAnalysis:/usr/src/PythonForDataAnalysis python:3.9
```
```
docker run --rm -it --entrypoint bash -v /Users/stevewatkins/Downloads/CodeLouisville/CL_unittest_mssql:/usr/src/CL_unittest_mssql andrevs/debian-python3:latest
```
SQL Server 2019 container (replace "MYPASSWORD" with your own PW)
```
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=MyP@ssword1" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest 

```

Azure SQL container
```
docker run --cap-add SYS_PTRACE -e 'ACCEPT_EULA=1' -e 'MSSQL_SA_PASSWORD=MyP@ssword1' -p 1433:1433 --name azuresqledge -d mcr.microsoft.com/azure-sql-edge

```


# Step 0 - install tools
- review [Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)
- Install Docker, vscode, Azure Data Studio
- update local repo for dev 

# Step 1 - setup vscode for Project 
"Start VS Code, run the Remote-Containers: Open Folder in Container... command from the Command Palette (F1)"

For our example, we choose "Python 3" --> "Debian" --> "3.8 Buster" --> "Azure CLI"

Doing the above downloads a Debian "Buster" (version 10) linux image with Python 3.8, and AZ CLI installed.

# Step 2 - install ODBC Driver 17 for SQL Server 
We follow these instructions for Debian 10.

[Install the Microsoft ODBC driver for SQL Server (Linux)](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)

# Step 3 - pip install pyodbc
run "pip install pyodbc"

# Step 4 - run test
python test_pyodbc_sql_server.py

sqlcmd -S mssql_2019 -U SA -p "MyP@ssword1" -Q "SELECT @@VERSION"

telnet mssql_2019
docker container exec -u 0 -it mssql_2019 bash
