import numpy as np

# insert and append are used to add elements in the array
# append is used to add elements at the end of the array
# insert is used to add elements at a specific index

# Creating a 2D array
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

newarr = np.insert(arr,1,5 , axis=0) # insert 5 at index 1 row wise all value will be 5
print(newarr)

arr2 = np.insert(arr,0,[11,12,13], axis=1) # insert 11,12,13 at index 0 column wise
print(arr2)

arr3 = np.insert(arr,0,[1,2,22],axis=1)
print(arr3)

print(np.append(arr,[[1,2,3]], axis=0))
#here we need to add a 2D array so we need to add double square brackets