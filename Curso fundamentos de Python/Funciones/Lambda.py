# Lambda es una función anónima, es decir, una función sin nombre. Se utiliza para crear funciones pequeñas y de una sola línea. La sintaxis básica de una función lambda es la siguiente:

# lambda argumentos: expresión

x = lambda a : a + 10 # Esta función lambda toma un argumento a, y devuelve su suma con 10

print(x(5)) # Llamada a la función lambda, se imprimira 15

y = lambda a, b : a * b # Esta función lambda toma dos argumentos a y b, y devuelve su multiplicación
print(y(5, 6)) # Llamada a la función lambda, se imprimira 30

def miFuncion(n): # Esta función toma un argumento n, y devuelve una función lambda que multiplica su argumento por n
    return lambda a : a * n

duplicar = miFuncion(2) # Llamada a la función miFuncion con el argumento 2, que devuelve una función lambda que multiplica su argumento por 2
triplicar = miFuncion(3) # Llamada a la función miFuncion con el argumento 3, que devuelve una función lambda que multiplica su argumento por 3
quituple = miFuncion(5) # Llamada a la función miFuncion con el argumento 5, que devuelve una función lambda que multiplica su argumento por 5

print(duplicar(5)) # Llamada a la función lambda devuelta por miFuncion, se imprimira 10
print(triplicar(5)) # Llamada a la función lambda devuelta por miFuncion, se imprimira 15
print(quituple(5)) # Llamada a la función lambda devuelta por miFuncion, se imprimira 25

