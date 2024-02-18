# Proyecto: Cálculo de Comisiones para Vendedores

# Paso 1: Solicitar al usuario su nombre y las ventas del mes.
nombre_vendedor = input("Ingrese su nombre: ")
ventas_mes_str = input(f"{nombre_vendedor}, ¿cuánto ha vendido este mes? €: ")

# Paso 2: Convertir las ventas a un número de punto flotante (float).
ventas_mes = float(ventas_mes_str)

# Paso 3: Calcular la comisión utilizando el 18% de las ventas.
comision = ventas_mes * 0.18

# Paso 4: Formatear el resultado como una frase con el nombre y la comisión.
# Utilizamos la función format() para dar formato a la salida.
resultado_formateado = "Hola {}, tu comisión por las ventas de este mes es: {:.2f} €".format(nombre_vendedor, comision)

# Paso 5: Mostrar en pantalla el resultado formateado.
print(resultado_formateado)
