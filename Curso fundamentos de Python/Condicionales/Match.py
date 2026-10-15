dia = input("Ingrese un número del 1 al 7: ") # Solicita al usuario que ingrese un número del 1 al 7 segun cada case asignado a cada dia de la semana

match dia:
    case 1:
        print("Hoy es lunes")
    case 2:
        print("Hoy es martes")
    case 3:
        print("Hoy es miércoles")
    case 4:
        print("Hoy es jueves")
    case 5:
        print("Hoy es viernes")
    case _:
        print("Es fin de semana")

Mes = input("Ingrese el mes: ").lower() # Solicita al usuario que ingrese el mes, el .lower() convierte el texto a minusculas para que no haya errores de comparacion

match Mes:
    case "enero":
        print("Animo comenzo el año")
    case "febrero":
        print("El mejor Mes de el año")
    case "marzo":
        print("El mes de la mujer")
    case "abril":
        print("El mes de la tierra")
    case "mayo":
        print("El mes de la madre")
    case "junio":
        print("llegamos a la mitad del año")
    case "julio":
        print("El mes de la independencia")
    case "agosto":
        print("A elevar cometas y globos")
    case "septiembre":
        print("Desde septiembre se siente Diciembreeeeee")
    case "octubre":
        print("llegaron las brujas y los fantasmas")
    case "noviembre":
        print("Ya cumpliste tus propositos, te queda un mes para cumplirlos")
    case "diciembre":
        print("Final final no va más")
    case _:
        print("Eso no es un mes del año, jajajajaja")