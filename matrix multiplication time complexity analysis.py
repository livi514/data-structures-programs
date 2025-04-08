#The Naive Matrix Multiplication algorithm
def NaiveMatrixMultiplication(A, B):
    rows_A = len(A) #1 step
    columns_A = len(A[0]) #2 steps, retrieve A[0] and get its length
    rows_B = len(B) # 1 step
    columns_B = len(B[0]) #2 steps, retrieve B[0] and get its length

    if columns_A != rows_B: #3-4 steps (retrieving columns_A from memory, retrieving rows_B from memory, comparison, conditional branching? - depends on architecture)
        raise ValueError("Number of columns of A must equal number of rows of B")

    # Initialise the result matrix C with zeros
    # O(n * p) steps to create a n x p matrix filled with zeros
    C = [[0 for _ in range(columns_B)] for _ in range(rows_A)]

    # Naive triple loop for matrix multiplication
    for i in range(rows_A): #runs n times
        for j in range(columns_B): #runs p times
            for k in range(columns_A): #runs len(columns_A) times
                C[i][j] += A[i][k] * B[k][j] #2 steps - multiplication and addition
    
    return C # 1 step

#rough number of steps: 3n*p*m+n*p+small overhead(roughly 9-10 steps but depends on architecture)
#time complexity:  O(n^3) - we only focus on the "main" part affecting the efficiency; here, the three nested loops lead to the most inefficiency 

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[4, 3, 2], [6, 5, 4], [9, 1, 8]]

result = NaiveMatrixMultiplication(A, B)
for row in result:
    print(row)

