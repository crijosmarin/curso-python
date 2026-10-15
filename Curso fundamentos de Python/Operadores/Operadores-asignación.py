# operadores asignación

x = 5 # Asignación de valor a la variable x
y = 3 # Asignación de valor a la variable y

x += y # Suma el valor de y a x y asigna el resultado a x
print("Suma:", x) # Imprime 8 por que es la suma de 5 y 3

x -= y # Resta el valor de y a x y asigna el resultado a x
print("Resta:", x) # Imprime 5 por que es la resta de 8 y 3

x *= y # Multiplica el valor de y por x y asigna el resultado a x
print("Multiplicación:", x) # Imprime 15 por que es la multiplicación de 5 y 3

x /= y # Divide el valor de x entre y y asigna el resultado a x
print("División:", x) # Imprime 5.0 por que es la división de 15 y 3

x %= y # Calcula el residuo de la división de x entre y y asigna el resultado a x
print("Módulo:", x) # Imprime 2.0 por que es el residuo de la división de 5.0 entre 3

y //= 2 # Divide el valor de y entre 2 y asigna el resultado a y
print("División entera:", y) # Imprime 1 por que es la división entera de 3 entre 2

y **= 2 # Eleva el valor de y a la potencia de 2 y asigna el resultado a y
print("Exponente:", y) # Imprime 1 por que es el exponente de 1 a la potencia de 2

#walrus operator
# El operador walrus (:=) permite asignar un valor a una variable como parte de una expresión. Esto puede ser útil para reducir la cantidad de líneas de código y mejorar la legibilidad.
if (n := len("Hola")) > 3: # Asigna el valor de la longitud de la cadena "Hola" a la variable n y luego compara si n es mayor que 3
    print(f"La longitud de la cadena es {n}, que es mayor que 3") # Imprime La longitud de la cadena es 4, que es mayor que 3

#z := 10 # Asignación de valor a la variable z
#print(z) # Imprime 10 por que es el valor asignado a la variable z
pass