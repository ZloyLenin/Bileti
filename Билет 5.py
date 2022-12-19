from random import randint

N = int(input("Строки: "))
M = int(input("Столбцы: "))
A = [[randint(0,1) for i in range(M)] for j in range(N)]
arr = [0 for i in range(M)]

for i in range(N):         
    for j in range(M):
        if A[i][j] == 1:
            arr[i] += 1 
        print(A[i][j], end = ' ')
    print()
    
B = [[0 for i in range(M + 1)] for j in range(N)]
for i in range(N):         
    for j in range(M + 1):
        if j < M:
            B[i][j]=A[i][j]
        else:
            if arr[i]%2!=0:
                B[i][j]=1
print()
for i in range(N):         
    for j in range(M + 1):
        print(B[i][j], end = ' ')
    print()
