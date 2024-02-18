from random import choice

def obtener_palabra_secreta():
    palabras = ["python", "programacion", "ahorcado", "codigo", "computadora", "inteligencia"]
    return choice(palabras)

def mostrar_palabra_oculta(palabra, letras_correctas):
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_correctas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    return palabra_mostrada.strip()

def elegir_letra():
    letra = input("Elige una letra: ").lower()
    while not letra.isalpha() or len(letra) != 1:
        print("Por favor, ingresa una única letra válida.")
        letra = input("Elige una letra: ").lower()
    return letra

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_correctas = set()
    vidas = 6

    print("¡Bienvenido al juego del ahorcado!")
    print("Tienes 6 vidas. Adivina la palabra.")

    while vidas > 0:
        letra = elegir_letra()

        if letra in palabra_secreta:
            print("¡Bien hecho! La letra está en la palabra.")
            letras_correctas.add(letra)
        else:
            print("Incorrecto. Pierdes una vida.")
            vidas -= 1

        palabra_mostrada = mostrar_palabra_oculta(palabra_secreta, letras_correctas)
        print(f"Palabra actual: {palabra_mostrada}")
        print(f"Vidas restantes: {vidas}")

        if "_" not in palabra_mostrada:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

    if vidas == 0:
        print(f"Perdiste. La palabra secreta era: {palabra_secreta}")

# Llamamos a la función para iniciar el juego
jugar_ahorcado()
