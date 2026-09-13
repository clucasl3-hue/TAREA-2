"""Agregando tarea: Estudiar
  Prioridad: alta
  Lista actual: [('Estudiar', 'alta')]

Agregando tarea: Leer
  Prioridad: baja
  Lista actual: [('Estudiar', 'alta'), ('Leer', 'baja')]


Buscando tareas prioritarias...

Tarea: Estudiar
  Prioridad: alta
  ¿La prioridad es alta? Sí ✓

Tarea: Leer
  Prioridad: baja
  ¿La prioridad es alta? No ✗

Tareas prioritarias:
  [('Estudiar', 'alta')]

[('Estudiar', 'alta')]


Buscando tarea para eliminar: Estudiar

  ¿'Estudiar' es 'Estudiar'?
  Sí → tarea encontrada ✓
  Tarea eliminada ✓


[]"""


class Tareas:

    def __init__(self):
        self.lista = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        prioritarias = []

        for tarea in self.lista:
            if tarea[1] == "alta":
                prioritarias.append(tarea)

        return prioritarias

    def eliminar_completada(self, descripcion):
        for tarea in self.lista:
            if tarea[0] == descripcion:
                self.lista.remove(tarea)
                break

t = Tareas()

t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")

print(t.tareas_prioritarias())

t.eliminar_completada("Estudiar")

print(t.lista)
