"""
Cargando notas...

¿La nota 85 es válida?
  ¿Está entre 0 y 100? Sí
  Resultado: 85 es válida ✓

¿La nota 92 es válida?
  ¿Está entre 0 y 100? Sí
  Resultado: 92 es válida ✓

¿La nota 110 es válida?
  ¿Está entre 0 y 100? No
  Resultado: 110 es inválida ✗

¿La nota 78 es válida?
  ¿Está entre 0 y 100? Sí
  Resultado: 78 es válida ✓

¿La nota -5 es válida?
  ¿Está entre 0 y 100? No
  Resultado: -5 es inválida ✗

¿La nota 88 es válida?
  ¿Está entre 0 y 100? Sí
  Resultado: 88 es válida ✓

Calculando promedio...
  Notas válidas: [85, 92, 78, 88]
  Suma: 343
  Cantidad de notas: 4
  Promedio: 85.75"""


class Calificador:
    def __init__(self):
        self.calificaciones = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

c = Calificador()
c.cargar_notas(85, 92, 110, 78, -5, 88)
c.promedio() 
