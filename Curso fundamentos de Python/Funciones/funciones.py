# Funciones en Python : es un bloque de código que se puede reutilizar, se puede llamar desde cualquier parte del programa y puede recibir parámetros y devolver valores.

def mi_funcion():
    print("Hola, soy una función sin parámetros y sin valor de retorno")

mi_funcion() # Llamada a la función, se imprimera las cantidad de veces que sea llamada sin limites

def saludar(nombre):
    print(f"Hola {nombre}, soy una función con parámetros y sin valor de retorno") # f es una forma de formatear cadenas de texto, permite insertar variables dentro de la cadena

saludar("Sara") # Llamada a la función con un argumento
saludar("Josue") # Llamada a la función con un argumento

def numeros(a, b):
    return a + b, a - b, a * b, a / b # return devuelve un valor, en este caso la suma, la resta, la multiplicación y la división de a y b

resultado = numeros(5, 3) # Llamada a la función con dos argumentos comensando desde una variable llamada resultado, que almacenara el valor retornado por la función numeros, que es una tupla con los cuatro valores retornados por la función
print(resultado) # Imprime el valor retornado por la función

def lugar(ciudad, departamento, pais = "Colombia"): # Parámetro con valor por defecto, si no se pasa un valor para pais, se usará "Colombia"
    print("Estoy en la ciudad de " + ciudad + ", departamento de " + departamento + ", país de " + pais) # Concatenación de cadenas de texto

lugar("Medellin", "Antioquia") # Llamada a la función con dos argumentos, pais tomara el valor por defecto "Colombia"
lugar("lima", "quito", "ecuador") # Llamada a la función con tres argumentos, pais tomara el valor que se le asigno "ecuador"
