import random

# Saludo al usuario y genero un número secreto entre 1 y 100
print("¡Bienvenido al juego de adivinanzas!")
nombre = input("¿Cuál es tu nombre? ")
print(f"Buenas, {nombre}, he pensado un número entre 1 y 100.")

numero_secreto = random.randint(1, 100)
intentos_maximos = 6
intentos_realizados = 0

# Bucle principal para adivinar
while intentos_realizados < intentos_maximos:
    # El usuario elige un número
    eleccion_usuario = int(input("Intenta adivinar el número: "))

    # Verifico si el número está dentro del rango permitido
    if 1 <= eleccion_usuario <= 100:
        # Incremento el número de intentos
        intentos_realizados += 1

        # Comparo el número elegido por el usuario con el número secreto
        if eleccion_usuario == numero_secreto:
            print(
                f"¡Felicidades, {nombre}! ¡Has adivinado el número en {intentos_realizados} intentos!"
            )
            break
        elif eleccion_usuario < numero_secreto:
            print(
                "Respuesta incorrecta. Has elegido un número menor al número secreto."
            )
        else:
            print(
                "Respuesta incorrecta. Has elegido un número mayor al número secreto."
            )
    else:
        print(
            "Has elegido un número que no está permitido. Por favor, elige un número entre 1 y 100."
        )

# Mensaje en caso de que el usuario agote todos los intentos sin adivinar
if intentos_realizados == intentos_maximos:
    print(
        f"Lo siento, {nombre}, has agotado tus intentos. El número secreto era {numero_secreto}."
    )
