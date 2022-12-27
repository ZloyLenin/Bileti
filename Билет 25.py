from random import randint


N = int(input("Введите количество элементов массива: "))
arr = [randint(-10, 10) for i in range(N)]
print(arr)
K = 1

for i in range(0, N):
    if arr[i] < 0:
        break
    if arr[i] >= 0:
        if arr[i] > arr[i + 1] and arr[i + 1] >= 0:
            K = 1
            break
        if arr[i] < arr[i + 1]:
                K = 2
    
if K == 1:
    print("Нет возрастающей последовательности")
elif K == 2:
    print("Возрастающая последовательность")
