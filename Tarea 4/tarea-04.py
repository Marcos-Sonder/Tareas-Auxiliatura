class Anuncio:
    def __init__(self, num=0, pre=0.1):
        self.__numero = num
        self.__precio = pre

    def getNumero(self):
        return self.__numero

    def getPrecio(self):
        return self.__precio


class Artista:
    def __init__(self, nom, car, anios):
        self.__nombre = nom
        self.__ci = car
        self.__aniosExp = anios

    def getNombre(self):
        return self.__nombre

    def getCi(self):
        return self.__ci

    def getAnios(self):
        return self.__aniosExp


class Obra:
    def __init__(self, titulo, material, nom1, car1, anio1,
                 nom2, car2, anio2):
        self._titulo = titulo
        self._material = material
        self._artista1 = Artista(nom1, car1, anio1)
        self._artista2 = Artista(nom2, car2, anio2)
        self._anuncio = None

    def agregarAnuncio(self, anun):
        self._anuncio = anun

    def getAnuncio(self):
        return self._anuncio

    def getArt1(self):
        return self._artista1

    def getArt2(self):
        return self._artista2

    def getTitulo(self):
        return self._titulo


class Pintura(Obra):
    def __init__(self, titulo: str, material: str, nom1, car1, anio1,
                 nom2, car2, anio2, gen):
        super().__init__(titulo, material, nom1, car1, anio1,
                         nom2, car2, anio2)
        self.__genero = gen


# Inciso b jjj
def artistaConMasExperiencia(pintura1, pintura2):
    artistas = [
        pintura1.getArt1(), pintura1.getArt2(),
        pintura2.getArt1(), pintura2.getArt2()
    ]
    return max(artistas, key=lambda artista: artista.getAnios())


# Inciso c jjj
def montoTotalVenta(pintura1, pintura2):
    total = 0
    for pintura in (pintura1, pintura2):
        anuncio = pintura.getAnuncio()
        if anuncio is not None:
            total += anuncio.getPrecio()
    return total


if __name__ == "__main__":
    # Inciso a
    a1 = Anuncio()          
    a2 = Anuncio(2, 2.3)    

    p1 = Pintura("monalisa", "oleo",
                 "davinci", 123, 20, "joel", 321, 1, "intriga")
    p2 = Pintura("monalisa", "oleo",
                 "davinci", 123, 20, "adrian", 444, 4, "cuatro")

    p2.agregarAnuncio(a1)

    
    artista = artistaConMasExperiencia(p1, p2)
    print("Artista con más experiencia:", artista.getNombre())
    print("Años de experiencia:", artista.getAnios())

    p1.agregarAnuncio(a2)
    print("Monto total de venta:", montoTotalVenta(p1, p2))
