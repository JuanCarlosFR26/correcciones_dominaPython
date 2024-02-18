# Ejercicio 1
texto = ",:_#,,,,,,:::_______##Pyt%on_,,,,,,::#"
texto_limpio = texto.lstrip(",:%#_")
print(texto_limpio)

# Ejercicio 2
frutas = ["mango", "plátano", "arándano", "ciruela", "naranja"]
frutas.insert(3, "piña")
print(frutas)

# Ejercicio 3
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

# Ejercicio 4
def saludar():
    print("¡Hola Python!")

# Ejercicio 5
def bienvenida(nombre_persona):
    print(f"¡Bienvenido/a {nombre_persona}!")

# Ejercicio 6
def cuadrado(numero):
    print(numero ** 2)

# Ejercicio 7
def potencia(base, exponente):
    return base ** exponente

# Ejercicio 8
def usd_a_eur(dolares):
    tasa_conversion = 0.90
    euros = dolares * tasa_conversion
    return euros

# Ejercicio 9
def invertir_palabra(palabra):
    palabra_invertida = palabra[::-1].upper()
    return palabra_invertida

# Ejercicio 10
def todos_positivos(lista_numeros):
    return all(num > 0 for num in lista_numeros)

# Ejercicio 11
def suma_menores(lista_numeros):
    return sum(num for num in lista_numeros if 0 < num < 1000)

# Ejercicio 12
def cantidad_pares(lista_numeros):
    return sum(1 for num in lista_numeros if num % 2 == 0)

# Ejercicio 13
import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(resultado):
    suma_dados = sum(resultado)
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable.")
    elif 6 < suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes oportunidades.")
    else:
        print(f"La suma de tus dados es {suma_dados}. Jugada maestra.")

# Ejercicio 14
def reducir_lista(lista_numeros):
    lista_numeros = list(set(lista_numeros))
    lista_numeros.remove(max(lista_numeros))
    return lista_numeros

def media_numeros(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

# Ejercicio 15
import random

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

def probar_suerte(resultado, lista_numeros):
    if resultado == "Cara":
        print("La lista se va a autodestruir")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros

# Ejercicio 16
def suma_cuadrados(*args):
    resultado = 0
    for arg in args:
        resultado += arg ** 2
    return resultado

# Ejercicio 17
def suma_absolutos(*args):
    resultado = 0
    for arg in args:
        resultado += abs(arg)
    return resultado

# Ejercicio 18
def numeros_juegos(nombre, *args):
    suma_numeros = 0
    for num in args:
        suma_numeros += num
    return f"El juego {nombre} tiene un stock de {suma_numeros} unidades."

# Ejercicio 19
def cantidad_atributos(*args):
    contador = 0
    for arg in args:
        contador += 1
    return contador

# Ejercicio 20
def lista_atributos(**kwargs):
    lista = []
    for key, value in kwargs.items():
        lista.append(value)
    return lista

# Ejercicio 21
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Ejercicio 22
def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        sorted_nums = sorted([num1, num2, num3])
        return sorted_nums[1]

# Ejercicio 23
def letras_unicas(palabra):
    lista_letras = []
    for letra in palabra:
        if letra not in lista_letras:
            lista_letras.append(letra)
    return sorted(lista_letras)

# Ejercicio 24
def tiene_doble_cero(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

# Ejercicio 25
def contar_primos(numero):
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primos = [es_primo(i) for i in range(2, numero + 1)]
    contador_primos = 0
    for primo in primos:
        if primo:
            contador_primos += 1
    print(f"Cantidad de números primos: {contador_primos}")
    return contador_primos

contar_primos(50)