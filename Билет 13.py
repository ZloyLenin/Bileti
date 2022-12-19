from random import randint

print("Введите количество элементов массива: ")
N = int(input())
A = 0
B = 0
arr = [randint(-10, 10) for i in range(N)]
print(arr)
for i in range(N):
    A += arr[i]
    if arr[i] > 0:
        B = B + 1      
arr.insert(0,A)
arr.insert(1,B)
print(arr)
