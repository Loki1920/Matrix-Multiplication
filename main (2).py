#matrix multiplication
r1 = [1, 2, 3]
r2 = [4, 5, 6]
r3 = [7, 8, 9]

s1 = [1, 2, 1]
s2 = [6, 2, 3]
s3 = [4, 2, 1]

A = []
B = []

A.append(r1)
A.append(r2)
A.append(r3)

A.append(s1)
A.append(s2)
A.append(s3)

C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

dim = 3
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]
            
print(C)
