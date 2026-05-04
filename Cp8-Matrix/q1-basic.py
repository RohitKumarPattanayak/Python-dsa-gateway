import introduction
# Set matrix Zero wherever you find a zero the entire row and column

matrix = [
    [4, 6, 6,9],
    [1, 2, 0,4],
    [4, 0, 6,3],
    [4, 6, 6,9]
]

# attempt-1
# def setZeroes(matrix):
#     col_set = set()
#     row_set = set()

#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 0:
#                 col_set.add(j)
#                 row_set.add(i)

#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if i in row_set or j in col_set:
#                 matrix[i][j] = 0    

# setZeroes(matrix)
# introduction.print_matrix(matrix)