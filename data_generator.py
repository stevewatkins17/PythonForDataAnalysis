import random

x = 20000
maincourse = ["pasta" ,"pizza" ,"falafel" ,"pesce con vivo" ,"hasenpfeffer" ,"green coconut curry" ,"ciopinno"]
veg = ["potato" ,"carrots" ,"kale" ,"broccali" ,"brussels sprouts" ,"cauliflower" ,"peas"]
dessert = ["chocolate tort" ,"chili chocolate tart" ,"melopita" ,"saffron kheer" ,"cinnamon brioche" ,"mom's peach cobbler" ,"vanilla ice cream"]

with open("Data/orders.csv", "a") as file:
    # Writing data to a file
    for _ in range(x):
        mc = random.choice(maincourse)
        v = random.choice(veg)
        d = random.choice(dessert)
        #order = " ,".join(["\"" + mc + "\"", "\"" + v + "\"","\"" + d + "\""])
        order = " ,".join([mc ,v ,d])
        file.writelines(f"{order} \n")