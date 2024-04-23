""" 
in O(n) complexcity there is many loops or function to run like in lower example there is 2 loops then it is like n+n = 2n then the time complexcity is O(2n) 

but in Big O we say O(n) = O(2n) or any consant like 3287n , here we drop the constant and complexcity is O(n)

--> reason:
    -it is very possible that in some case O(n) is faster than O(1) for some specific inputs
    -different computer with different acrhitecture have different consant factors.
        - faster computer have faster memory access then slower computer. 
    -as soon as n -> infinite then consant factors are not big deal.   
"""

def print_items(n):
    for i in range(n):
        print(i+1)
    for j in range(n):
        print(j)
        
print_items(15)