mydict = {
    'name':'vraj',
    'age' : 21,
    'city': 'vadodara'
}

di = mydict  # if you assign it to some new element then memory location is same and if you change something it will also change in main
di['age'] = 29
print(mydict)

new_dict = mydict.copy() # copy the dictonary in new memory
new_dict['age'] = 22


# fromkeys
