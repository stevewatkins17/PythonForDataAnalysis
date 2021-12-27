This is an in-progress help doc for development using Anaconda & vscode inside a docker container.

# RESOURCES
[Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)

Python container that mounts a local file path into the container, and opens bash CLI.
```
sudo docker run --rm -it --entrypoint bash -v /Users/stevewatkins/Downloads/CodeLouisville/PythonForDataAnalysis:/usr/src/PythonForDataAnalysis python:3.9
```

SQL Server 2019 container (replace "MYPASSWORD" with your own PW)
```
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=MYPASSWORD“ -p 1433:1433 --name sql1 -h sql1 -d mcr.microsoft.com/mssql/server:2019-latest
```

Azure SQL container
```
docker run --cap-add SYS_PTRACE -e 'ACCEPT_EULA=1' -e 'MSSQL_SA_PASSWORD=//Monday7104//' -p 1433:1433 --name azuresqledge -d mcr.microsoft.com/azure-sql-edge

```