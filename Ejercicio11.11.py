class ContadorVotos:

    def __init__(self):
        self.votos = {}

    def registrar_voto(self, candidato):
        if candidato in self.votos:
            self.votos[candidato] += 1
        else:
            self.votos[candidato] = 1

    def candidato_mas_votado(self):
        mayor = ""
        cantidad = 0

        for candidato, votos in self.votos.items():
            if votos > cantidad:
                cantidad = votos
                mayor = candidato

        return mayor

    def votos_candidato(self, candidato):
        if candidato in self.votos:
            return self.votos[candidato]
        else:
            return 0


contador = ContadorVotos()

contador.registrar_voto("Ana")
contador.registrar_voto("Luis")
contador.registrar_voto("Ana")
contador.registrar_voto("Carlos")
contador.registrar_voto("Ana")
contador.registrar_voto("Luis")

print(contador.votos)
print(contador.candidato_mas_votado())
print(contador.votos_candidato("Ana"))
