from random import randint
N = int(input("Размер массива: "))
arr = [randint(0,9) for i in range(N)]
print(arr)

for i in range(N):
    if arr[i] == 0:
        arr[i] = []


print(arr)
