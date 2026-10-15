# listas son ordenadas, modificables y permiten valores duplicados se identifica cuando se asigna o empieva el valor de la variable con []

# indices:    0         1           2
Frutas = ["Manzana", "Naranja", "Mandarina"]
print(Frutas) # Imprime las frutas que se asignaron en la lista
print(type(Frutas)) # Se imprime el tipo, en este caso es una lista
print(type(Frutas[1])) # Imprime la posición 1 según se le indico [1] como se ve en el indice

Frutas[1] = "Banana" # Cambia de la lista en la posición 1 de Naranja a Banana
print(Frutas) # Imprime la lista con la modificacion de Banana

Lista = ["Python", 5, True] # es una lista donde puede contenel Texto, Números o Booleanos
print(list) # Imprime lo que contiene la lista
print(type) # Imprime el tipo, para el ejemplo es una lista

print(len(Frutas)) # Imprime la cantidad de elementos (3) que hay en la lista de frutas
print(len(Lista)) # Imprime la cantidad de elementos (3) que hay en la variable Lista

print(Frutas[:2]) # Imprime un rango seleccionadodeacuerdo a lo que coloquemos en el [], para el ejemplo desde el inicio hasta la posición 1 ya que el 2 no cuenta
print(Lista[1:3]) # Imprime el rango desde la posicion 1 hasta la 2 ya que la posicion no cuenta
print(Frutas[1:]) # Imprime los elementos de la lista desde la posicion 1 en adelante la posición 0 no la imprimiria

# para saber si un rango existe dentro de la lista o no!!!

if "Manzana" in Frutas: # Aca lo que realiza el codigo es buscar dentro de la lista que se encuentra dentro de la variable si existe la palabra Manzana
    print("La Manzana esta dentro de las frutas") # Si se cumple la condición de imprimira el mensaje escrito

# Metodos para modificar listas

# Indices       0       1        2           3
Vehiculos = ["Carro", "Moto", "Avión", "Bicicleta"]

# Append (Agrega un elemento al final de la lista)
Vehiculos.append("Barco") # Se agregara a la lista de Vehiculos el Barco
print(Vehiculos) # Imprime la lista completa con la adición del barco

# Insert (Agrega un elemento pero en la posición que le indiquemos)
Vehiculos.insert(1, "Patineta") # Se inserta Patineta en la posicion 1 y desplaza la lista desde Moto en adelante manteniendo a Carro en la posición 0
print(Vehiculos) # Imprime la lista completa con las modificación de la Patineta en la posición 1 

# Remove
Vehiculos.remove("Patineta") # Como lo dice la palabra quita o remueve de la lista el elemento indicado en este caso Patineta
print(Vehiculos) # Imprime la lista completa sin el elemento Patineta

# pop
Vehiculos.pop(4) # Elimina un item de la lista según la posición indicada, para este ejemplo quitara la posicion 4 (Barco)
print(Vehiculos) # Imprime la lista la lista original que teniamos definido en la variable inicial

# sort
Vehiculos.sort() # Organiza todos los items de la lista en orden alfabetico
print(Vehiculos) # Imprime en orden alfabetico la lista de item de la variable definida

# reverse
Vehiculos.reverse() # organiza todos los items de la lista de forma invertida alfabeticamente
print(Vehiculos) # Imprime la lista invertida alfabeticamente

# Unir listas
numeros1 = [1,2,3] 
numeros2 = [4,5,6]

numeros3 = numeros1 + numeros2 # Toma los valores de la lista 1 y la lista 2 y la concatena con el simbolo + para crear la lista de valores unificados en numeros3
print(numeros3) # Imprime la lista de los valores de numeros1 y numeron 2 en una lista nueva llamada numeros3

# Extend
numeros1.extend(numeros2) # Para este ejemplo tomamos los elementos de numeros2 y lo unificamos en numeros 1, asi no tendriamos que crear numero3 
print(numeros1) # Imprime la nueva lista de elementos de numeros1 añadiendo la lista de numeros2