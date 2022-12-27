S = int(input("Введите четырехзначное число: "))
m = [int(a) for a in str(S)]
m.pop(1)
print(m)
