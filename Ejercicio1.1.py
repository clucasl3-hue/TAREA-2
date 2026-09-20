class RegistroTemperaturas:

    def __init__(self):
        self.temperaturas = []

    def validar_temperatura(self, temperatura):
        if -50 <= temperatura <= 50:
            return True
        else:
            return False

    def cargar_temperaturas(self, *args):
        for temperatura in args:
            if self.validar_temperatura(temperatura):
                self.temperaturas.append(temperatura)

        return self.temperaturas

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


registro = RegistroTemperaturas()

print(registro.cargar_temperaturas(20, 25, 70, -10, 30, 80))
print(registro.promedio())
