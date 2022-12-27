b = "[X]"
def y(x, y):
    a[x-2][y-1] = b
    a[x-1][y-2] = b
    a[x+1][y+2] = b
    a[x+2][y+1] = b
    a[x-2][y+1] = b 
    a[x-1][y+2] = b
    a[x+2][y-1] = b
    a[x+1][y-2] = b
a = []
for i in range(8):         
    for j in range(8):
        a.append(["[ ]"]*8) 
        print(a[i][j], end = ' ')
    print()
    
x1 = int(input("x Первого коня: "))-1
y1 = int(input("y Первого коня: "))-1
y(x1,y1)
a[x1][y1] = "[K]"
for i in range(8):         
    for j in range(8):
        a.append(["[ ]"]*8) 
        print(a[i][j], end = ' ')
    print()
x2 = int(input("x Второго коня: "))-1
y2 = int(input("y Второго коня: "))-1
y(x2,y2)
if a[x1][y1] == b:
    print("Минус кони")
    a[x1][y1] = "[K]"
else:
    print("А вот нет")
a[x2][y2] = "[K]"
for i in range(8):         
    for j in range(8):
        print(a[i][j], end = ' ')
    print()
