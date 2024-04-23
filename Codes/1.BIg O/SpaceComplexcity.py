def sum(n):
    if n<=0:
        return 0
    return n + sum(n-1)

sum(3)   # here space complexcity is O(n) because it contain n number of space 



def sum(a,b):
    print(a+b)

sum(2,3)   #here space complexcity is O(1) because this function only take one stack space for exicuting