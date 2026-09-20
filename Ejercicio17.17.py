class AgrupadorEstaturas:

    def __init__(self):
        self.estaturas = {}

    def clasificar_estatura(self, estatura):

        if estatura < 1.60:
            return "baja"
        elif estatura < 1.75:
            return "media"
        else:
            return "alta"

    def agrupar_por_categoria(self, *estaturas):

        self.estaturas = {
            "baja": [],
            "media": [],
            "alta": []
        }

        for estatura in estaturas:
            categoria = self.clasificar_estatura(estatura)
            self.estaturas[categoria].append(estatura)

        return self.estaturas

    def estatura_promedio_categoria(self, categoria):

        if categoria not in self.estaturas:
            return 0

        if len(self.estaturas[categoria]) == 0:
            return 0

        suma = sum(self.estaturas[categoria])
        promedio = suma / len(self.estaturas[categoria])

        return promedio


a = AgrupadorEstaturas()

print(a.clasificar_estatura(1.68))

print(a.agrupar_por_categoria(1.55, 1.62, 1.70, 1.80, 1.58, 1.75))

print(a.estatura_promedio_categoria("media"))
