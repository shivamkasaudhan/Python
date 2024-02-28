# Input matrix dimensions
rows_A = int(input("Enter the number of rows of matrix A: "))
cols_A = int(input("Enter the number of columns of matrix A: "))
rows_B = int(input("Enter the number of rows of matrix B: "))
cols_B = int(input("Enter the number of columns of matrix B: "))

# Check if multiplication is possible
if cols_A != rows_B:
    print("Matrix multiplication is not possible!")
else:
    # Input elements of matrix A
    print("Enter elements of matrix A:")
    matrix_A = []
    for i in range(rows_A):
        row = []
        for j in range(cols_A):
            row.append(int(input(f"Enter element A[{i}][{j}]: ")))
        matrix_A.append(row)
    
    # Input elements of matrix B
    print("Enter elements of matrix B:")
    matrix_B = []
    for i in range(rows_B):
        row = []
        for j in range(cols_B):
            row.append(int(input(f"Enter element B[{i}][{j}]: ")))
        matrix_B.append(row)
    
    # Perform matrix multiplication
    matrix_C = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            element = 0
            for k in range(cols_A):
                element += matrix_A[i][k] * matrix_B[k][j]
            row.append(element)
        matrix_C.append(row)
    
    # Print the result
    print("Resultant matrix C (A * B):")
    for row in matrix_C:
        print(row)
