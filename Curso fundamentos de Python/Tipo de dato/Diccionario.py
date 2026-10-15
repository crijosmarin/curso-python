# Colección de elementos ordenados, mutables y que permite duplicados (se puede acceder por indice) se identifica por [] (Ordenado a partir de la version 3.7 de Python, antes no era ordenado)

auto = {"marca": "Toyota",
        "modelo": "Corolla",
        "año": 2020,
        "color": "Rojo",}

print(auto) # Imprime los elementos de la variable
print(type(auto)) # Imprime el tipo (dict) diccionario
print(auto["marca"]) # Imprime el valor de la clave "marca"
print(auto["modelo"]) # Imprime el valor de la clave "modelo"
print(auto["año"]) # Imprime el valor de la clave "año"
print(auto["color"]) # Imprime el valor de la clave "color"
print(auto.get("marca")) # Imprime el valor de la clave "marca" con el metodo get()
print(auto.keys()) # Imprime las claves del diccionario
print(auto.values()) # Imprime los valores del diccionario

if "marca" in auto: # Valida si la clave "marca" existe en el diccionario, debe ser escrita tal cual la clave, si no existe devuelve False
    print("La clave 'marca' existe en el diccionario")

auto ["año"] = 2021 # Modifica el valor de la clave "año"
auto ["color"] = "Azul" # Modifica el valor de la clave "color"
print(auto) # Imprime los elementos de la variable

auto["transmision"] = "Automatica" # Agrega una nueva clave y valor al diccionario
print(auto) # Imprime los elementos de la variable

auto.update({"puertas": 4}) # Agrega varias claves y valores al diccionario
auto.update({"año": 2022}) # Modifica el valor de la clave "año"
auto.update({"color": "Negro", "transmision": "Manual"}) # Modifica el valor de la clave "color" y agrega una nueva clave y valor
print(auto) # Imprime los elementos de la variable

# auto.pop("transmision") # Elimina la clave y valor del diccionario
# auto.popitem() # Elimina la ultima clave y valor del diccionario
# del auto["puertas"] # Elimina la clave y valor del diccionario
# print(auto) # Imprime los elementos de la variable

# auto.clear() # Elimina todos los elementos del diccionario
# print(auto) # Imprime los elementos de la variable

for K in auto: # Recorre las claves del diccionario
    print(K) # Imprime las claves del diccionario
print("------------------------------------------------------------------------------------")
for V in auto.values(): # Recorre los valores del diccionario
    print(V) # Imprime los valores del diccionario
print("------------------------------------------------------------------------------------")
for K, V in auto.items(): # Recorre las claves y valores del diccionario
    print(K, V) # Imprime las claves y valores del diccionario

# Diccionarios anidados (diccionarios dentro de diccionarios)

familia = [
    {
        "padre": {
        "nombre": "Cristian",
        "edad": 41,
        "profesion": "Ingeniero"
        }
    },
    {
        "madre": {
        "nombre": "Luisa",
        "edad": 32,
        "profesion": "Enfermera"
        },
        "hijos": {
        "hijo1" : {
        "nombre": "Sara",
        "edad": 16
        },
        "hijo2" : {
        "nombre": "Josue",
        "edad": 11
        },
        "hijo3" : {
        "nombre": "Majo",
        "edad": 4
        }
        }
    }
]

print(familia) # Imprime los elementos de la variable
print(familia[1]["hijos"]["hijo3"]["nombre"]) # Imprime los elementos de la variable
