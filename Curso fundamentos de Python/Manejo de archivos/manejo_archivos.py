
# open(nombre, modo) # Abre un archivo con el nombre y modo especificados. El modo puede ser 'r' para lectura, 'w' para escritura, 'a' para agregar contenido al final del archivo, entre otros.

# R (Read): Abre un archivo para lectura. Si el archivo no existe, se generará un error.
# W (Write): Abre un archivo para escritura. Si el archivo no existe, se creará uno nuevo. Si el archivo ya existe, se sobrescribirá su contenido.
# A (Append): Abre un archivo para agregar contenido al final del archivo. Si el archivo no existe, se creará uno nuevo.

try:
    with open("archivo.txt", "r", encoding="utf-8") as f: # Abre el archivo "archivo.txt" en modo lectura y con codificación UTF-8. El bloque with asegura que el archivo se cierre automáticamente al finalizar.
        print(f.readline()) # Lee la primera línea del archivo y la imprime en la consola.
except FileNotFoundError: # Captura la excepción FileNotFoundError si el archivo no
        print(f.readline()) # Lee la primera línea del archivo y la imprime en la consola.
except FileNotFoundError: # Captura la excepción FileNotFoundError si el archivo no existe y ejecuta el bloque de código dentro del except.
    open("archivo.txt", "x") # Crea un archivo nuevo con el nombre "archivo.txt" si no existe. El modo 'x' se utiliza para crear un archivo nuevo y generará un error si el archivo ya existe.
    print("No se ha encontrado el archivo") # Imprime un mensaje indicando que el archivo no se ha encontrado.

# En la anterior lineas de codigo crea el archivo .txt si no existe y luego imprime un mensaje indicando que el archivo no se ha encontrado. Si el archivo ya existe, se abrirá en modo lectura y se imprimirá la primera línea del archivo.

try:
    with open("archivo.txt", "a") as f: # Abre el archivo "archivo.txt" en modo agregar contenido al final del archivo. Si el archivo no existe, se creará uno nuevo.
        f.write("\n") # Escribe un salto de línea en el archivo para separar el contenido existente del nuevo contenido que se agregará.
        f.write("Hola mundo desde write en el with") # Escribe el texto "Hola mundo desde write en el with" en el archivo.
    with open("archivo.txt", "r", encoding="utf-8") as f: # Abre el archivo "archivo.txt" en modo lectura y con codificación UTF-8 para leer su contenido.
        print(f.read()) # Lee todo el contenido del archivo y lo imprime en la consola.
except FileNotFoundError: # Captura la excepción FileNotFoundError si el archivo no existe y ejecuta el bloque de código dentro del except.
    print("No se ha encontrado el archivo") # Imprime un mensaje indicando que el archivo no se ha encontrado.

# verifica que en la terminal este apuntando al archivo creado .txt