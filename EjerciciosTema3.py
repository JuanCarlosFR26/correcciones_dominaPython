# Ejercicio 1
# Encuentra y muestra por pantalla el tercer carácter en "escritorio".
palabra = "escritorio"
tercer_caracter = palabra[2]
print("El tercer carácter es:", tercer_caracter)

# Ejercicio 2
# Muestra por pantalla el índice de la primera aparición de "videojuego".
frase1 = "No es por nada, pero este videojuego es demasiado fácil"
indice_videojuego = frase1.find("videojuego")
print("El índice de la primera aparición de 'videojuego' es:", indice_videojuego)

# Ejercicio 3
# Muestra por pantalla el índice de la última aparición de "ejercicio".
frase2 = "Tengo que asegurarme de comprobar el ejercicio para que no tenga errores"
indice_ultimo_ejercicio = frase2.rfind("ejercicio")
print("El índice de la última aparición de 'ejercicio' es:", indice_ultimo_ejercicio)

# Ejercicio 4
# Extrae la primera palabra de la frase usando slicing y muéstrala por pantalla.
frase3 = "Escribir código es fundamental para aprender programación"
primera_palabra = frase3[:frase3.find(" ")]
print("La primera palabra es:", primera_palabra)

# Ejercicio 5
# Coge cada tercer carácter desde el sexto hasta el final e imprime el resultado.
frase4 = "Python es uno de los lenguajes más populares de la actualidad"
resultado_slicing = frase4[5::3]
print("Cada tercer carácter desde el sexto hasta el final:", resultado_slicing)

# Ejercicio 6
# Invierte la posición de todos los caracteres y muestra el resultado.
frase5 = "Si trabajas con ordenadores no tienes que aguantar discusiones ni bromas estúpidas, además de que no se comen tu comida"
resultado_invertido = frase5[::-1]
print("Frase invertida:", resultado_invertido)

# Ejercicio 7
# Imprime el texto en mayúsculas usando métodos de strings.
texto_original = "Con estos ejercicios voy a adquirir todo lo necesario para dominar la lógica de programación"
texto_mayusculas = texto_original.upper()
print("Texto en mayúsculas:", texto_mayusculas)

# Ejercicio 8
# Une la lista completa en un string, separando cada elemento con un espacio.
palabras = ["Este", "curso", "me", "gusta"]
union_string = " ".join(palabras)
print("Lista unida en un string:", union_string)

# Ejercicio 9
# Reemplaza "el primero" por "JavaScript" y "el segundo" por "Python".
frase6 = "No sé con cuál quedarme, si con el primero o con el segundo"
resultado_reemplazo = frase6.replace("el primero", "JavaScript").replace("el segundo", "Python")
print("Frase con reemplazos:", resultado_reemplazo)

# Ejercicio 10
# Verifica si la palabra "trabajo" no se encuentra en la frase.
frase7 = "Mi jefe me ha mandado aprender Python para el trabajo, y estoy emocionado"
resultado_verificacion = "trabajo" not in frase7
print("¿La palabra 'trabajo' no se encuentra en la frase?", resultado_verificacion)

# Ejercicio 11
# Concatena 12 veces la palabra "Python" y muestra el resultado.
palabra_python = "Python"
concatenacion_multiplicativa = palabra_python * 12
print("Palabra 'Python' concatenada 12 veces:", concatenacion_multiplicativa)

# Ejercicio 12
# Muestra el largo de la palabra "esternocleidomastoideo".
palabra_larga = "esternocleidomastoideo"
largo_palabra = len(palabra_larga)
print("Largo de la palabra:", largo_palabra)

# Ejercicio 13
# Crea una lista con 8 elementos y muéstrala por pantalla.
lista = [1, "dos", 3.0, True, [4, 5], (6, 7), {"ocho": 8}, None]
print("Lista:", lista)

# Ejercicio 14
# Agrega "JavaScript" a la lista y muéstrala por pantalla.
lenguajes_programacion = ["Python", "Ruby", "PHP", "CSS"]
lenguajes_programacion.append("JavaScript")
print("Lista con JavaScript agregado:", lenguajes_programacion)

# Ejercicio 15
# Utiliza pop() para quitar el quinto elemento y almacénalo en "eliminada".
marcas = ["Acer", "Samsung", "Xiaomi", "Apple", "Windows", "Lg"]
eliminada = marcas.pop(4)
print("Lista después de pop:", marcas)
print("Elemento eliminado:", eliminada)

# Ejercicio 16
# Crea un diccionario con información personal.
informacion_personal = {"nombre": "Juan", "apellido": "Pérez", "edad": 30, "profesion": "Ingeniero"}
print("Diccionario de información personal:", informacion_personal)

# Ejercicio 17
# Imprime el segundo ítem del diccionario.
segundo_item = informacion_personal["apellido"]
print("Segundo ítem del diccionario:", segundo_item)

# Ejercicio 18
# Añade una clave "pais" y muéstralo por pantalla.
diccionario = {"nombre": "Juan Carlos", "apellido": "Fernández", "edad": 28}
diccionario["pais"] = "España"
print("Diccionario con clave 'pais':", diccionario)

# Ejercicio 19
# Usa un método de tuplas para contar la cantidad de veces que aparece el valor 3.
tupla_ejercicio = (3, 2, 4, 5, 1, 2, 6, 2, 3, 1, 5, 7, 2, 8, 9)
contador_tres = tupla_ejercicio.count(3)
print("Cantidad de veces que aparece el valor 3:", contador_tres)

# Ejercicio 20
# Convierte la tupla en una lista y almacénala en una variable.
tupla_ejercicio = (1, 2, 3, 4, 5, 1, 2, 3, 4)
lista_convertida = list(tupla_ejercicio)
print("Tupla convertida en lista:", lista_convertida)

# Ejercicio 21
# Extrae los elementos de la tupla en 6 variables a, b, c, d, e, f.
tupla_ejercicios = ("Python", "Java", "PHP", "SQL", "JavaScript", "Django")
a, b, c, d, e, f = tupla_ejercicios
print("Elementos extraídos de la tupla:", a, b, c, d, e, f)

# Ejercicio 22
# Une los sets en uno solo.
set1 = {8, 10, "once", "doce"}
set2 = {"once", 4, 5}
set_unido = set1.union(set2)
print("Sets unidos:", set_unido)

# Ejercicio 23
# Elimina un elemento al azar del set.
loteria = {"Python", "Java", "SQL", "JQuery", "Git", "Github"}
elemento_eliminado = loteria.pop()
print("Set después de eliminar un elemento:", loteria)
print("Elemento eliminado:", elemento_eliminado)

# Ejercicio 24
# Agrega el nombre de Lorenzo al set.
nombres = {"Juan", "Sonia", "Iván", "Mayte", "José Manuel", "Javi", "Miriam"}
nombres.add("Lorenzo")
print("Set con Lorenzo agregado:", nombres)

# Ejercicio 25
# Realiza una comparación y almacena el resultado en una variable llamada prueba.
prueba = (5 > 3)
print("Resultado de la comparación:", prueba)

# Ejercicio 26
# Verifica si 19238 / 38 es mayor que 92*59 y muestra el resultado en pantalla.
resultado_comparacion = (19238 / 38) > (92 * 59)
print("¿19238 / 38 es mayor que 92*59?", resultado_comparacion)

# Ejercicio 27
# Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado en pantalla.
resultado_raiz_cuadrada = (25 ** 0.5) == 5
print("¿La raíz cuadrada de 25 es igual a 5?", resultado_raiz_cuadrada)
