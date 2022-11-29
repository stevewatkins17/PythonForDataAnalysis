import json

def iter_immutable_obj(imm_obj):
    """ strings or tuples are immutable objects with custom properties/methods """
    """ we can transform a string or tuple into a dictionary using the index ID as key """
    string_as_dict = {}

    for index, c in enumerate(imm_obj, start=0):
        print(f"{index}: '{c}'")
        string_as_dict[index] = c

    print("--------------------")
    print(string_as_dict)
    print("--------------------")
    return string_as_dict

def iter_simple_range(stop):
    for i in range(stop):
        print(f"simple range: {i}")
    print("--------------------")
    return 0

def iter_complex_range(start, stop, step):
    for i in range(start, stop, step):
        print(f"complex range: {i}")
    print("--------------------")
    return 0

def fun_with_tuples(*tuples):
    mega_tuple = ()
    for t in tuples:
        print(f"tuple: {t}")
        mega_tuple += t
    print("--------------------")
    print(mega_tuple)    
    print("--------------------")
    return mega_tuple

# EXAMPLE 4 - lists
def listomania(myobject):
    mylist = list(myobject)
    mylist[2] = "Z17"
    print(mylist)
    print("--------------------")

    return mylist 

# EXAMPLE 5 - dictionaries 

def get_release_configuration(release_configuration_file):
    """Parse 'workbook_release.config' to retrieve and return runtime params"""  
    with open(release_configuration_file, "r") as read_file:
        release_configuration = json.load(read_file)

        workbooks = release_configuration["workbooks"]
        tableau_servers = release_configuration["tableau_servers"]
        datasource = str(release_configuration["other_files"]["datasource"])
        internal = str(release_configuration["other_files"]["internal"])
        olap = str(release_configuration["other_files"]["olap"])
        index = str(release_configuration["other_files"]["index"])

    return release_configuration ,workbooks ,tableau_servers ,datasource ,internal ,olap ,index

def simple_dictionary(thisdictionary):
    for w in thisdictionary:
        print(f"name = {w}")
    print("--------------------")
    return 0

def combine_dictionaries():
    dictA = {"mykey1":"valueA" ,"mykey2":{"Pass":2 ,"Fail":0 ,"NA":0 ,"null":10}}
    dictB = {"mykey1":"valueB" ,"mykey2":{"Pass":0 ,"Fail":1 ,"NA":1 ,"null":0}}
    dict_combined = {}
    print("dictA")
    print(dictA)
    print("dictB")
    print(dictB)
    dict_combined["dictA"] = dictA["mykey2"]
    dict_combined["dictB"] = dictB["mykey2"]
    print("dict_combined")
    print(dict_combined)

    return dict_combined

def main():
    my_release_configuration_file = "../data/workbook_release.config"

    string_as_dict = iter_immutable_obj("Hello")
    iter_simple_range(5)
    iter_complex_range(10, 6, -2)
    tuple_as_dict = iter_immutable_obj(("Hello" ,"World!"))
    dict_as_dict = iter_immutable_obj(string_as_dict)
    mega_tuple = fun_with_tuples(("Q" ,"Z") ,("V" ,"W"))
    mylist = listomania(mega_tuple)

    release_configuration ,workbooks ,tableau_servers_scope ,datasource ,internal ,olap ,index  = get_release_configuration(my_release_configuration_file)    
    print(release_configuration)
    print("--------------------")
    simple_dictionary(workbooks)
    simple_dictionary(release_configuration["other_files"])

    return 0

if __name__ == '__main__':
    main()
