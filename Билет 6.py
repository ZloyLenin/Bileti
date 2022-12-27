from random import randint

N = int(input("Размер матрицы: "))
Sg = 0
Sp = 0
A = [[randint(1,10) for i in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        print(A[i][j], end = ' ')
    print()
for i in range(A[i][i]):
    Sg = Sg + i
print("Суммая главной диагонали: ", Sg)
