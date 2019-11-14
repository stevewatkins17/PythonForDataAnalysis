SourceDB = "HCHB_COMMON"
SourceInstance = "DBDWH202"
Query_pt = """
select top 100 
  [Pt_id]
 ,[Timestamp_est]
 ,[Object_name]
 ,[Row_count]
from [rec].[performancetrace2]
where [Object_name] is not null
and [Object_name] not in('sp_readrequest' ,'sp_executesql' ,'sp_execute' ,'usp_Queue_GetNextWorkItem' ,'start_execution')
order by [Cpu_time] desc;
"""