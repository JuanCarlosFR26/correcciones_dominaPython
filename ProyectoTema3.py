# Paso 1: Solicitar al usuario que ingrese un texto.
texto_usuario = input("Ingrese un texto: ")

# Paso 2: Solicitar al usuario que ingrese tres letras a su elección.
letra1 = input("Ingrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la tercera letra: ")

# Paso 3: Almacenar las letras en una lista para su posterior uso.
letras_elegidas = [letra1, letra2, letra3]

# Paso 4: Contar cuántas veces aparece cada una de las letras en el texto.
# Usar el método count() para contar ocurrencias, convertir el texto y las letras a minúsculas para evitar diferencias de mayúsculas y minúsculas.
conteo_letra1 = texto_usuario.lower().count(letra1.lower())
conteo_letra2 = texto_usuario.lower().count(letra2.lower())
conteo_letra3 = texto_usuario.lower().count(letra3.lower())

# Paso 5: Contar la cantidad de palabras en el texto.
# Usar el método split() para dividir el texto en una lista de palabras y luego contar el tamaño de la lista.
cantidad_palabras = len(texto_usuario.split())

# Paso 6: Obtener la primera y última letra del texto.
primera_letra = texto_usuario[0]
ultima_letra = texto_usuario[-1]

# Paso 7: Invertir el orden de las palabras en el texto.
# Usar el método split() para dividir el texto en una lista, invertir la lista y luego unir las palabras.
texto_invertido = " ".join(texto_usuario.split()[::-1])

# Paso 8: Verificar si la palabra "python" se encuentra en el texto.
palabra_python_presente = "python" in texto_usuario.lower()

# Paso 9: Mostrar los resultados al usuario.
print("\nResultados:")
print(f"1. La letra '{letra1}' aparece {conteo_letra1} veces.")
print(f"2. La letra '{letra2}' aparece {conteo_letra2} veces.")
print(f"3. La letra '{letra3}' aparece {conteo_letra3} veces.")
print(f"4. Hay {cantidad_palabras} palabras en el texto.")
print(f"5. La primera letra del texto es '{primera_letra}' y la última letra es '{ultima_letra}'.")
print(f"6. Texto con orden de palabras invertido: '{texto_invertido}'")
print(f"7. ¿La palabra 'python' se encuentra en el texto?: {palabra_python_presente}")
