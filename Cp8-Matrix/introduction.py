matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [4, 5, 6]
]

matrix_2 = [
    [1, 2, 3],
    [4, 5, 6]
]


# ---------------- PRINT MATRIX ----------------
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in matrix[i]:
            print(j, end=" ")
        print()


# ---------------- UPPER TRIANGLE ----------------
def print_upper_triangle(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i <= j):
                print(matrix[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()


# ---------------- LOWER TRIANGLE ----------------
def print_lower_triangle(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i >= j):
                print(matrix[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()


# ---------------- DIAGONAL ----------------
def print_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i == j):
                print(matrix[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()


# ---------------- SQUARE TRANSPOSE ----------------
def transpose_square(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j >= i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print_matrix(matrix)

# ---------------- UNIVERSAL TRANSPOSE ----------------
def transpose_universal(matrix):
    result_matrix = []
    col = len(matrix)
    rows = len(matrix[0])

    for i in range(rows):
        result_matrix.append([0] * col)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[j][i] = matrix[i][j]

    print_matrix(result_matrix)


# ---------------- USAGE ----------------
# print("PRINT MATRIX")
# print_matrix(matrix)

# print("\nUPPER TRIANGLE")
# print_upper_triangle(matrix)

# print("\nLOWER TRIANGLE")
# print_lower_triangle(matrix)

# print("\nDIAGONAL")
# print_diagonal(matrix)

# print("\nSQUARE TRANSPOSE")
# transpose_square([row[:] for row in matrix])  # copy to avoid modifying original

# print("\nUNIVERSAL TRANSPOSE")
# transpose_universal(matrix_2)