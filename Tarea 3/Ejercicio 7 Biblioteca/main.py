class Documento:
    def __init__(self, titulo, autores, editorial, anioPublicacion):
        self.titulo = titulo
        self.autores = autores
        self.editorial = editorial
        self.anioPublicacion = anioPublicacion

    def mostrarDatos(self):
        print("Titulo:", self.titulo)
        print("Autores:", self.autores)
        print("Editorial:", self.editorial)
        print("Año de publicacion:", self.anioPublicacion)

class Libro(Documento):
    pass

class Revista(Documento):
    def __init__(self, titulo, autores, editorial, anioPublicacion, volumen, numero, mesSalida):
        super().__init__(titulo, autores, editorial, anioPublicacion)
        self.volumen = volumen
        self.numero = numero
        self.mesSalida = mesSalida

class DocumentoCD(Documento):
    def __init__(self, titulo, autores, editorial, anioPublicacion, formatoCD, tipoLicencia):
        super().__init__(titulo, autores, editorial, anioPublicacion)
        self.formatoCD = formatoCD
        self.tipoLicencia = tipoLicencia

class RevistaInvestigacion(Revista):
    def __init__(self, titulo, autores, editorial, anioPublicacion, volumen, numero, mesSalida, campoInvestigacion, anioPublicacionInvestigacion):
        super().__init__(titulo, autores, editorial, anioPublicacion, volumen, numero, mesSalida)
        self.campoInvestigacion = campoInvestigacion
        self.anioPublicacionInvestigacion = anioPublicacionInvestigacion

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = []

    def agregarDocumento(self, documento):
        self.documentos.append(documento)

    def contarRevistas(self):
        return sum(isinstance(d, Revista) for d in self.documentos)

    def contarDocumentos(self):
        return len(self.documentos)

    def trasladarRevistas(self, destino):
        for d in self.documentos[:]:
            if isinstance(d, Revista):
                destino.agregarDocumento(d)
                self.documentos.remove(d)

    def trasladarLibros(self, destino):
        for d in self.documentos[:]:
            if type(d) == Libro:
                destino.agregarDocumento(d)
                self.documentos.remove(d)

    def copiarSeguridad(self):
        copia = Biblioteca(self.nombre + " - Copia")
        for d in self.documentos:
            autores = d.autores.copy()
            if isinstance(d, RevistaInvestigacion):
                nuevo = RevistaInvestigacion(d.titulo, autores, d.editorial, d.anioPublicacion, d.volumen, d.numero, d.mesSalida, d.campoInvestigacion, d.anioPublicacionInvestigacion)
            elif isinstance(d, Revista):
                nuevo = Revista(d.titulo, autores, d.editorial, d.anioPublicacion, d.volumen, d.numero, d.mesSalida)
            elif isinstance(d, DocumentoCD):
                nuevo = DocumentoCD(d.titulo, autores, d.editorial, d.anioPublicacion, d.formatoCD, d.tipoLicencia)
            else:
                nuevo = Libro(d.titulo, autores, d.editorial, d.anioPublicacion)
            copia.agregarDocumento(nuevo)
        return copia

biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca2 = Biblioteca("Biblioteca Universitaria")

biblioteca1.agregarDocumento(Libro("Don Quijote", ["Cervantes"], "Clasicos", 1605))
biblioteca1.agregarDocumento(Revista("Ciencia Hoy", ["Ana Perez"], "Ciencia", 2024, 5, 2, "Mayo"))
biblioteca1.agregarDocumento(RevistaInvestigacion("Estudios Ambientales", ["Luis Rojas"], "Universidad", 2025, 2, 1, "Marzo", "Medio ambiente", 2025))
biblioteca1.agregarDocumento(DocumentoCD("Python", ["Juan Lopez"], "Educativa", 2023, "CD-ROM", "Libre"))

biblioteca2.agregarDocumento(Libro("El Principito", ["Saint-Exupery"], "Literaria", 1943))
biblioteca2.agregarDocumento(Libro("Cien años de soledad", ["Garcia Marquez"], "Sudamericana", 1967))
biblioteca2.agregarDocumento(Revista("Tecnologia", ["Maria Diaz"], "Tech", 2025, 3, 4, "Abril"))

print("=== ANTES DEL TRASLADO ===")
for b in [biblioteca1, biblioteca2]:
    print(b.nombre, "- Documentos:", b.contarDocumentos(), "- Revistas:", b.contarRevistas())

if biblioteca1.contarRevistas() > biblioteca2.contarRevistas():
    print("Mas revistas:", biblioteca1.nombre)
elif biblioteca2.contarRevistas() > biblioteca1.contarRevistas():
    print("Mas revistas:", biblioteca2.nombre)
else:
    print("Igual cantidad de revistas")

if biblioteca1.contarDocumentos() > biblioteca2.contarDocumentos():
    print("Mas documentos:", biblioteca1.nombre)
elif biblioteca2.contarDocumentos() > biblioteca1.contarDocumentos():
    print("Mas documentos:", biblioteca2.nombre)
else:
    print("Igual cantidad de documentos")

biblioteca2.trasladarRevistas(biblioteca1)
biblioteca1.trasladarLibros(biblioteca2)

print("\n=== DESPUES DEL TRASLADO ===")
for b in [biblioteca1, biblioteca2]:
    print(b.nombre, "- Documentos:", b.contarDocumentos(), "- Revistas:", b.contarRevistas())

copia1 = biblioteca1.copiarSeguridad()
copia2 = biblioteca2.copiarSeguridad()
print("\n=== COPIAS DE SEGURIDAD ===")
for b in [copia1, copia2]:
    print(b.nombre, "- Documentos:", b.contarDocumentos(), "- Revistas:", b.contarRevistas())
