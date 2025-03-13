'''
differnce between array and list
1. array can store only one type of data
2. array is faster than list
3. array is not dynamic
4. array is not flexible
5. in list we can store multiple type of data
6. in list we cannot perform mathematical operations in this case array are so usefull
7. list is dynamic
'''

a = [1,2,"helo",3.4,[{1,2,3},{"key":"value"}]]

# to remove the element we use pop function (we and not remove slice of elements)
a.pop() #it will remove the last element
a.pop(2) #it will remove the element at index 2
print(a.pop(1)) # it will remove and return the element at index 1

# also use remove function and del function

del a[1] # it will remove the element at index 1
del a[1:3] # it will remove the element from index 1 to 3

a.remove(3.4) # here we give the value to remove not index