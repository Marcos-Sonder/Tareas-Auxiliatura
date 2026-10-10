class Animal:
    def __init__(self, edad, peso, especie):
        self.edad = edad
        self.peso = peso
        self.especie = especie

    def respirar(self):
        print("El animal toma oxigeno para respirar")

    def mover(self):
        print("El animal se mueve")

    def mostrarDatos(self):
        print("Especie:", self.especie)
        print("Edad:", self.edad)
        print("Peso:", self.peso)

class Terrestre(Animal):
    def __init__(self, edad, peso, especie, numeroPatas, velocidad):
        super().__init__(edad, peso, especie)
        self.numeroPatas = numeroPatas
        self.velocidad = velocidad

    def respirar(self):
        print("El", self.especie, "respira mediante pulmones")

    def mover(self):
        print("El", self.especie, "camina o corre por la tierra")

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Numero de patas:", self.numeroPatas)
        print("Velocidad:", self.velocidad)

class Acuatico(Animal):
    def __init__(self, edad, peso, especie, tipoAletas, profundidad):
        super().__init__(edad, peso, especie)
        self.tipoAletas = tipoAletas
        self.profundidad = profundidad

    def respirar(self):
        print("El", self.especie, "respira mediante branquias")

    def mover(self):
        print("El", self.especie, "nada en el agua")

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Tipo de aletas:", self.tipoAletas)
        print("Profundidad:", self.profundidad)

class Aereo(Animal):
    def __init__(self, edad, peso, especie, envergadura, alturaVuelo):
        super().__init__(edad, peso, especie)
        self.envergadura = envergadura
        self.alturaVuelo = alturaVuelo

    def respirar(self):
        print("El", self.especie, "respira mediante pulmones y sacos aereos")

    def mover(self):
        print("El", self.especie, "vuela por el aire")

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Envergadura:", self.envergadura)
        print("Altura de vuelo:", self.alturaVuelo)

animal1 = Terrestre(5, 20, "Perro", 4, 30)
animal2 = Acuatico(3, 15, "Pez", "Aletas dorsales", 100)
animal3 = Aereo(2, 1, "Aguila", 2, 3000)

for animal in [animal1, animal2, animal3]:
    print("\n===", type(animal).__name__, "===")
    animal.mostrarDatos()
    animal.respirar()
    animal.mover()
