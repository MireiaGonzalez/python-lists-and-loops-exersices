names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
names[1] = "Steven"
names[len(names)-1] = "Pepe"

third_element = names[2]
fifth_element = names[4]

names[0] = third_element+fifth_element


for x in range(len(names)-1, -1, -1):
    print(names[x])