from pathlib import Path

# Ejercicio 1
with open("texto.txt", "r") as archivo:
    contenido = archivo.read()
    print("Ejercicio 1:")
    print(contenido)

# Ejercicio 2
with open("texto.txt", "r") as archivo:
    primera_linea = archivo.readline()
    print("\nEjercicio 2:")
    print(primera_linea)

# Ejercicio 3
with open("texto.txt", "r") as archivo:
    segunda_linea = archivo.readlines()[1]
    print("\nEjercicio 3:")
    print(segunda_linea)

# Ejercicio 4
with open("mi_archivo.txt", "w") as archivo:
    archivo.write("Nuevo texto")

with open("mi_archivo.txt", "r") as archivo:
    nuevo_contenido = archivo.read()
    print("\nEjercicio 4:")
    print(nuevo_contenido)

# Ejercicio 5
with open("mi_archivo.txt", "a") as archivo:
    archivo.write("\nNuevo inicio de sesión")

with open("mi_archivo.txt", "r") as archivo:
    nuevo_contenido = archivo.read()
    print("\nEjercicio 5:")
    print(nuevo_contenido)

# Ejercicio 6
registro_ultima_sesion = ["Lorena", "12/12/2019", "08:17:32 hs", "Sin errores de carga"]
with open("registro.txt", "a") as archivo:
    archivo.writelines("\t".join(registro_ultima_sesion) + "\n")

with open("registro.txt", "r") as archivo:
    nuevo_contenido = archivo.read()
    print("\nEjercicio 6:")
    print(nuevo_contenido)

# Ejercicio 7
ruta_base = Path.home()
print("\nEjercicio 7:")
print(ruta_base)

# Ejercicio 8
ruta = ruta_base / "AprendePython" / "Tema6" / "practicas_path.py"
print("\nEjercicio 8:")
print(ruta)

# Ejercicio 9
ruta_absoluta = Path("/home") / "Aprende Python" / "Tema 6" / "practicas_path.py"
print("\nEjercicio 9:")
print(ruta_absoluta)

# Ejercicio 10
def abrir_leer(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
    return contenido

# Ejercicio 11
def sobrescribir(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("contenido eliminado")

# Ejercicio 12
def registro_error(nombre_archivo):
    with open(nombre_archivo, "a") as archivo:
        archivo.write("se ha registrado un error de ejecución\n")

# Utiliza las funciones creadas
nombre_archivo_prueba = "prueba.txt"
print("\nEjercicio 10:")
print(abrir_leer(nombre_archivo_prueba))

print("\nEjercicio 11:")
sobrescribir(nombre_archivo_prueba)
print("Contenido sobrescrito")

print("\nEjercicio 12:")
registro_error(nombre_archivo_prueba)
print("Error registrado")
