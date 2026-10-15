# Tuplas: Colección ordenadas e inmutable de elementos que permiten duplicados

# indice          0         1      2       3
tecnologias = ("Python", "Java", "Go", "Python")

print(tecnologias) # Imprime lo que contenga la variable
print(tecnologias [1]) # Imprime el valor que contenga en la posición 1
print(len(tecnologias)) # Imprime la cartidad de elementos en la variable
print(type(tecnologias)) # Imprime que tipo de elementos contiene la variable (tupla)

fruta = ("Manzana") # en este ejemplo no se considera una tupla ya que si se imprime el resultado nos daria str ya que para que se conridere tupla despues de los "" debe haber una ,
print(type(fruta))

tupla = ("Python", 5, True) # En este ejemplo tenemos diferentes tipos de elemento
print(tupla) #Imprime lo que contiene la variable
print(type(tupla)) # Imprime como resultado "tuple"

# Para dividir el contenido de la variable y asignarselo a otra variable se puede resolver asi:
x, y, z = tupla # El valor de cada variable se determina en la posicion del indice de la tupla ya definida
print(x) # Imprime Python
print (y) # Imprime 5
print(z) # Imprime True

# Si queremos unificar el valos de varias tuplas lo podemos resolver asi:

tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)
tupla3 = tupla1 + tupla2

print(tupla3) # Imprime la unificacón de los elementos de las variables tupla 1 + tupla 2 sin importar si tenemos datos duplicados

# Para duplicar los datos de una tupla se puede hacer asi:

tupla = ("Python", 5, True)
print(tupla * 2) # Imprime los elementos 2 veces

# Tambien se puede colocar los elementos en forma de lista

for item in tupla:
    print(item) 

# Una tupla no es modificable, pero hay una forma de hacerlo, si convertimos una tupla en lista y modificamos esa lista para volverta despues tupla, es la forma de hacerlo

tuplaAModificar = ("Python", "Java", "HTML")
listaComodin = list(tuplaAModificar) # convertimos o  hacemos un casteo de una tupla en lista se identifica cuando imprimimos y el resultado esta dentro de []
listaComodin.append("CSS") # agregamos CSS dentro de la lista
tuplaAModificar = tuple(listaComodin) # convertimos o casteamos la lista en tupla nuevamente
print(tuplaAModificar) # Imprime como tesultado una tupla con la adición del elemento CSS
print(type(tuplaAModificar)) # Imprime como resultado tupla confirmado que volvimos al valor inicial de la variable