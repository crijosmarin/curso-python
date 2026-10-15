ARCHIVOS_PEDIDOS ="historial_pedidos.txt"


def pedir_cafe():
    print("\n Elige el café que prefieras:")
    print("1. Café americano")
    print("2. Café con leche")
    print("3. Café capuchino")
    print("4. Café expreso")
    print("5. Café descafeinado")
    print("6. Cafélatte")

    opcion = input("Seleccione una opción: ") # Aquí puedes agregar la lógica para preparar el café

    cafe = {
        "1": "Café americano",
        "2": "Café con leche",
        "3": "Café capuchino",
        "4": "Café expreso",
        "5": "Café descafeinado",
        "6": "Café latte"
    }

    if opcion in cafe:
        cafe_elegido = cafe[opcion]
        print(f"\n Has elegido: {cafe_elegido}. ¡Disfruta tu café!")

        with open(ARCHIVOS_PEDIDOS, "a", encoding="utf-8") as archivo: # Abre el archivo "historial_pedidos.txt" en modo agregar contenido al final del archivo. Si el archivo no existe, se creará uno nuevo.
            archivo.write(f"{cafe_elegido}\n") # Escribe el café elegido en el archivo, seguido de un salto de línea.
    else:
        print("Opción inválida. Por favor, seleccione una opción sugerida.")