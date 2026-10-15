#numeros
a = 5 # Esto es un numero entero
b = 5.5 # Esto es un numero decimal
c = 5 + 2j # Esto es un numero complejo
print(a)
print(b)
print(c)

print("El tipo de dato de la variable a es: " + str(type(a))) # Imprime el tipo de dato de la variable a (int)
print("El tipo de dato de la variable b es: " + str(type(b))) # Imprime el tipo de dato de la variable b (float)
print("El tipo de dato de la variable c es: " + str(type(c))) # Imprime el tipo de dato de la variable c (complex)

positivo = 5 # Esto es un numero positivo
negativo = -5 # Esto es un numero negativo

imaginaria = 5j # Esto es un numero imaginario

af = float(a) # Esto es una conversion de un numero entero a un numero decimal
print("El tipo de dato de la variable af es: " + str(type(af))) # Imprime el tipo de dato de la variable af (float)
print(af) # Imprime el valor de la variable af (5.0)

be = int(b) # Esto es una conversion de un numero decimal a un numero entero
print("El tipo de dato de la variable be es: " + str(type(be))) # Imprime el tipo de dato de la variable be (int)
print(be) # Imprime el valor de la variable be (5)

entero = 5 # Esto es un numero entero
flotante = 5.5 # Esto es un numero decimal

enteroFlotante = complex(entero) # Esto es una conversion de un numero entero a un numero complejo
flotanteComplejo = complex(flotante) # Esto es una conversion de un numero decimal a un numero complejo
print("El tipo de dato de la variable enteroFlotante es: " + str(type(enteroFlotante))) # Imprime el tipo de dato de la variable enteroFlotante (complex)
print("El tipo de dato de la variable flotanteComplejo es: " + str(type(flotanteComplejo))) # Imprime el tipo de dato de la variable flotanteComplejo (complex)

import random # Esto es una libreria que permite generar numeros aleatorios
aleatorio = random.randrange(1, 10) # Esto es un numero aleatorio entre 1 y 10
print("El numero aleatorio generado es: " + str(aleatorio)) # Imprime el numero aleatorio generado