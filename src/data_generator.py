# src/data_generator.py
import random
import argparse

def create_csv(myfile ,linecount ,list0 ,list1 ,list2):
    """ we generate and persist a csv file """
    with open(myfile, "w", encoding="utf-8") as file:
        # Writing data to a file
        for _ in range(linecount):
            item0 = random.choice(list0)
            item1 = random.choice(list1)
            item2 = random.choice(list2)
            myline = "||".join([item0 ,item1 ,item2])
            file.writelines(f"{myline} \n")
    return 0

def main(myfile ,linecount):
    """ we pass input variables to FN that generates and persists a csv file """
    
    maincourse = ["" ,"haggis" ,"Miquel's Pizza" ,"falafel" ,"pesce con vivo" ,"hasenpfeffer" ,"green coconut curry" ,"ciopinno" ,"potato pie"]
    veg = ["" ,"potato au gratin" ,"Chef John 5-spice carrots" ,"kale" ,"broccali" ,"brussels sprouts" ,"cauliflower" ,"peas" ,"roasted green beans"]
    dessert = ["" ,"tavuk göğsü" ,"creme brulee" ,"Mizu Shingen Mochi" ,"green chile chocolate tart" ,"melopita" ,"saffron kheer" ,"cinnamon brioche" ,"mom's peach cobbler" ,"cherry ice cream"]
    
    csv_create_result = create_csv(myfile ,linecount ,maincourse ,veg ,dessert)
    return csv_create_result

if __name__ == '__main__':
    """ python src/data_generator.py -f "Data/orders.csv" -c "117" """
    parser = argparse.ArgumentParser(description='generates a mock data file')
    parser.add_argument('-f','--filename' ,type=str, required=True ,help='relative path and file name')
    parser.add_argument('-c','--count',type=int ,required=True ,help='count of mock records to generate')

    args = parser.parse_args()
 
    myresult = main(args.filename ,args.count)
    
