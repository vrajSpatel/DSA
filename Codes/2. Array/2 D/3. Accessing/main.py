import numpy as np

'''
notes :
  -to find the length of the array's dimension, use the shape attribute and the len() function 
     shape : in shape attribute, the first element is the number of rows and the second element is the number of columns
     len() : in len() function, the first element is the number of rows and the second element is the number of columns
        len(arr) : number of rows
        len(arr[0]) : number of columns
  
'''

# Creating a 2D array
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# len() function
# print(len(arr)) # number of rows
# print(len(arr[0])) # number of columns

# shape attribute
# print(arr.shape)  # (3,3) : 3 rows and 3 columns
# print(arr.shape[0]) # number of rows
# print(arr.shape[1]) # number of columns

def access2DArray(arr,row,col):
    if row >= arr.shape[0] or col >= arr.shape[1]:
        return "Invalid index"
    # print(arr[row][col])
    return arr[row][col]

# access2DArray(arr,1,1)
ele = access2DArray(arr,1,1)
print(ele)