class ClasificadorEdades:

    def __init__(self):
        self.mayores = []
        self.menores = []

    def es_mayor(self, edad):
        if edad >= 18:
            return True
        else:
            return False

    def separar_edades(self, *edades):
        for edad in edades:
            if self.es_mayor(edad):
                self.mayores.append(edad)
            else:
                self.menores.append(edad)

        return {
            "mayores": self.mayores,
            "menores": self.menores
        }

    def cantidad_mayores_menores(self):
        return (len(self.mayores), len(self.menores))


clasificador = ClasificadorEdades()

print(clasificador.separar_edades(15, 20, 17, 25, 30, 12))
print(clasificador.cantidad_mayores_menores())
