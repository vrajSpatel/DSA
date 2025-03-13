# here we have to delete a row or a column , we cannot delete a single element form the matrix(2D array)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

new_arr = np.delete(arr,1,axis=0) #array , index , axis
print(new_arr)