class Auto:
    def __init__(self, marca, color="Blanco", gasolina=0):
        self.marca = marca
        self.color = color
        self.gasolina = gasolina

    def __iadd__(self, valor):
        self.gasolina += 5
        return self

    def __add__(self, color):
        self.color = color
        return self

    def __sub__(self, otro):
        return self.gasolina + otro.gasolina

    def mostrar(self):
        print("Marca:", self.marca)
        print("Color:", self.color)
        print("Gasolina:", self.gasolina, "litros")
        print()


auto1 = Auto("Toyota")
auto2 = Auto("Nissan", "Rojo", 20)

print("DATOS INICIALES")
auto1.mostrar()
auto2.mostrar()

auto1 += 1

print("DESPUES DE INCREMENTAR GASOLINA")
auto1.mostrar()

auto2 = auto2 + "Azul"

print("DESPUES DE CAMBIAR EL COLOR")
auto2.mostrar()

total = auto1 - auto2

print("TOTAL DE GASOLINA DE LOS 2 AUTOS:", total, "litros")