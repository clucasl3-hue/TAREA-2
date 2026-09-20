class RegistroCalificaciones:

    def __init__(self):
        self.notas = []

    def registrar_nota(self, nota):
        self.notas.append(nota)

    def minima(self):
        return min(self.notas)

    def maxima(self):
        return max(self.notas)

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def registrar_multiples(self, *notas):
        for nota in notas:
            self.registrar_nota(nota)


registro = RegistroCalificaciones()

registro.registrar_nota(80)
registro.registrar_nota(90)

registro.registrar_multiples(70, 85, 95)

print(registro.notas)
print("Nota mínima:", registro.minima())
print("Nota máxima:", registro.maxima())
print("Promedio:", registro.promedio())
