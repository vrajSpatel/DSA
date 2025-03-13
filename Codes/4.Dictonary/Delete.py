myDict = {
    'name' : 'vraj',
    'age' : 21,
    'city' : 'vadodara'
}

# del myDict['age']   #o(1)
new_dict1 = myDict.pop('name') #remove the key-value pair of key name

# di = myDict.clear() # empty

di2 = myDict.popitem()
print(di2)
