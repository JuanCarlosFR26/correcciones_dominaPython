# Ejercicio 1
class Personaje:
    pass

hector_barbossa = Personaje()

# Ejercicio 2
class Clase:
    pass

mago = Clase()
paladin = Clase()
arquero = Clase()

# Ejercicio 3
class PlataformaStreaming:
    pass

netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()

# Ejercicio 4
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco", 4)

# Ejercicio 5
class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")

# Ejercicio 6
class Personaje:
    real = False

class InosukeHashibira(Personaje):
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

inosuke_hashibira = InosukeHashibira("¿Humano?", False, 15)

# Ejercicio 7
class Perro:
    def ladrar(self):
        print("¡Guau!")

perro = Perro()
perro.ladrar()

# Ejercicio 8
class Mortifago:
    def maldicion_imperdonable(self):
        print("¡Avada Kedavra!")

class Mago(Mortifago):
    pass

bellatrix = Mago()
bellatrix.maldicion_imperdonable()

# Ejercicio 9
class Alarma:
    def aplazar(self, cantidad_minutos):
        print(f"La alarma ha sido atrasada {cantidad_minutos} minutos")

alarma = Alarma()
alarma.aplazar(5)

# Ejercicio 10
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()

# Ejercicio 11
class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True

Jugador.revivir()
print(Jugador.vivo)  # Esto imprimirá True

# Ejercicio 12
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

personaje = Personaje(cantidad_flechas=10)
personaje.lanzar_flecha()
print(personaje.cantidad_flechas)  # Esto imprimirá 9

# Ejercicio 13
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

# Ejercicio 14
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

# Ejercicio 15
class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass

# Ejercicio 16
class Padre:
    def trabajar(self):
        print("Trabajando en el hospital")

    def reir(self):
        print("ja ja ja")

class Madre:
    def trabajar(self):
        print("Trabajando en la fiscalía")

class Hija(Madre, Padre):
    pass

hija = Hija()
hija.trabajar()  # Esto imprimirá "Trabajando en el hospital"
hija.reir()  # Esto imprimirá "ja ja ja"

# Ejercicio 17
class Vertebrado:
    def poner_huevos(self):
        pass

class Pez(Vertebrado):
    nadar = True

class Reptil(Vertebrado):
    caminar = True
    venenoso = True

class Ave(Vertebrado):
    tiene_pico = True
    volar = True

class Mamifero(Vertebrado):
    amamantar = True

class Ornitorrinco(Pez, Reptil, Ave, Mamifero):
    def __init__(self):
        self.tiene_pico = True
        self.vertebrado = True
        self.venenoso = True

    def nadar(self):
        pass

    def caminar(self):
        pass

    def amamantar(self):
        pass

# Ejercicio 18
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

hijo = Hijo()
print(hijo.hobby())  # Esto imprimirá "Juego videojuegos en mi tiempo libre"

# Ejercicio 19
# Ejercicio 19
palabra = "Hola"
lista = [1, 2, 3]
tupla = (4, 5, 6)

for objeto in (palabra, lista, tupla):
    print(f'Longitud de {objeto}: {len(objeto)}')


# Ejercicio 20
class Arquero:
    def atacar(self):
        print("Atacando como Arquero")

class Mago:
    def atacar(self):
        print("Atacando como Mago")

class Samurai:
    def atacar(self):
        print("Atacando como Samurai")

personajes = [Arquero(), Mago(), Samurai()]

for personaje in personajes:
    personaje.atacar()

# Ejercicio 21
def personaje_defender(personaje):
    personaje.defender()

# Suponiendo que hay instancias de diferentes clases que tienen el método "defender()"
# personaje_defender(algun_personaje)

# Ejercicio 22
class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}" de \'{self.autor}\''

# Ejercicio 23
class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return int(self.cantidad_paginas)

# Ejercicio 24
class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")

# Puedes crear una instancia y luego eliminarla con "del":
# libro = Libro("Harry Potter", "J.K. Rowling", 400)
# del libro  # Esto imprimirá "Libro eliminado"
