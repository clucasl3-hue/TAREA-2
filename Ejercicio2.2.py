class RegistroColores:

    def __init__(self):
        self.colores_unicos = set()
        self.lista_colores = []

    def agregar_color(self, color):
        self.colores_unicos.add(color)
        self.lista_colores.append(color)

    def contar_colores(self):
        return len(self.colores_unicos)

    def agregar_multiples(self, *args):
        for color in args:
            self.agregar_color(color)


registro = RegistroColores()

registro.agregar_color("rojo")
registro.agregar_color("azul")

registro.agregar_multiples("verde", "rojo", "amarillo")

print(registro.lista_colores)
print(registro.colores_unicos)
print(registro.contar_colores())
