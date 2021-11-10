import json
import collections
import pytz
import datetime


def create_json_from_dict(mydict ,myfilepathname):
    """convert input dictionary to formatted json file """  
    try:
        with open(myfilepathname, "w+") as fileToSave: 
            json.dump(mydict, fileToSave, ensure_ascii=True, indent=4, sort_keys=False)
            return 0
    except:
        return 1

def convert_json_to_dict(myfilepathname):
    """convert input json to dictionary """  
    try:
        with open(myfilepathname, "r") as read_file:
            my_new_dict =  dict(json.load(read_file))
            
    except:
        my_new_dict = {}
    
    return my_new_dict


def create_detail_results():
    detail_results = {"test 3": "Pass" ,"test 0": "Fail" ,"test 1": None}
    return detail_results


def main():
    timestamp_b = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("America/Louisville"))
    timestring_file =  timestamp_b.strftime("%Y%m%d%H%M%S")

    configuration = convert_json_to_dict("configuration.json")

    unit_test_batch_name = configuration["unit_test_batch_name"]

    print(f"unit_test_batch_name = '{unit_test_batch_name}'")

    outputfilename = f"output ({timestring_file}).json"

    detail_results = create_detail_results()
    test_results = {}

    test_results["timestamp_begin"] = str(timestamp_b)
    test_results["timestamp_end"] = str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("America/Louisville")))
    test_results["results"] = collections.OrderedDict(sorted(detail_results.items()))

    create_json_from_dict(test_results ,outputfilename)

    timestamp_e = pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("America/Louisville"))

if __name__ == "__main__":
    main()
