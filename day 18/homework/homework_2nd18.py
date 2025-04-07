def manual_remove(set_collection, value_to_remove):
    if value_to_remove not in set_collection:
        raise KeyError(f"'{value_to_remove}' not found in set")
    
    result = set({})
    for item in set_collection:
        if item != value_to_remove:
            result.add(item)
    return result


print(manual_remove({"Gio", "Nika", "Luka"}, "Luka"))


def manual_pop(collection, index_remove = -1):
    if index_remove < 0:
        index_remove = len(collection) + index_remove
    
    result = []
    
    for index in range(len(collection)):
        if index != index_remove:
            result.append(collection[index])
    
    return result

print(manual_pop(["Gio", "Luka", "Nika"], -3))


def manual_insert(collection, item_insert, index_insert):
    if index_insert < 0:
        index_insert = len(collection) + index_insert
        
    result = []
    
    for index in range(len(collection)):
        if index == index_insert:
            result.append(item_insert)
            result.append(collection[index])
        else:
            result.append(collection[index])
    
    return result

print(manual_insert(["Gio", "Nika", "Luka"], "Deme", -1))


