SourceDB = "tempdb"
SourceInstance = "localhost"
createlogin = "CREATE LOGIN mylogin WITH PASSWORD = 'Myp@ssword';"
# replace mypasswrd with actual sa pw
# PWD = 'mypassword'
Query_pt = """
select top 100 *
from [sys].[objects];
"""