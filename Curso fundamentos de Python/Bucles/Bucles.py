# Bucles es un concepto fundamental en la programación que permite ejecutar un bloque de código repetidamente mientras se cumpla una condición específica. 
# En Python, existen varios tipos de bucles, siendo los más comunes el bucle "for" y el bucle "while".


# while es un bucle que se ejecuta mientras una condición sea verdadera. La sintaxis básica de un bucle while es la siguiente:

i = 1 # Esto es una variable que se utiliza como contador para el bucle while
while i <= 5: # Esto es un bucle while que se ejecuta mientras la condición i <= 5 sea verdadera
    print(i) # Imprime el valor de la variable i en cada iteración del bucle
    i += 1 # Incrementa el valor de la variable i en 1 en cada iteración del bucle

while i <= 10 : # Esto es un bucle while que se ejecuta indefinidamente hasta que se cumpla una condición de salida
    print(i) # Imprime el valor de la variable i en cada iteración del bucle
    i += 1 # Incrementa el valor de la variable i en 1 en cada iteración del bucle
    if i == 8: # Esto es una condición que se evalúa en cada iteración del bucle
        break # Esto es una instrucción que detiene la ejecución del bucle cuando se cumple la condición if



# For es un bucle que se ejecuta un número determinado de veces. La sintaxis básica de un bucle for es la siguiente:

Palabra = "Python" # Esto es una variable que contiene una cadena de texto
for letra in Palabra: # Esto es un bucle for que se ejecuta una vez por cada letra en la cadena de texto contenida en la variable Palabra
    print(letra) # Imprime cada letra de la cadena de texto en cada iteración del bucle

frutas = ["manzana", "banana", "cereza"] # Esto es una lista que contiene tres elementos
for fruta in frutas: # Esto es un bucle for que se ejecuta una vez por cada elemento en la lista contenida en la variable frutas
    print(fruta) # Imprime cada elemento de la lista en cada iteración del bucle

frutas = ["manzana", "banana", "cereza"] # Esto es una lista que contiene tres elementos
for fruta in frutas: # Esto es un bucle for que se ejecuta una vez por cada elemento en la lista contenida en la variable frutas
    if fruta == "banana": # Esto es una condición que se evalúa en cada iteración del bucle
        continue # Esto es una instrucción que salta a la siguiente iteración del bucle cuando se cumple la condición if
    print(fruta) # Imprime cada elemento de la lista en cada iteración del bucle
else: # Esto es una instrucción que se ejecuta cuando el bucle for termina de ejecutarse
    print("No hay más frutas") # Imprime un mensaje indicando que no hay más elementos


# ejemplos de rangos

for i in range(10): # Esto es un bucle que contiene los números de 0 a 9
    print(i) # Imprime los números contenidos

for i in range(3,5): 
    print(i)

Adjetivos = ["Rica", "Saludable"]
frutas = ["Manzana", "Naranja", "Kiwi"]

for fruta in frutas:
    for adjetivo in Adjetivos:
        print(fruta, adjetivo)