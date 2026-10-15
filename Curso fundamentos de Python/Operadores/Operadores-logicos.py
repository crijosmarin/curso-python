# Operadores de comparacion

x = 5
y = 10
z = 5

print(x == y)  # Imprime False porque 5 no es igual a 10
print(x == z)  # Imprime True porque 5 es igual a 5
print(x != y)  # Imprime True porque 5 no es diferente de 10
print(x != z)  # Imprime False porque 5 no es diferente de 5
print(x < y)   # Imprime True porque 5 es menor que 10
print(x > y)   # Imprime False porque 5 no es mayor que 10
print(x <= z)  # Imprime True porque 5 es menor o igual a 5
print(x >= z)  # Imprime True porque 5 es mayor o igual a 5

# Operadores logicos

print(x < y and x == z)  # Imprime True porque ambas condiciones son verdaderas
print(x < y or x != z)   # Imprime True porque al menos una condición es verdadera
print(not(x < y))        # Imprime False porque la condición es verdadera y se niega con not