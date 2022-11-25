def query_table_help(tablename):
    return f"select * from PRAGMA_TABLE_INFO('{tablename}');"

def select_top10(tablename):
    return f"SELECT * FROM {tablename} limit 10;"

query_state_KM = """
select 
 Vendor_State
,sum(Vendor_Amount) as "Sum Amount"
,avg(Vendor_Amount) as "Avg Amount"
,count(*) as "Trans Count"
from stage_expenses_cleaned
group by Vendor_State

union all

select 
 '(Total)'
,sum(Vendor_Amount) as "Sum Amount"
,avg(Vendor_Amount) as "Avg Amount"
,count(*) as "Trans Count"
from stage_expenses_cleaned

order by "Sum Amount" desc;
"""

show_tables = """
SELECT * 
FROM sqlite_master
ORDER BY name;
"""

query_category_KM = """
select 
 Vendor_Category
,sum(Vendor_Amount) as "Sum Amount"
,avg(Vendor_Amount) as "Avg Amount"
,count(*) as "Trans Count"
from stage_expenses_cleaned
group by Vendor_Category

union all

select 
 '(Total)'
,sum(Vendor_Amount) 
,avg(Vendor_Amount) 
,count(*) 
from stage_expenses_cleaned

order by "Sum Amount" desc;
"""

query_st_map = """
select 
 Vendor_State as "VendorState"
,count(*) as "TransCount"
from stage_expenses_cleaned
group by Vendor_State
order by "VendorState" asc;
"""