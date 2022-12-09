# SQL_demo_20180925.py
import os
import sqlite3
import pandas as pd
import urllib.request

#hubway.db: "https://www.dataquest.io/blog/large_files/hubway.db"
def get_hubway_db(hubway_db_file):
  if not os.path.isfile(hubway_db_file):
    urllib.request.urlretrieve("https://www.dataquest.io/blog/large_files/hubway.db", hubway_db_file)
  db = sqlite3.connect(hubway_db_file)
  return db

def run_query(query ,db):
    return pd.read_sql_query(query,db)

def get_top_trips(toplimit ,db):
  top_trips_sql = f"SELECT * FROM trips LIMIT {toplimit};"
  top_trips_results = run_query(top_trips_sql ,db)
  return top_trips_results

def get_table_metadata(db):
  get_table_metadata_sql = """
  SELECT * 
  FROM sqlite_master
  ORDER BY name;
  """
  metadata_results = run_query(get_table_metadata_sql ,db) 
  return metadata_results

def get_top_duration(db ,mylimit):
  top_duration_sql = f"""
  SELECT 
      duration
      ,start_date 
  FROM trips 
  ORDER BY duration DESC ,start_date ASC
  LIMIT {mylimit};
  """
  top_duration_results = run_query(top_duration_sql ,db) 
  return top_duration_results

def get_highest_avg_duration_by_station(db ,mylimit):
  highest_avg_duration_by_station_sql = f"""
  SELECT s.station , avg(t.duration) as avg_duration 
  FROM trips t 
  join stations s on t.start_station = s.id
  group by s.station
  order by 2 desc
  LIMIT {mylimit};
  """
  highest_avg_duration_by_station_results = run_query(highest_avg_duration_by_station_sql ,db) 
  return highest_avg_duration_by_station_results

def get_hubway_query_store():

  duration_GT_9990 = '''
  SELECT * 
  FROM trips
  WHERE duration > 9990;
  '''

  duration_GTEQ_9990_registered = '''
  SELECT * 
  FROM trips
  WHERE (duration >= 9990) AND (sub_type = "Registered")
  ORDER BY duration DESC;
  '''

  Total_Trips_Registered = '''
  SELECT 
    COUNT(*) AS "Total Trips by Registered Users"  
  FROM trips
  WHERE sub_type = "Registered";
  '''

  Total_Trips_sub_type = '''
  SELECT 
    sub_type
    ,COUNT(*) AS "Total Trips by Registered Users"  
  FROM trips
  group by sub_type
  order by 2 desc;
  '''

  trip_avg_duration = '''
  SELECT sub_type, AVG(duration) AS "Average Duration"
  FROM trips
  GROUP BY sub_type;
  '''

  count_bike_trips = '''
  SELECT bike_number as "Bike Number", COUNT(*) AS "Number of Trips"
  FROM trips
  GROUP BY bike_number
  ORDER BY COUNT(*) DESC
  LIMIT 1;
  '''

  avg_duration_GT_30 = '''
  SELECT AVG(duration)
  FROM trips
  WHERE (2022 - birth_date) > 30;
  '''

  age_demographics = '''
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

  mega_join = '''
  SELECT s.* ,t.*
  FROM trips t
  INNER JOIN stations s ON t.start_station = s.id
  ORDER BY 1 DESC
  LIMIT 5;
  '''

  return duration_GT_9990 ,duration_GTEQ_9990_registered ,Total_Trips_Registered ,Total_Trips_sub_type ,trip_avg_duration ,count_bike_trips ,avg_duration_GT_30 ,age_demographics ,mega_join

def create_mytable():
  create_table_sql = '''
  CREATE TABLE IF NOT EXISTS MyTable(rid integer);
  '''

  cn2 = sqlite3.connect("../data/MySqlite.DB")

  c = cn2.cursor()

  c.execute(create_table_sql)

  MyQuery = """
  SELECT * 
  FROM sqlite_master
  ORDER BY name;
  """

  c.execute(MyQuery)

  c.close()

  return 0

def insert_mytable():
  MyInsert = 'insert into MyTable values(-199) ,(17);'

  cn2 = sqlite3.connect("../data/MySqlite.DB")

  c = cn2.cursor()

  c.execute(MyInsert)
  cn2.commit()
  c.close()

  pd.read_sql_query("select * from MyTable;",cn2)

def update_mytable():
  MyUpdate = 'update MyTable set rid = 0 where rid = -199;'

  cn2 = sqlite3.connect("../data/MySqlite.DB")
  c = cn2.cursor()

  c.execute(MyUpdate)

  cn2.commit()

  c.close()

  pd.read_sql_query("select * from MyTable;",cn2)

def delete_mytable():
  MyDelete = 'delete from MyTable where rid = 0;'

  cn2 = sqlite3.connect("../data/MySqlite.DB")
  c = cn2.cursor()

  c.execute(MyDelete)

  cn2.commit()

  c.close()

  pd.read_sql_query("select * from MyTable;",cn2)


def main():
  hubway_db_file = "../data/hubway.db"
  db = get_hubway_db(hubway_db_file)

  metadata_results = get_table_metadata(db)
  top_trips_results = get_top_trips(3,db)
  top_duration_results = get_top_duration(db,3)
  highest_avg_duration_by_station_results = get_highest_avg_duration_by_station(db,3)

  print(metadata_results)
  print(top_trips_results)
  print(top_duration_results)
  print(highest_avg_duration_by_station_results)

  return 0

if __name__ == '__main__':
  myresult = main()
