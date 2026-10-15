v = True
f = False

print(v) # Imprime True por que es un valor booleano
print(f) # Imprime False por que es un valor booleano

print(5 > 3) # Imprime True por que 5 es mayor que 3
print(3 > 5) # Imprime False por que 3 no es mayor que 5

print(type(v)) # Imprime <class 'bool'> por que es un valor booleano

print(bool("Hola")) # Imprime True por que es un string diferente de vacio
print(bool("")) # Imprime False por que es un string vacio
print(bool(0)) # Imprime False por que es un numero entero igual a cero
print(bool(5)) # Imprime True por que es un numero entero diferente de cero

# True

print(bool(5564889793)) # Imprime True por que es un numero entero diferente de cero
print(bool(-5564889793)) # Imprime True por que es un numero entero diferente de cero
print(bool("Hola")) # Imprime True por que es un string diferente de vacio
print(bool([1, 2, 3])) # Imprime True por que es una lista diferente de vacio
print(bool((1, 2, 3))) # Imprime True por que es una tupla diferente de vacio
print(bool({"a": 1, "b": 2})) # Imprime True por que es un diccionario diferente de vacio
print(bool(["manzana", "Pera", "uva"])) # Imprime True por que es una lista diferente de vacio
x = 123456
print(isinstance(x, int)) # Imprime True por que es un numero entero

# false

print(bool(None)) # Imprime False por que es un valor nulo
print(bool("") ) # Imprime False por que es un string vacio
print(bool(0)) # Imprime False por que es un numero entero igual a cero
print(bool([])) # Imprime False por que es una lista vacia
x = 1.23456
print(isinstance(x, int)) # Imprime False por que es un numero decimal
