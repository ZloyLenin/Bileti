X = float (input ("Длина стороны X: "))
Y = float (input ("Длина стороны Y: "))
Z = float (input ("Длина стороны Z: "))
 
if (X + Y > Z and Y + Z > X and X + Z > Y):
    print ("Такой треугольник существует")
    A = [X, Y, Z]
    A.sort ()
    X = A [0]
    Y = A [1]
    Z = A [2]
    if X * X + Y * Y == Z * Z :
        print ("Это треугольник прямоугольный")
        print ("Его площадь равна %.2f" %(X * Y / 2.0))
    else:
        print ("Это не прямоугольный треугольник")
  
else :
  print ("Треугольника с такими сторонами не существует")
 
 
