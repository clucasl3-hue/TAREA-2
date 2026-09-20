class Cursos:

    def __init__(self):
        self.cursos = {}

    def crear_curso(self, nombre_curso):
        self.cursos[nombre_curso] = []

    def agregar_estudiante(self, curso, estudiante):
        self.cursos[curso].append(estudiante)

    def curso_mayor_estudiantes(self):
        mayor = ""
        cantidad = 0

        for curso, estudiantes in self.cursos.items():
            if len(estudiantes) > cantidad:
                cantidad = len(estudiantes)
                mayor = curso

        return mayor


cursos = Cursos()

cursos.crear_curso("Python")
cursos.crear_curso("Java")
cursos.crear_curso("JavaScript")

cursos.agregar_estudiante("Python", "Ana")
cursos.agregar_estudiante("Python", "Carlos")
cursos.agregar_estudiante("Python", "Luis")

cursos.agregar_estudiante("Java", "Maria")
cursos.agregar_estudiante("Java", "Pedro")

cursos.agregar_estudiante("JavaScript", "Juan")

print(cursos.cursos)
print(cursos.curso_mayor_estudiantes())
