class CalculadorTiempo:

    def __init__(self):
        self.diferencias = []

    def diferencia_horas(self, hora1, hora2):
        minutos1 = hora1[0] * 60 + hora1[1]
        minutos2 = hora2[0] * 60 + hora2[1]

        diferencia = abs(minutos1 - minutos2)

        self.diferencias.append(diferencia)

        return diferencia

    def hora_mas_cercana(self, referencia, *horas):
        menor_diferencia = None
        hora_cercana = None

        for hora in horas:
            diferencia = self.diferencia_horas(referencia, hora)

            if menor_diferencia is None or diferencia < menor_diferencia:
                menor_diferencia = diferencia
                hora_cercana = hora

        return hora_cercana


c = CalculadorTiempo()

print(c.diferencia_horas((10, 30), (11, 15)))

print(c.hora_mas_cercana(
    (10, 30),
    (9, 45),
    (10, 20),
    (11, 30)
))

print(c.diferencias)
