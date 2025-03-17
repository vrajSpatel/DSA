from random import randint

# new_dict = {new_key:new_value for (key,value) in dict.items()}

cities = ['london', 'vadodara', 'ahemdabad', 'mumbai']

new_dict = {city:randint(1,100) for city in cities}
print(new_dict)

