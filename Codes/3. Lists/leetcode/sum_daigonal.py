def diagonal_sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i][i];
    return sum


myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(myList2D))