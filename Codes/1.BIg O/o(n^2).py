'''
in below example we can see that there is a nested loop inside and also other nested loop inside it it means we assume n*n*n = n^3 time complexcity is O(n^3) ; but here we always type O(n^2) every time in any condition like this also for 4 loops or any number
'''

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
        
print_items(2)