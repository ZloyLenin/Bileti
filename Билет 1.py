from random import randint

print("Введите количество элементов массива: ")
N = int(input())
A = [randint(0, 10) for i in range(N)]
print(A)
X = A.pop(-1)
A.insert(0,X)
print(A)
