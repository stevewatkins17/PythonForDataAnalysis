import json

# a string is an iterable
myname = "janet"
x = 1 

for i in myname:
    print(f"letter {x} = {i}")
    x += 1

print(f"the character in the 4th position of {myname} is {myname[3]}")
print("--------------------")

# https://pynative.com/python-range-function/
for i in range(10):
    print(i)

print("--------------------")

for i in range(10, 0, -2):
    print(i)
print("--------------------")

mytuple_0 = ("A" ,"B")
mytuple_1 = ("C" ,"D")
mytuple_0 = mytuple_0 + mytuple_1
print(mytuple_0)
print("--------------------")

print(mytuple_0[2])

# mytuple_0[2] = "Z" #intentional fail

mylist = list(mytuple_0)
mylist[2] = "Z"
print(mylist[2])

print("--------------------")

for character in mytuple_0:
    print(character)

# dictionaries are also iterable
# https://realpython.com/python-dicts/
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

my_release_configuration_file = "IpythonNotebooks/Data/workbook_release.config"

release_configuration ,workbooks ,tableau_servers_scope ,datasource ,internal ,olap ,index  = get_release_configuration(my_release_configuration_file)    

# release_configuration  = get_release_configuration(my_release_configuration_file)[0]

print(release_configuration)

print("--------------------")

for w in workbooks:
    print(f"workbook name = {w}")

print("--------------------")

for ofs in release_configuration["other_files"]:
    print(f"other_files = {ofs}")

