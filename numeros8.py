# numeros.py
def turno_generator(area):
    """
    Generador que devuelve turnos consecutivos para una área específica.

    Args:
    area (str): El nombre del área.

    Yields:
    str: Números consecutivos de turnos para el área especificada.
    """
    contador = 1
    while True:
        yield f"{area}-{contador}"
        contador += 1

def mensaje_decorador(mensaje_inicio, mensaje_fin):
    """
    Decorador que agrega mensajes al inicio y al final del resultado de una función.

    Args:
    mensaje_inicio (str): Mensaje al inicio.
    mensaje_fin (str): Mensaje al final.

    Returns:
    function: Función decorada.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return f"{mensaje_inicio} {resultado} {mensaje_fin}"
        return wrapper
    return decorator
