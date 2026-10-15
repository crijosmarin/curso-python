# Condicionales if elif else

x = 5
y = 2


if x > y: # solo da un resultado cuando se cumpla la regla de que 5 es mayor que 2
    print("x es mayor que y")

if x < y: # no da ningun resultado porque la regla no se cumple
    print("x es menor que y")

elif x == y: # no da ningun resultado porque la regla no se cumple
    print("x es igual a y")

else: # da un resultado cuando ninguna de las condiciones anteriores se cumple
    print("ninguna de las condiciones se cumple")


a = "Python"
b = "Java"
c = "Python"

if a == c: # no da ningun resultado porque la regla no se cumple
    if a != b: # da un resultado porque la regla se cumple
        print("a es igual a c pero a es diferente de b")
    else: # no da ningun resultado porque la regla no se cumple
        print("ninguna de las condiciones se cumple saliendo del if anidado o interno")

elif a == c: # da un resultado porque la regla se cumple
    print("a es igual a c")
else: # no da ningun resultado porque la regla no se cumple
    print("ninguna de las condiciones se cumple")


e = 10
f = 10

if e == f: # da un resultado porque la regla se cumple
    pass # no hace nada pero permite que el programa continue ejecutandose sin errores