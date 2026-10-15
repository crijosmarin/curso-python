
ARCHIVO_PEDIDOS = "historial_pedidos.txt"

def ver_historial(): # Esta función permite ver el historial de pedidos de café realizados por el usuario. Abre el archivo "historial_pedidos.txt" en modo lectura y muestra cada pedido en la consola. Si el archivo no existe, se captura la excepción FileNotFoundError y se muestra un mensaje indicando que aún no existe un historial de pedidos.
    try:
        print("\n Historial de pedidos") # Imprime un mensaje indicando que se mostrará el historial de pedidos.
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo: # Abre el archivo "historial_pedidos.txt" en modo lectura y con codificación UTF-8. El bloque with asegura que el archivo se cierre automáticamente al finalizar.
            pedidos = archivo.readlines() # Lee todas las líneas del archivo y las almacena en la lista "pedidos". Cada línea representa un pedido de café realizado por el usuario.
            if pedidos: # Verifica si la lista "pedidos" contiene elementos. Si es así, se itera sobre cada pedido y se imprime en la consola con su número de orden. Si la lista está vacía, se imprime un mensaje indicando que aún no hay ningún pedido.
                for i, pedido in enumerate(pedidos, start=1): # Itera sobre la lista "pedidos" utilizando la función enumerate para obtener el índice y el valor de cada pedido. El parámetro start=1 indica que la numeración comenzará desde 1 en lugar de 0.
                    print(str(i) + ". " + pedido.strip()) # Imprime el número de orden y el pedido correspondiente en la consola. La función strip() se utiliza para eliminar cualquier espacio en blanco al inicio o al final del pedido.
            else: # Si la lista "pedidos" está vacía, se imprime un mensaje indicando que aún no hay ningún pedido.
                print("Aún no hay ningún pedido") # Imprime un mensaje indicando que aún no hay ningún pedido registrado.
    except FileNotFoundError: # Captura la excepción FileNotFoundError si el archivo "historial_pedidos.txt" no existe y ejecuta el bloque de código dentro del except.
        print("\n Todavía no existe un historial de pedidos") # Imprime un mensaje indicando que aún no existe un historial de pedidos, ya que el archivo no se ha creado o no se ha registrado ningún pedido hasta el momento.
        