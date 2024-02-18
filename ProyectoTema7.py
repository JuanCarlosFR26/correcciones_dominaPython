class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        # Llamamos al constructor de la clase base (Persona)
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        # Método especial para imprimir la información del cliente
        return f"Nombre: {self.nombre} {self.apellido}\nNúmero de Cuenta: {self.numero_cuenta}\nBalance: {self.balance} €"

    def depositar(self, cantidad):
        # Método para depositar dinero en la cuenta
        self.balance += cantidad
        print(f"Se han depositado {cantidad} €. Nuevo balance: {self.balance} €")

    def retirar(self, cantidad):
        # Método para retirar dinero de la cuenta
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se han retirado {cantidad} €. Nuevo balance: {self.balance} €")
        else:
            print("Fondos insuficientes. No se puede realizar la operación.")

# Función para crear un nuevo cliente
def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    balance = float(input("Ingrese el balance inicial: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)

# Función principal que organiza la ejecución del programa
def inicio():
    cliente = crear_cliente()

    while True:
        print("\n¿Qué operación desea realizar?")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar balance")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == '3':
            print(cliente)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

inicio()
