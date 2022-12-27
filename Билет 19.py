X = int(input("Число X: "))

a = int(input("Начло промежутка(a): "))
b = int(input("Конец промежутка(b): "))
if b > a:
    print("[a, b] =" + "[ " + str(a) + ", " + str(b) + " ]")
    if a <= X and X <= b:
        print("Пренадлежит")
    elif a > X or X > b:
        print("Не пренадлежит")
elif a > b:
    print("Неккоректный ввод")
