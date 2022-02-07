
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filter_func(name):
    return name[0] == "R"

resulting_names = list(filter(filter_func, all_names))

print(resulting_names)




