# Manejo de errores con try y except: es una estructura de control que permite manejar errores en tiempo de ejecución. Se utiliza para capturar excepciones y evitar que el programa se detenga abruptamente. La sintaxis básica es la siguiente:

try:
    numero = 10 / 0 # Esto generará un error de división por cero
except ZeroDivisionError: # Este bloque se ejecutará si ocurre un error de división por cero
    print("No se puede dividir por cero") # Este mensaje se imprimirá si ocurre el error

x = 1 # Esta variable x ha sido definida y no generará un error

try:
    print(x) # Esto imprimirá el valor de x, que es 1
except NameError: # Este bloque se ejecutará si ocurre un error de variable no definida
    print("Esta variable no ha sido definida") # Este mensaje se imprimirá si ocurre el error
finally: # Este bloque se ejecutará siempre, haya ocurrido un error o no
    print("Esto será ejecutado siendo exitoso o no el bloque") # Este mensaje se imprimirá siempre, haya ocurrido un error o no