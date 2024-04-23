""" 
    -in below example we can see that there is a nested loop and also a loop 
    -here we count like --> n^2 + n 
    -but here we drop the non dominent term for calclutate the real time complexcity
    -so here dominent term is n^2 so all of the other are going to be removed.
    -so real time complexcity is O(n^2)
    
"""


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
        
print_items(2)