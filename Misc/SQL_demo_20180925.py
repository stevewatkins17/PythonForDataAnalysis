
# coding: utf-8

# ## https://www.dataquest.io/blog/sql-basics/
# 
# ### Covering
#  - SELECT
#  - WHERE
#  - GROUP BY
#  - JOIN
#  - Conditionals

# In[1]:


import os
os.getcwd()
# os.chdir("/Users/stevewatkins/python3/demos/sqlite") # relative path: scripts dir is under Users/stevewatkins


# ## create conn. and "read results" pd function

# In[2]:


import sqlite3
import pandas as pd

db = sqlite3.connect("hubway.db")

def run_query(query):
    return pd.read_sql_query(query,db)


# ## read metadata about sqlite DB tables

# In[3]:


query = """
SELECT * 
FROM sqlite_master
ORDER BY name;
"""
run_query(query)


# ## select all from table

# In[4]:


query = "SELECT * FROM trips LIMIT 5;"
run_query(query)


# ## select 2 columns from table with custom order

# In[5]:


query = """
SELECT 
     duration
    ,start_date 
FROM trips 
ORDER BY duration DESC ,start_date ASC
LIMIT 5;
"""
run_query(query)


# ## select all where duration is max, using limit & order desc

# In[6]:


query = '''
SELECT duration ,*
FROM trips
ORDER BY duration DESC
LIMIT 1;
'''

run_query(query)


# ## select max duration per each start_station, using group by

# In[7]:


query = """
SELECT max(duration) ,start_station 
FROM trips
group by start_station
order by 1 desc
limit 5;

"""

run_query(query)


# ## where clause to filter resultset

# In[8]:


query = '''
SELECT * 
FROM trips
WHERE duration > 9990
--limit 5
;
'''

run_query(query)


# # AND condition

# In[9]:


query = '''
SELECT * 
FROM trips
WHERE (duration >= 9990) AND (sub_type = "Registered")
ORDER BY duration DESC;
'''

run_query(query)


# # Count with AND condition

# In[10]:


query = '''
SELECT 
  COUNT(*) AS "Total Trips by Registered Users"  
FROM trips
WHERE sub_type = "Registered";
'''

run_query(query)


# # Aggregating data with GROUP BY

# In[11]:


query = '''
SELECT 
   sub_type
  ,COUNT(*) AS "Total Trips by Registered Users"  
FROM trips
group by sub_type
order by 2 desc;
'''

run_query(query)


# In[12]:


query = '''
SELECT sub_type, AVG(duration) AS "Average Duration"
FROM trips
GROUP BY sub_type;
'''

run_query(query)


# # which bike was used for the most trips?

# In[13]:


query = '''
SELECT bike_number as "Bike Number", COUNT(*) AS "Number of Trips"
FROM trips
GROUP BY bike_number
ORDER BY COUNT(*) DESC
LIMIT 1;
'''

run_query(query)


# # Arithmetic Operators

# In[14]:


query = '''
SELECT AVG(duration)
FROM trips
WHERE (2018 - birth_date) > 30;
'''

run_query(query)


# In[15]:


query = '''
SELECT 
 birth_date  as "birth year"
,(2017 - birth_date) as "Years Old"
,date('now') as "now date"
,(strftime('%Y',date('now'))) as "now Year string"
,((strftime('%Y',date('now'))) - birth_date) as "Years Old revised"
FROM trips
WHERE (2018 - birth_date) > 30
and birth_date <> '';
'''

run_query(query)


# # Joins

# In[16]:


query = '''
SELECT *
FROM stations
where id = 23
LIMIT 5;
'''
run_query(query)


# In[17]:


query = '''
SELECT *
FROM trips
where start_station = 23 -- or end_station = 23
LIMIT 5;
'''
run_query(query)


# In[18]:


query = '''
SELECT s.* ,t.*
FROM trips t
INNER JOIN stations s ON t.start_station = s.id
and s.id = 23
--GROUP BY s.station
ORDER BY 1 DESC
LIMIT 5;
'''

run_query(query)


# # Create new DB & table

# In[19]:


#intentional failure; SQL is syntactically correct
query = '''
CREATE TABLE IF NOT EXISTS MyTable(rid integer);
'''

#run_query(query)


# In[20]:


create_table_sql = '''
CREATE TABLE IF NOT EXISTS MyTable(rid integer);
'''

cn2 = sqlite3.connect("MySqlite.DB")

c = cn2.cursor()

c.execute(create_table_sql)

MyQuery = """
SELECT * 
FROM sqlite_master
ORDER BY name;
"""

c.execute(MyQuery)

c.close()

#pd.read_sql_query(MyQuery,cn2)


# # INSERT, UPDATE, DELETE

# In[21]:


MyInsert = 'insert into MyTable values(-199) ,(17);'

c = cn2.cursor()

c.execute(MyInsert)

cn2.commit()

c.close()

pd.read_sql_query("select * from MyTable;",cn2)


# In[22]:


MyUpdate = 'update MyTable set rid = 0 where rid = -199;'

c = cn2.cursor()

c.execute(MyUpdate)

cn2.commit()

c.close()

pd.read_sql_query("select * from MyTable;",cn2)


# In[23]:


MyDelete = 'delete from MyTable where rid = 0;'

c = cn2.cursor()

c.execute(MyDelete)

cn2.commit()

c.close()

pd.read_sql_query("select * from MyTable;",cn2)

