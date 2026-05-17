'''
2. নিচের nested list থেকে:
   matrix = [[1,2,3],[4,5,6],[7,8,9]]
   - Diagonal elements বের করো (1, 5, 9)
   - সব elements এর sum বের করো
   - Matrix টা transpose করো (row → column)
   '''

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# 1. Diagonal elements 

diagonal = [matrix[i][i] for i in range(len(matrix))]
print("Diagonal:", diagonal)


# 2. Sum of total
total = sum(num for row in matrix for num in row)
print("Total sum:", total)

# 3. Transpose 

transpose = [[matrix[row][col] for row in range(3)] for col in range(3)]

print("Original matrix:")
for row in matrix:
    print(row)

print("\nTranspose matrix:")
for row in transpose:
    print(row)