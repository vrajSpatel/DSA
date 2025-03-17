a = [1,2,3]
t = (1,2,3,4)

print(a.index(1))
print(t.index(3))

def SearchingElement(tupp,ele):
    for i in tupp:
        if i == ele :
            return f'element {i} is stored in {tupp.index(ele)} index'

print(SearchingElement(t,2))