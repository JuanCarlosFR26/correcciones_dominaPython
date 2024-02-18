import os
import re
import time
from datetime import datetime
from tabulate import tabulate


def buscar_numeros_serie(directorio_raiz):
    # Obtener la fecha de búsqueda
    fecha_busqueda = datetime.now().strftime("%d/%m/%y")

    # Iniciar el temporizador
    tiempo_inicio = time.time()

    # Lista para almacenar los resultados
    resultados = []

    # Patrón de número de serie
    patron_numero_serie = re.compile(r"N\w{3}-\d{5}")

    # Recorrer el árbol de directorios
    for raiz, carpetas, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            # Construir la ruta completa del archivo
            ruta_archivo = os.path.join(raiz, archivo)

            # Leer el contenido del archivo
            with open(ruta_archivo, "r", encoding="utf-8") as file:
                contenido = file.read()

                # Buscar números de serie en el contenido
                matches = re.findall(patron_numero_serie, contenido)

                # Agregar resultados a la lista
                for match in matches:
                    resultados.append((archivo, match))

    # Detener el temporizador
    tiempo_fin = time.time()
    duracion_busqueda = round(tiempo_fin - tiempo_inicio)

    # Mostrar resultados en formato de tabla
    if resultados:
        tabla_resultados = tabulate(
            resultados, headers=["ARCHIVO", "NRO. SERIE"], tablefmt="grid"
        )
        print(f"Fecha de búsqueda: {fecha_busqueda}\n")
        print(tabla_resultados)
    else:
        print("No se encontraron números de serie.")

    # Informar números encontrados y duración de búsqueda
    print(f"\nNúmeros encontrados: {len(resultados)}")
    print(f"Duración de la búsqueda: {duracion_busqueda} segundos")


# Directorio raíz donde se realizará la búsqueda
# Acuérdate que debes cambiar la ruta por la tuya
directorio_raiz = (
    "C:\\Users\\Juanqui\\Desktop\\Aprende Python\\correcciones\\Gran proyecto"
)

# Llamar a la función de búsqueda
buscar_numeros_serie(directorio_raiz)
