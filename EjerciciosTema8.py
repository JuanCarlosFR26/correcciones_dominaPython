# Ejercicio 1
def dividir(numero1, numero2):
    """
    Función que divide dos números y maneja el caso de división por cero.

    Args:
    numero1 (float): El dividendo.
    numero2 (float): El divisor.

    Returns:
    float: El resultado de la división.
    """
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        print("Error: División por cero.")
        return None

# Ejercicio 2
def ingresar_entero():
    """
    Función que solicita al usuario ingresar un número entero y maneja excepciones
    en caso de que se ingrese un valor no válido.

    Returns:
    int: Número entero ingresado por el usuario.
    """
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero.")

# Ejercicio 3
def sumar_numeros_en_archivo(nombre_archivo):
    """
    Función que lee un archivo de texto que contiene números separados por comas,
    suma los números y devuelve el resultado.

    Args:
    nombre_archivo (str): El nombre del archivo a leer.

    Returns:
    float: La suma de los números en el archivo.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            numeros = [float(numero) for numero in archivo.read().split(',')]
            suma = sum(numeros)
            return suma
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        return None
    except ValueError:
        print("Error: El archivo contiene datos no numéricos.")
        return None

# Ejercicio 4
def generador_infinito():
    """
    Generador que devuelve una secuencia infinita de números consecutivos
    iniciando desde el 1.

    Yields:
    int: Números consecutivos iniciando desde el 1.
    """
    numero = 1
    while True:
        yield numero
        numero += 1

# Ejercicio 5
def generador_multiplos_siete():
    """
    Generador que devuelve de manera indefinida múltiplos de 7 iniciando desde el 7.

    Yields:
    int: Múltiplos de 7.
    """
    numero = 7
    while True:
        yield numero
        numero += 7

# Ejercicio 6
def generador_perder_vida(vidas_iniciales):
    """
    Generador que resta una a una las vidas de un personaje de videojuego y
    devuelve un mensaje cada vez que es llamado.

    Args:
    vidas_iniciales (int): La cantidad inicial de vidas del personaje.

    Yields:
    str: Mensaje indicando la cantidad de vidas restantes o "Game Over".
    """
    vidas = vidas_iniciales
    while vidas > 0:
        yield f"Te quedan {vidas} vidas"
        vidas -= 1
    yield "Game Over"

# Uso de las funciones y generadores
resultado_division = dividir(10, 2)
print(f"Resultado de la división: {resultado_division}")

numero_entero = ingresar_entero()
print(f"Número entero ingresado: {numero_entero}")

suma_archivo = sumar_numeros_en_archivo("datos.txt")
print(f"Suma de los números en el archivo: {suma_archivo}")

generador_numeros = generador_infinito()
for _ in range(5):
    print(next(generador_numeros))

generador_multiplos_siete = generador_multiplos_siete()
for _ in range(5):
    print(next(generador_multiplos_siete))

perder_vida = generador_perder_vida(3)
for _ in range(4):
    print(next(perder_vida))
