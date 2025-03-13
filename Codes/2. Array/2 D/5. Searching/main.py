import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# len(arr[0]) because here cols and rows are same length (3 * 3) so this will find the length of first row which is same as cols

def Search(arr, x):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==x:
                return "The indexes are "+ str(i)+ " " + str(j)
    return "NOt found"

print(Search(arr,5))
