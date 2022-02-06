chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    merged_list = []
    #Your code go here:
    for name in list1:
        merged_list.append(name)
    for other_name in list2:
        merged_list.append(other_name)
    return merged_list

    
print(merge_list(chunk_one, chunk_two))
