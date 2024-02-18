# Ejercicio 1
# Declarar variables nombre y edad con valores asignados.
nombre = "TuNombre"
edad = 25

# Ejercicio 2
# Declarar variables nombre, apellido y nombre_completo, y realizar concatenación.
nombre = "Tu"
apellido = "Apellido"
nombre_completo = nombre + " " + apellido

# Ejercicio 3
# Declarar variable libro, asignar valor y mostrar en pantalla.
libro = "Python"
print(f"Estoy aprendiendo Python gracias a este libro de {libro}")

# Ejercicio 4
# Declarar variable num_entero, asignar valor y mostrar tipo de dato.
num_entero = 42
print(f"El tipo de dato de num_entero es: {type(num_entero)}")

# Ejercicio 5
# Declarar variable num_decimal, asignar valor float.
num_decimal = 3.14

# Ejercicio 6
# Verificar el tipo de resultado de la suma de dos números.
num1 = 7.5
num2 = 2.5
tipo_resultado = type(num1 + num2)
print(f"El tipo de dato del resultado es: {tipo_resultado}")

# Ejercicio 7
# Convertir num1 a int e imprimir tipo de dato resultante.
num1 = int(num1)
print(f"El tipo de dato de num1 después de la conversión es: {type(num1)}")

# Ejercicio 8
# Convertir num2 a float e imprimir tipo de dato resultante.
num2 = float(num2)
print(f"El tipo de dato de num2 después de la conversión es: {type(num2)}")

# Ejercicio 9
# Sumar valores de num1 y num2, aplicando conversiones necesarias.
print("La suma de num1 y num2 es:", int(num1) + num2)

# Ejercicio 10
# Mostrar nombre y número de asociado en una frase.
nombre_asociado = "Usuario"
numero_asociado = 123
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

# Ejercicio 11
# Mostrar cantidad de puntos acumulados en una frase.
puntos_nuevos = 50
puntos_totales = 200
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

# Ejercicio 12
# Calcular y mostrar la cantidad total de puntos acumulados.
puntos_anteriores = 150
puntos_totales = puntos_anteriores + puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

# Ejercicio 13
# Mostrar el cociente de la división de dos números.
resultado_division = 874 / 27
print("El cociente de la división es:", resultado_division)

# Ejercicio 14
# Mostrar el módulo de la división de dos números.
resultado_modulo = 456 % 33
print("El módulo de la división es:", resultado_modulo)

# Ejercicio 15
# Calcular y mostrar la raíz cuadrada de un número.
raiz_cuadrada = 783 ** 0.5
print("La raíz cuadrada de 783 es:", raiz_cuadrada)

# Ejercicio 16
# Redondear el resultado de la división a 2 decimales y mostrar en pantalla.
resultado_redondeado = round(10 / 3, 2)
print("El resultado redondeado es:", resultado_redondeado)

# Ejercicio 17
# Redondear el número al entero más próximo y mostrar en pantalla.
numero_redondeado = round(10.676767)
print("El número redondeado es:", numero_redondeado)

# Ejercicio 18
# Calcular y mostrar la raíz cuadrada de 5 redondeada a 4 decimales.
raiz_cuadrada_5 = (5 ** 0.5)
raiz_redondeada = round(raiz_cuadrada_5, 4)
print("La raíz cuadrada de 5 redondeada a 4 decimales es:", raiz_redondeada)
