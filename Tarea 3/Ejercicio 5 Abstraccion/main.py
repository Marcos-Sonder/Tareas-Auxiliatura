from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def obtenerArea(self):
        pass

class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def obtenerArea(self):
        return self.lado * self.lado

class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtenerArea(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s-self.lado1) * (s-self.lado2) * (s-self.lado3))

class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def obtenerArea(self):
        return math.pi * self.radio ** 2

cuadrado1 = Cuadrado("Rojo", 4)
cuadrado2 = Cuadrado("Azul", 3)
triangulo1 = Triangulo("Verde", 3, 4, 5)
triangulo2 = Triangulo("Amarillo", 5, 5, 6)
redondo1 = Redondo("Morado", 3)
redondo2 = Redondo("Naranja", 5)

for figura in [cuadrado1, cuadrado2, triangulo1, triangulo2, redondo1, redondo2]:
    print(type(figura).__name__, "- Color:", figura._color, "- Area:", round(figura.obtenerArea(), 2))

if cuadrado1.obtenerArea() > triangulo1.obtenerArea():
    print("La figura con mayor area es el cuadrado. Color:", cuadrado1._color)
elif triangulo1.obtenerArea() > cuadrado1.obtenerArea():
    print("La figura con mayor area es el triangulo. Color:", triangulo1._color)
else:
    print("Ambas figuras tienen la misma area")
