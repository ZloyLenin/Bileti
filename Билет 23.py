from random import randint

N = int(input("Введите количество элементов массива: "))
arr = [randint(0,9) for i in range(N)]
print(arr)
M = int(input("Введите количество исключаемых элементов: "))
K = int(input("Введите номер элемента массива: ")) 
arr[K:K+M] = []
print(arr)
