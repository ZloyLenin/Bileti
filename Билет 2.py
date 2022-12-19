print("Введите количество строк символов: ")
M = int(input())
print("Введите строки: ")
arr = [0 for i in range(M)]

for i in range(M):
    arr[i]=input()
print(arr)
print("Количество символов в самой длинной строке:"+str(len(max(arr))))
K = len(arr[0])
for i in range(M):
    if (len(arr[i]) > K):
           K = len(arr[i])
for i in range(M):
    N=K-len(arr[i])
    print("*" * N + str(arr[i]))
