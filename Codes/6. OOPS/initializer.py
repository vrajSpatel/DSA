'''
to use initializer python has __init__ function
'''

class Info:
    company = 'vtf'
    def __init__(self,name='vrj', id=0):
        # we can also give default value to the parameter
        '''
        initialize the attribute here
        going to run first everytime object creted from this class
        '''
        self.name = name
        self.id = id

    def printName(self):
        print(self.name)

emp1 = Info(id=1212)
print(emp1.name,emp1.id)
emp1.name = 'newname'
print(emp1.name)

print(emp1.company) #every object has this same value for this class

# example
emp2 = Info('vraj',1212)
print(emp2.company,emp2.name,emp2.id)


# __dict__ function gives you information about object and class
print(emp1.__dict__)
print(emp2.__dict__)
print(Info.__dict__)

emp1.printName()
