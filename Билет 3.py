print("Введите количество строк: ")
A = int(input())
print("Введите строки: ")
for i in range(A) :
  S = input()
  K = S.count(' ')
  print ('В', i + 1, 'строке', K, 'пробелов')
