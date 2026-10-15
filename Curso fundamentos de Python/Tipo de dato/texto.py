print("Hola, 'Mundo!'") # Imprime Hola, 'Mundo!'

ingles = "Hello, 'World!'" # Imprime Hello, 'World!'
multiples = """Hola,
desde
las
comillas
simples""" # Imprime el texto con múltiples líneas

print(ingles)
print(multiples)

palabra = "estetoscopio" # Imprime la palabra estetoscopio
print(len(palabra)) # (len) Imprime la cantidad de caracteres de la palabra

texto = "Hola, desde la variable texto en Python" # Imprime el texto
estaIncluida = "Python" in texto # (in) Verifica si la palabra Python esta incluida en la variable texto
noEstaIncluida = "Java" not in texto # (not in) Verifica si la palabra Java no esta incluida en la variable texto
print(estaIncluida) # Imprime True si la palabra esta incluida en la variable
print(noEstaIncluida) # Imprime True si la palabra no esta incluida en la variable

mayuscula = texto # Imprime el texto en mayuscula
print(mayuscula.upper()) # (upper) Imprime el texto en mayuscula

minuscula = texto # Imprime el texto en minuscula
print(minuscula.lower()) # (lower) Imprime el texto en minuscula

espacios = "   Hola, desde la variable espacios en Python   " # Imprime el texto con espacios al inicio y al final
print(espacios.strip()) # (strip) Imprime el texto sin los espacios al inicio y al final

# indice son la cantidad de caracteres que tiene la palabra, el primer caracter es el indice 0, el segundo es el indice 1 y asi sucesivamente
texto2 = "Hola, desde la variable texto2 en Java" # Imprime el texto
print(texto2[0:5]) # Imprime el primer caracter de la variable texto2 (Hola,) y el segundo caracter (desde) y el tercer caracter (la) y el cuarto caracter (variable) y el quinto caracter (texto2) y el sexto caracter (en) y el septimo caracter (Python)
print(texto2[ :20]) # Imprime los primeros 20 caracteres de la variable texto2 (Hola, desde la variab)
print(texto2[20: ]) # Imprime los caracteres desde el indice 20 hasta el final de la variable texto2 (le texto2 en Python)
print(texto2[-6: ]) # Imprime los ultimos 6 caracteres de la variable texto2 (Python)

#remplazar
texto2 = texto2.replace("Java", "Python") # (replace) Reemplaza la palabra Java por Python en la variable texto2
print(texto2) # Imprime el texto con la palabra Python en lugar de Java

#texto dividido
texto3 = "Hola, desde la variable texto3 en Python" # Imprime el texto
print(texto3.split(",")) # (split) Divide el texto en una lista de cadenas usando la coma como separador

#normalizar texto
texto4 = "Hola, desde la variable texto4 en Python" # Imprime el texto
print(texto4.strip()) # (strip) Imprime el texto sin los espacios al inicio y al final

#primera letra en mayuscula
texto5 = "hola, desde la variable texto5 en Python" # Imprime el texto
print(texto5.capitalize()) # (capitalize) Imprime el texto con la primera letra en mayuscula

#primera letra en minuscula
texto6 = "HOLA, DESDE LA VARIABLE TEXTO6 EN PYTHON" # Imprime el texto
print(texto6.lower()) # (lower) Imprime el texto con todas las letras en minuscula