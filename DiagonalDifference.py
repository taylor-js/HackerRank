def diagonalDifference(arr):
    # Write your code here
    diag1 = []
    diag2 = []
    n = len(arr)-1
    for i in range(len(arr)): 
        diag1.append(arr[i][i])
        diag2.append(arr[n-i][i])
    return abs(sum(diag1) - sum(diag2))

matrix = [[1, 2, 3],
          [4, 5, 6],
          [9, 8, 9]]

print(diagonalDifference(matrix))