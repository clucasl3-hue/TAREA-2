"""Registrando múltiples temperaturas...

Registrando temperatura: 20°
  Temperatura agregada ✓
  Temperaturas actuales: [20]

Registrando temperatura: 25°
  Temperatura agregada ✓
  Temperaturas actuales: [20, 25]

Registrando temperatura: 18°
  Temperatura agregada ✓
  Temperaturas actuales: [20, 25, 18]

Registrando temperatura: 30°
  Temperatura agregada ✓
  Temperaturas actuales: [20, 25, 18, 30]


Buscando temperatura mínima...
  Temperaturas: [20, 25, 18, 30]
  Mínima: 18° ✓

18


Buscando temperatura máxima...
  Temperaturas: [20, 25, 18, 30]
  Máxima: 30° ✓

30


Calculando promedio...
  Suma: 93
  Cantidad de temperaturas: 4
  Promedio: 23.25° ✓

23.25"""


class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

gt = GestorTemperatura()

gt.registrar_multiples(20, 25, 18, 30)

print(gt.minima())
print(gt.maxima())
print(gt.promedio())
