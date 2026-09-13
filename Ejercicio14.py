"""Registrando estudiante: Ana
  Nota: 95
  Registro actual: {'Ana': 95}

Registrando estudiante: Bob
  Nota: 70
  Registro actual: {'Ana': 95, 'Bob': 70}


Buscando al estudiante con la mejor nota...

Estudiante: Ana
  Nota: 95
  ¿95 > 0? Sí ✓
  Nuevo mejor estudiante: Ana

Estudiante: Bob
  Nota: 70
  ¿70 > 95? No ✗

Mejor estudiante:
  Ana → 95 ✓

Resultado:
  ('Ana', 95)


Buscando estudiantes aprobados...
  Nota mínima: 70

¿Ana tiene una nota >= 70?
  95 >= 70 → Sí ✓

¿Bob tiene una nota >= 70?
  70 >= 70 → Sí ✓

Estudiantes aprobados:
  ['Ana', 'Bob']

Resultado:
  ['Ana', 'Bob'] ✓"""


class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        mejor_nombre = None
        mejor_nota = 0

        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)

rn = RegistroNotas()

rn.registrar("Ana", 95)
rn.registrar("Bob", 70)

print(rn.mejor_estudiante())
print(rn.estudiantes_aprobados(70))
