'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

'''

def rotate(mat):
    length_matrix = len(mat)
    n=length_matrix-1
    new_matrix = [[None for _ in range(length_matrix)] for _ in range(length_matrix)]
    for i in range(length_matrix):
        for j in range(length_matrix):
            new_matrix[j][n] = mat[i][j]
            # print(f'j={j} n={n}')
        n -= 1
        # print(f'n = {n}')
    return new_matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))