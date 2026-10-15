# conjuntos (set): Colección NO ordenada de elementos únicos quita los duplicados (no se puede acceder por indice) se identifica por {}

frutas = {"Manzana", "Naranja", "Uvas", "Manzana"}
print(frutas) # Imprime los elementos de la variable
print(type(frutas)) # Imprime el tipo (set) conjunto
print(len(frutas)) # Imprime la cantidad de elementos quitando los duplicados, para este ejemplo 3 de los 4 por el duplicado Manzana

# Para validar si un elemento esta dentro del conjunto es con IN y para saber si no es con NOT

print("manzana" in frutas)
print("pera" not in frutas)

# Agregar elementos
# add() agrega un elemento al conjunto, si el elemento ya existe no lo agrega y no da error
frutas.add("Pera")
print(frutas)

# update() agrega varios elementos al conjunto, si el elemento ya existe no lo agrega y no da error
frutasTropicales = {"Mango", "Piña", "Durazno"}
frutas.update(frutasTropicales) # el update tambien puede agregar elementos de una lista, tupla, conjuntos o diccionario
print(frutas)

# Eliminar elementos
# remove() elimina un elemento del conjunto, si el elemento no existe da error
frutas.remove("Naranja")
# discard() elimina un elemento del conjunto, si el elemento no existe no da error
frutas.discard("Uvas")
# pop() elimina un elemento aleatorio del conjunto, si el conjunto esta vacio da error
frutas.pop()
# clear() elimina todos los elementos del conjunto
frutas.clear()

'''conjuntos = {"Python", 85, True, 85, "Java"}
print(conjuntos)
print(type(conjuntos))

# para recorres los elementos existentes podemos hacerlo asi:

for item in conjuntos:
    print(item) # Imprime los elementos tipo lista uno debajo de otro'''

print ("------------------------------------------------------------------------------------")

a = {"a", "b", "c"}
b = {"c", "d", "e"}

c = a.union(b) # union() une los elementos de dos conjuntos y devuelve un nuevo conjunto
print(c)

i = a.intersection(b) # intersection() devuelve un nuevo conjunto con los elementos que se repiten en ambos conjuntos
print(i)

d = a.difference(b) # difference() devuelve un nuevo conjunto con los elementos que no se repiten en ambos conjuntos
print(d)

