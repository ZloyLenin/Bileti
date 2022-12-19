from random import randint

print("Введите количество элементов массива: ")
N = int(input())
arr = [randint(1,10) for i in range(N)]
print(arr)
print("Введите положительное число: ")
T = int(input())

for i in range(N):
    if arr[i] > 0:
        t = arr[i]/T
        arr[i] = arr[i]+t
print(arr)
