# Ejercicio 1
# Crea dos variables y verifica si num1 es mayor o igual que num2.
num1 = 20
num2 = 49
mi_booleano = num1 >= num2
print(f"Ejercicio 1: ¿{num1} es mayor o igual que {num2}?: {mi_booleano}")

# Ejercicio 2
# Calcula la raíz cuadrada de 81 y compara con el valor de num2.
num1 = (81 ** 0.5)
num2 = 5
mi_booleano = num1 == num2
print(f"Ejercicio 2: ¿La raíz cuadrada de 81 es igual a {num2}?: {mi_booleano}")

# Ejercicio 3
# Realiza operaciones y verifica si num1 es diferente a num2.
num1 = 78 * 2
num2 = 24 * 5
mi_booleano = num1 != num2
print(f"Ejercicio 3: ¿{num1} es diferente a {num2}?: {mi_booleano}")

# Ejercicio 4
# Realiza operaciones y verifica condiciones múltiples.
num1 = 80
num2 = 94 / 5
num3 = 5 * 12
mi_booleano = num1 > num2 and num1 < num3
print(f"Ejercicio 4: ¿{num1} es mayor que {num2} y menor que {num3}?: {mi_booleano}")

# Ejercicio 5
# Realiza operaciones y verifica condiciones con operadores lógicos.
num1 = 42
num2 = 120 / 5
num3 = 5 * 8
mi_booleano = num1 > num2 or num1 < num3
print(f"Ejercicio 5: ¿{num1} es mayor que {num2} o menor que {num3}?: {mi_booleano}")

# Ejercicio 6
# Verifica si ciertas palabras no se encuentran en una frase.
palabra1 = "éxito"
palabra2 = "tecnología"
frase = "Hay que practicar cada tecnología hasta que consigamos tener éxito"
mi_booleano = palabra1 not in frase and palabra2 not in frase
print(f"Ejercicio 6: ¿'{palabra1}' y '{palabra2}' no se encuentran en la frase?: {mi_booleano}")

# Ejercicio 7
# Compara valores ingresados por el usuario.
num1 = int(input("Ingrese el valor de num1: "))
num2 = int(input("Ingrese el valor de num2: "))
if num1 > num2:
    print(f"El valor ingresado para num1 ({num1}) es mayor que el valor de num2 ({num2}).")
elif num2 > num1:
    print(f"El valor ingresado para num2 ({num2}) es mayor que el valor de num1 ({num1}).")
else:
    print(f"Los valores ingresados para num1 ({num1}) y num2 ({num2}) son iguales.")

# Ejercicio 8
# Verifica si una persona puede conducir.
edad = 16
carnet = False
if edad >= 18 and carnet:
    print("Puede conducir")
elif edad >= 18 and not carnet:
    print("No puedes conducir aún. Debes tener 18 años y tener el carnet")
elif edad < 18 and carnet:
    print("No puedes conducir. Necesitas tener el carnet")
else:
    print("No puedes conducir. Necesitas tener 18 años y el carnet")

# Ejercicio 9
# Evalúa las condiciones para acceder a un puesto de trabajo.
sabe_python = False
conoce_ingles = True
if sabe_python and conoce_ingles:
    print("Cumples los requisitos para el trabajo")
elif sabe_python and not conoce_ingles:
    print("Para el trabajo, necesitas saber programar en Python y tener conocimientos de inglés")
elif not sabe_python and conoce_ingles:
    print("Necesitas saber programar en Python para este trabajo")
else:
    print("Para poder acceder al puesto de trabajo, necesitas tener conocimientos de inglés")

# Ejercicio 10
# Saluda a todos los miembros de la clase utilizando loops for.
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print(f"Hola {alumno}")

# Ejercicio 11
# Suma todos los números de la lista utilizando loops for.
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros += numero
print(f"Ejercicio 11: La suma de todos los números es: {suma_numeros}")

# Ejercicio 12
# Suma números pares e impares por separado utilizando loops for.
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
print(f"Ejercicio 12: Suma de pares: {suma_pares}, Suma de impares: {suma_impares}")

# Ejercicio 13
# Imprime los números del 10 al 0 utilizando loops while.
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

# Ejercicio 14
# Resta números de 50 a 0, mostrando los divisibles por 5.
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1

# Ejercicio 15
# Imprime elementos de una lista hasta encontrar un valor negativo.
lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]
for numero in lista_numeros:
    if numero < 0:
        break
    print(numero)

# Ejercicio 16
# Crea una lista de números desde 2500 hasta 2585.
mi_lista = list(range(2500, 2586))

# Ejercicio 17
# Crea una lista de múltiplos de 3 desde 3 hasta 300.
mi_lista = list(range(3, 301, 3))

# Ejercicio 18
# Suma los cuadrados de los números del 1 al 15.
suma_cuadrados = 0
for numero in range(1, 16):
    cuadrado = numero ** 2
    suma_cuadrados += cuadrado
print(f"Ejercicio 18: La suma de los cuadrados es: {suma_cuadrados}")

# Ejercicio 19
# Imprime frases con nombres y sus índices utilizando enumerate().
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f"{nombre} se encuentra en el índice {indice}")

# Ejercicio 20
# Crea una lista de tuplas (índice, elemento) utilizando enumerate() en un string.
cadena = "Python"
lista_indices = list(enumerate(cadena))

# Ejercicio 21
# Imprime en pantalla únicamente los índices de aquellos nombres que empiecen por M.
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(f"El nombre {nombre} empieza con M y se encuentra en el índice {indice}")

# Ejercicio 22
# Muestra frases con la relación entre países y capitales utilizando zip.
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Camberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")

# Ejercicio 23
# Crea un objeto zip con listas de marcas y productos.
marcas = ["Nike", "Adidas", "Puma"]
productos = ["Zapatillas", "Camisetas", "Gorras"]
mi_zip = zip(marcas, productos)

# Ejercicio 24
# Crea un zip con las traducciones de los números del 1 al 5.
numeros = list(zip(["uno", "Dos", "Tres", "Cuatro", "Cinco"], ["un", "Deux", "Trois", "Quatre", "Five"], ["one", "Two", "Three", "Four", "Five"]))
print(numeros)

# Ejercicio 25
# Obtiene el valor máximo de la lista_numeros y almacénalo en valor_maximo.
lista_numeros = [44542247/2, 21310/5, 213474*33, 44556475, 121676, 6654067, 353254, 123134, 5512, 6115]
valor_maximo = max(lista_numeros)
print(valor_maximo)

# Ejercicio 26
# Calcula la diferencia entre el valor máximo y mínimo en la lista_numeros.
rango = max(lista_numeros) - min(lista_numeros)
print(rango)

# Ejercicio 27
# Utiliza max(), min() y diccionarios para obtener el mínimo valor y el último nombre en orden alfabético.
diccionario_edades = {"Lucía": 32, "María": 18, "Lorena": 44, "Pedro": 30, "Juan": 22, "Sonia": 45, "Gonzalo": 20, "Isabel": 5, "Rubén": 59}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima, ultimo_nombre)

# Ejercicio 28
# Implementa randint() para obtener un número entero del 1 al 10.
from random import randint
aleatorio = randint(1, 10)
print(aleatorio)

# Ejercicio 29
# Implementa random() para obtener un número decimal entre 0 y 1.
from random import random
aleatorio = random()
print(aleatorio)

# Ejercicio 30
# Usa choice() para obtener un nombre al azar de la lista_nombres.
from random import choice
sorteo = choice(lista_nombres)
print(sorteo)

# Ejercicio 31
# Crea una lista con los cuadrados de los números en la lista valores.
valores_cuadrado = [valor ** 2 for valor in [1, 2, 3, 4, 5, 6, 9.5]]
print(valores_cuadrado)

# Ejercicio 32
# Utiliza comprensión de listas para obtener una lista de valores pares de la lista valores.
valores_pares = [valor for valor in [1, 2, 3, 4, 5, 6, 9.5] if valor % 2 == 0]
print(valores_pares)

# Ejercicio 33
# Convierte los grados Fahrenheit a Celsius utilizando comprensión de listas.
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(fahrenheit - 32) * 5/9 for fahrenheit in temperatura_fahrenheit]
print(grados_celsius)
