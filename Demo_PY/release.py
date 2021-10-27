import datetime
import pytz
import json

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
est_now = utc_now.astimezone(pytz.timezone("America/Louisville"))

est_now = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("America/Louisville"))

seconds_since_midnight = str(int((est_now - est_now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()))
print(seconds_since_midnight)

class Release:   

    def __init__(self ,assertID ,release_assert):
        self.mydatetime = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("America/Louisville"))
        self.assertID = assertID
        #release_assert = dict(release_assert)
        self.workbook_items = release_assert["workbooks"]
        self.servers_customers = release_assert["tableau_servers"]

    def assert_release(self ,assert_log):
        pass

    def myfunction(self):
        print("Hello")

    def myfunction2(self):
        print("Hello2")


    MyString = "MyString1"

    #workbook_items = release_assert["workbooks"]

#release_assert_log = 
#     {"ID": "1" ,"server":"https://basrv.qa.hchb.local" ,"content_url":"hov" ,"workbook":"Workbook1" ,"start":"UTC datetime" ,"stop":"UTC datetime" ,"status":"0"}
#    ,{"ID": "1" ,"server":"https://basrv.qa.hchb.local" ,"content_url":"QA" ,"workbook":"Workbook1" ,"start":"UTC datetime" ,"stop":"UTC datetime" ,"status":"0"}
#    ,{"ID": "1" ,"server":"https://basrv.qa.hchb.local" ,"content_url":"Wabash" ,"workbook":"Workbook1" ,"start":"UTC datetime" ,"stop":"UTC datetime" ,"status":"0"}

def create_json_from_dict(mydict ,myfilepathname):
    with open(myfilepathname, "w+") as fileToSave: 
        json.dump(mydict, fileToSave, ensure_ascii=True, indent=4, sort_keys=False)

def build_init_assert_log(myAssert):
    for workbook in myAssert["workbooks"]:
        pass#print("workbook = " + workbook)

#imported log template
assert_workbook_release_log = {
    "retry" : 0
    ,"begin_timestamp" : "2021-06-03 13:00"
    ,"update_timestamp" : "2021-06-03 14:00"
    ,"status" : "In Progress"
    ,"workbook1":{
            "https://basrv.qa.hchb.local" : {
                 "enqueue" : []    
                ,"fail" : []    
                ,"complete" : []
        }
    }
}

def get_system_settings():
    system_settings_data  = "data/system_settings.json" 

    with open(system_settings_data, "r") as read_file:
        system_settings = json.load(read_file)
        for key, value in system_settings.items():
            if key == "internal_user_names":
                internal_user_names = value
            if key == "anchor_instance":
                """for MSSQL Configuration DB access; can be any Live Prod HCHB MSSQL instance but we use IT's supported alias"""
                anchor_instance = value
            if key == "anchor_DB":
                anchor_DB = value
            if key == "cn_retry":
                cn_retry = value
            if key == "retry_wait":
                """int seconds between retry attempt"""
                retry_wait = value
            if key == "cn_timeout":
                """int seconds wait for MSSQL connection"""
                cn_timeout = value
            if key == "qry_timeout":
                """int seconds wait for MSSQL to complete query exe"""
                qry_timeout = value
            if key == "customer_codename_exceptions":
                """we map exceptions where the Tableau customer 'content_url' != SQL Server customer code name"""  
                """the customer Tableau 'content_url' site name (eg. 'Encompass') is mapped to the customer MSSQL datasource code name (used for DB name ('bi_edw_ehhi') & SQL Server instance alias (eg. 'tabds-ehhi')"""
                customer_codename_exceptions = value
            if key == "excluded_customers":
                """'server' : [(myCustomer_Name ,MyCustomer_contenturl) ,...]"""
                """note we INCLUDE ('*Demo', 'Analytics_DEMO') in TX & KY but EXCLUDE in QA"""
                excluded_customers = value
            if key == "pat_auth":
                pat_auth = value
            if key == "customer_fileshare":
                customer_fileshare = value
            if key == "datasource_alias":
                datasource_alias = value
            if key == "deploy_template_codes":
                deploy_template_codes = value
            if key == "customer_codename_exception_map":
                customer_codename_exception_map = value
            if key == "AD_groups_roles":
                AD_groups_roles = value
            if key == "QA_env":
                QA_env = value
            if key == "pat_map":
                pat_map = value
    return internal_user_names ,anchor_instance ,anchor_DB ,cn_retry ,retry_wait ,cn_timeout ,qry_timeout ,customer_codename_exceptions ,excluded_customers ,pat_auth ,customer_fileshare ,datasource_alias ,deploy_template_codes ,customer_codename_exception_map ,AD_groups_roles ,QA_env ,pat_map

#imported json configuration
# "data/workbook_release_configuration_dict.json"

def get_release_configuration():
    release_configuration_data  = "data/workbook_release_configuration.json" 

    with open(release_configuration_data, "r") as read_file:
        release_configuration = json.load(read_file)
        tableau_servers = {}

        for key, value in release_configuration.items():
            print(f"key: '{key}', value: '{value}'")
            if key == "workbooks":
                workbooks = value
            if key == "https://basrv.qa.hchb.local":
                myserver_dict = dict(value) #["ReleaseEnable"] == "True":
                if myserver_dict["ReleaseEnable"] == "True":
                    tableau_servers.update(value)

    return workbooks ,tableau_servers

workbooks ,tableau_servers = get_release_configuration()

print(tableau_servers)

"""tableau_servers_scope = {}

for key, value in tableau_servers.items():
    print(key, value)
    if tableau_servers[key]["ReleaseEnable"] == False:
        tableau_servers_scope.update

print(tableau_servers_scope)
"""

#print(workbooks,tableau_servers)

internal_user_names ,anchor_instance ,anchor_DB ,cn_retry ,retry_wait ,cn_timeout ,qry_timeout ,customer_codename_exceptions ,excluded_customers, pat_auth ,customer_fileshare ,datasource_alias ,deploy_template_codes ,customer_codename_exception_map ,AD_groups_roles ,QA_env ,pat_map= get_system_settings()

workbook_release_configuration_dict_json = {
    "workbooks": [
        "Workbook1" 
        ,"Workbook2" 
        ,"Workbook3"
        ] 
    ,"tableau_servers" : {
        "https://basrv.qa.hchb.local" : {
             "ReleaseEnable" : "True"
            ,"include_content_urls": [
                 "QA"
                ,"Wabash" 
                ,"HOV"
                ,"AccentCare"
                ]
            ,"exclude_content_urls": [
                "Test"
                ,"SUTTER"
                ,"Demo"
                ,"HOV"
                ,"MyFakeCustomer1"
                ]
            }
        ,"https://basrv.qa.hchb.local" : {
             "ReleaseEnable" : "True"
            ,"include_content_urls": [
                ]
            ,"exclude_content_urls": [
                "Test"
                ,"VERITAS"
                ,"Demo"
                ,"RIVERSIDE"
                ]
            }
        ,"https://basrv.qa.hchb.local" : {
             "ReleaseEnable" : "False"
            ,"include_content_urls": [
                ]
            ,"exclude_content_urls": [
                ]
            }
    }
}

release = Release(0,workbook_release_configuration_dict_json)

release_log = {}

for wkbk in release.workbook_items:
    #print(wkbk)
    log_file = f"release[{wkbk}]{seconds_since_midnight}.log"
    for server in release.servers_customers:
        #person['fname'] = 'Joe'
        enqueue = release.servers_customers[server]["include_content_urls"]
        completed = []
        fail = []
        release_log["assertID"] = 0
        release_log["begin_datetime"] = str(est_now)
        release_log[server] = {"enqueue" : enqueue}
        create_json_from_dict(mydict = release_log ,myfilepathname = f"data/{log_file}")
        for customer in enqueue:
            enqueue.remove(customer)
            completed.append(customer)
            release_log[server] = {"enqueue" : enqueue}
            release_log[server] = {"completed" : completed}
            create_json_from_dict(mydict = release_log ,myfilepathname = f"data/{log_file}")
            pass#print(f"publish {wkbk} for customer {customer} on server {server}")


myservers = workbook_release_configuration_dict_json["tableau_servers"].keys()
#print(myservers)

my_stub_dict = {'https://basrv.qa.hchb.local': {'include_content_urls': ['QA', 'Wabash', 'HOV'], 'exclude_content_urls': ['Test', 'QA', 'Demo', 'HOV']}, 'https://basrv.qa.hchb.local': {'include_content_urls': ['QA', 'Wabash', 'HOV'], 'exclude_content_urls': ['Test', 'QA', 'Demo', 'HOV']}}

for key in my_stub_dict:
    include_content_urls = my_stub_dict[key]["include_content_urls"]
    exclude_content_urls = my_stub_dict[key]["exclude_content_urls"]
    #print(key ,include_content_urls)
    #print(key ,exclude_content_urls)
    if not include_content_urls:
        pass #get content_urls from server query


for key, value in my_stub_dict.items():
    pass
    #print(value["include_content_urls"])

create_json_from_dict(mydict = workbook_release_configuration_dict_json ,myfilepathname = "/Users/stevewatkins/Downloads/release_assert.json")

build_init_assert_log(myAssert=workbook_release_configuration_dict_json)


release.myfunction()
#release.myfunction2()

#print(release.workbook_items)
#print(release.servers_customers)
#print(release.MyString)
#release.assertID = 0
#print(release.mydatetime)
#print(release.assertID)
#print(release.assert_log)
