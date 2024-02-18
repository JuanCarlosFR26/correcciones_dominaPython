from collections import Counter, defaultdict, deque
import datetime
import math
import re

# Ejercicio 1
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)
print("Ejercicio 1:")
print(contador)
print()

# Ejercicio 2
mi_diccionario = defaultdict(lambda: "Valor no encontrado", {"edad": 44})
print("Ejercicio 2:")
print(mi_diccionario)
print()

# Ejercicio 3
lista_ciudades = deque(["Madrid", "Tokio", "Londres", "París", "Roma", "Copenhague"])
print("Ejercicio 3:")
print(lista_ciudades)
print()

# Ejercicio 4
mi_fecha = datetime.date(2022, 3, 19)
print("Ejercicio 4:")
print(mi_fecha)
print()

# Ejercicio 5
hoy = datetime.date.today()
print("Ejercicio 5:")
print(hoy)
print()

# Ejercicio 6
minutos = datetime.datetime.now().minute
print("Ejercicio 6:")
print(minutos)
print()

# Ejercicio 7
resultado = math.log10(38)
print("Ejercicio 7:")
print(resultado)
print()

# Ejercicio 8
resultado = math.sqrt(math.pi)
print("Ejercicio 8:")
print(resultado)
print()

# Ejercicio 9
resultado = math.factorial(9)
print("Ejercicio 9:")
print(resultado)
print()

# Ejercicio 10
def verificar_email(email):
    if "@" in email and email.endswith(".com"):
        print("Correcto")
    else:
        print("La dirección de email no es correcta")

print("Ejercicio 10:")
verificar_email("usuario@example.com")
print()

# Ejercicio 11
def verificar_saludo(frase):
    if frase.startswith("Hola"):
        print("Ok")
    else:
        print("No ha saludado")

print("Ejercicio 11:")
verificar_saludo("Hola, ¿cómo estás?")
print()

# Ejercicio 12
def verificar_cp(cp):
    # Expresión regular para verificar el código postal (nnnnn)
    patron = re.compile(r'^\d{5}$')

    if patron.match(cp):
        print("Ok")
    else:
        print("El código postal no es correcto")

print("Ejercicio 12:")
verificar_cp("12345")

