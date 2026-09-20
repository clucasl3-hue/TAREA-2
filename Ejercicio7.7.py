class RegistroEstudiantes:

    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, nota):
        self.estudiantes[nombre] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for nombre, nota in self.estudiantes.items():
            if nota >= nota_minima:
                aprobados.append(nombre)

        return aprobados

    def nota_promedio(self):
        return sum(self.estudiantes.values()) / len(self.estudiantes)


registro = RegistroEstudiantes()

registro.agregar_estudiante("Carlos", 80)
registro.agregar_estudiante("Ana", 95)
registro.agregar_estudiante("Luis", 60)
registro.agregar_estudiante("Maria", 75)

print(registro.estudiantes)
print(registro.estudiantes_aprobados(70))
print(registro.nota_promedio())
