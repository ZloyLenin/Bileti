from random import randint
N = int(input("Введите количество элементов массива: "))
arr = [randint(-10,10) for i in range(N)]
print(arr)
p = 0
m = 0

for i in range(N):
    if arr[i] > 0:
        p += 1
    elif arr[i] < 0:
        m += 1
if p > m:
    for i in range(m , p):
        arr.append(-1)
elif p < m:
    for i in range(p , m):
        arr.append(1)

print("Положительных: " + str(p))
print("Отрицательных: " + str(m))
print(arr)
