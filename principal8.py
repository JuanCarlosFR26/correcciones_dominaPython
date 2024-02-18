# principal.py
from numeros8 import turno_generator, mensaje_decorador

# Decorador para agregar mensajes a la función obtener_turno
@mensaje_decorador("Su turno es", "Espere para ser atendido")
def obtener_turno(area_generador):
    """
    Obtiene un nuevo turno para el área especificada.

    Args:
    area_generador (generator): Generador de turnos para el área.

    Returns:
    str: Número de turno.
    """
    return next(area_generador)

def main():
    # Inicialización de generadores para cada área
    cultura_generador = turno_generator("C")
    ocio_generador = turno_generator("O")
    perfumeria_generador = turno_generator("P")

    while True:
        # Pregunta al cliente a cuál área desea ir
        area_elegida = input("Seleccione el área (cultura, ocio, perfumeria): ").capitalize()

        # Obtén el turno para el área seleccionada
        if area_elegida == "Cultura":
            turno = obtener_turno(cultura_generador)
        elif area_elegida == "Ocio":
            turno = obtener_turno(ocio_generador)
        elif area_elegida == "Perfumeria":
            turno = obtener_turno(perfumeria_generador)
        else:
            print("Área no válida. Por favor, seleccione cultura, ocio o perfumeria.")
            continue

        print(turno)

        # Pregunta si el cliente desea sacar otro turno
        otro_turno = input("¿Desea sacar otro turno? (s/n): ").lower()
        if otro_turno != 's':
            print("Gracias por usar nuestro servicio. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
