from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:
        mostrar_menu() # mostrar el menú de opciones del café que se ofrece
        opcion = input("Seleccione una opción: " )

        if opcion == "1":
            pedir_cafe() # Aquí se puede agregar la lógica para preparar el café1
        elif opcion == "2":
            ver_historial() # ver el historial de pedidos
        elif opcion == "3":
            print("\n Gracias por usar la máquina de café. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción sugeridas.")

if __name__ == "__main__":
    main()