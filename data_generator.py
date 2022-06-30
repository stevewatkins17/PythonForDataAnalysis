import random

def create_csv(myfile ,linecount ,list0 ,list1 ,list2):
    with open(myfile, "w") as file:
        # Writing data to a file
        for _ in range(linecount):
            item0 = '"' + random.choice(list0) + '"'
            item1 = '"' + random.choice(list1) + '"'
            item2 = '"' + random.choice(list2) + '"'
            myline = "||".join([item0 ,item1 ,item2])
            file.writelines(f"{myline} \n")
    return 0

def main():
    linecount = 20000
    maincourse = ["" ,"haggis" ,"Miquel's Pizza" ,"falafel" ,"pesce con vivo" ,"hasenpfeffer" ,"green coconut curry" ,"ciopinno" ,"potato pie"]
    veg = ["" ,"potato au gratin" ,"Chef John 5-spice carrots" ,"kale" ,"broccali" ,"brussels sprouts" ,"cauliflower" ,"peas" ,"roasted green beans"]
    dessert = ["" ,"tavuk göğsü" ,"creme brulee" ,"Mizu Shingen Mochi" ,"green chili chocolate tart" ,"melopita" ,"saffron kheer" ,"cinnamon brioche" ,"mom's peach cobbler" ,"cherry ice cream"]
    myfile = "Data/orders.csv"

    csv_create_result = create_csv(myfile ,linecount ,maincourse ,veg ,dessert)
    return csv_create_result

if __name__ == '__main__':
    myresult = main()
    print(f"csv_create_result={myresult}")
