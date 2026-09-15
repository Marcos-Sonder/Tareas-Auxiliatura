class SerVivo:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Animal(SerVivo):
    def __init__(self, nombre, edad, peso):
        super().__init__(nombre, edad)
        self.peso = peso


class Felino(Animal):
    def __init__(self, nombre, edad, peso, colorPelaje):
        super().__init__(nombre, edad, peso)
        self.colorPelaje = colorPelaje


class Gato(Felino):
    def __init__(self, nombre, edad, peso, colorPelaje, raza):
        super().__init__(nombre, edad, peso, colorPelaje)
        self.raza = raza


class Leon(Felino):
    def __init__(self, nombre, edad, peso, colorPelaje, melena):
        super().__init__(nombre, edad, peso, colorPelaje)
        self.melena = melena


class Reptil(Animal):
    def __init__(self, nombre, edad, peso, escamas):
        super().__init__(nombre, edad, peso)
        self.escamas = escamas


class Vivora(Reptil):
    def __init__(self, nombre, edad, peso, escamas, venenosa):
        super().__init__(nombre, edad, peso, escamas)
        self.venenosa = venenosa


class Roedor(Animal):
    def __init__(self, nombre, edad, peso, tamaño):
        super().__init__(nombre, edad, peso)
        self.tamaño = tamaño


class Raton(Roedor):
    def __init__(self, nombre, edad, peso, tamaño, color):
        super().__init__(nombre, edad, peso, tamaño)
        self.color = color


class Conejo(Roedor):
    def __init__(self, nombre, edad, peso, tamaño, orejas):
        super().__init__(nombre, edad, peso, tamaño)
        self.orejas = orejas


class Rana(Animal):
    def __init__(self, nombre, edad, peso, colorPiel):
        super().__init__(nombre, edad, peso)
        self.colorPiel = colorPiel


class Humano(Animal):
    def __init__(self, nombre, edad, peso, nacionalidad):
        super().__init__(nombre, edad, peso)
        self.nacionalidad = nacionalidad


class Niño(Humano):
    def __init__(self, nombre, edad, peso, nacionalidad, escuela):
        super().__init__(nombre, edad, peso, nacionalidad)
        self.escuela = escuela


class Adulto(Humano):
    def __init__(self, nombre, edad, peso, nacionalidad, profesion):
        super().__init__(nombre, edad, peso, nacionalidad)
        self.profesion = profesion


class Anciano(Humano):
    def __init__(self, nombre, edad, peso, nacionalidad, jubilado):
        super().__init__(nombre, edad, peso, nacionalidad)
        self.jubilado = jubilado


class Planta(SerVivo):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre, edad)
        self.tipo = tipo


class Flor(Planta):
    def __init__(self, nombre, edad, tipo, color):
        super().__init__(nombre, edad, tipo)
        self.color = color


# OBJETOS

gato = Gato("Michi", 3, 5, "Blanco", "Siames")
leon = Leon("Simba", 5, 180, "Amarillo", "Grande")
vivora = Vivora("Kaa", 4, 10, "Si", True)
raton = Raton("Jerry", 2, 1, "Pequeño", "Gris")
conejo = Conejo("Bugs", 3, 3, "Mediano", "Largas")
rana = Rana("Rana", 2, 1, "Verde")

niño = Niño("Pedro", 10, 30, "Boliviana", "Colegio")
adulto = Adulto("Juan", 35, 75, "Boliviana", "Ingeniero")
anciano = Anciano("Carlos", 70, 70, "Boliviana", True)

flor = Flor("Rosa", 1, "Rosa", "Rojo")


# MOSTRAR

print("Gato:", gato.nombre, gato.edad, gato.peso, gato.colorPelaje, gato.raza)
print("Leon:", leon.nombre, leon.edad, leon.peso, leon.colorPelaje, leon.melena)
print("Vivora:", vivora.nombre, vivora.edad, vivora.peso, vivora.escamas, vivora.venenosa)
print("Raton:", raton.nombre, raton.edad, raton.peso, raton.tamaño, raton.color)
print("Conejo:", conejo.nombre, conejo.edad, conejo.peso, conejo.tamaño, conejo.orejas)
print("Rana:", rana.nombre, rana.edad, rana.peso, rana.colorPiel)
print("Niño:", niño.nombre, niño.edad, niño.peso, niño.nacionalidad, niño.escuela)
print("Adulto:", adulto.nombre, adulto.edad, adulto.peso, adulto.nacionalidad, adulto.profesion)
print("Anciano:", anciano.nombre, anciano.edad, anciano.peso, anciano.nacionalidad, anciano.jubilado)
print("Flor:", flor.nombre, flor.edad, flor.tipo, flor.color)