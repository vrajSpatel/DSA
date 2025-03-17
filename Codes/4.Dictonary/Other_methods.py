mydict = {
    'name':'vraj',
    'age' : 21,
    'city': 'vadodara'
}

di = mydict  # if you assign it to some new element then memory location is same and if you change something it will also change in main
di['age'] = 29
# print(mydict)

new_dict = mydict.copy() # copy the dictonary in new memory
new_dict['age'] = 22


# fromkeys
li = ['name','age','locatin','name']
li2 = None
di2 = {}.fromkeys(li,li2)
print(di2)


# get
# give the value of that perticular key if key is not available then it will print default value that is given
# print(di2.get('name','not found'))  #None
# print(di2.get('lastname','not found')) # not found

# items -> print the object of tuple that contain key and value
print(list(mydict.items()))

# keys -> retrun the keys of dictonary in object form
print((list(mydict.keys())))

# value -> return the values
print((list(mydict.values())))

#update -> add the new elements to out dictonary
newele = {
    1 : 1 ,
    2:2,
    3:3
}
mydict.update(newele)
print(mydict)