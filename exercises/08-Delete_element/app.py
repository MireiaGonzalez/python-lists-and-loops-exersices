people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_people = []
    for name in people:
        if name.lower() != person_name:
            new_people.append(name)
    return new_people

    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))