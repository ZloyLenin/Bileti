print("Вводите поток данных: ")
x = int(input())
maximum = x
minimum = x
while x != 0:
    if x > maximum:
        maximum = x
    if x < maximum and x < minimum:
        minimum = x
    x = int(input())
print('Максимальный элемент: ', maximum, '\nМинимальный элемент: ', minimum)
