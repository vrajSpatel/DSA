'''
def reverse_dict(my_dict):
    keys= list(my_dict.keys())
    values= list(my_dict.values())
    new_dict = {}
    for item in range(len(keys)):
        new_dict[values[item]] = keys[item]
    return new_dict


'''



def reversre_dict(my_dict):
    new_dict = {value : key for key,value in my_dict.items()}
    return new_dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reversre_dict(my_dict))
