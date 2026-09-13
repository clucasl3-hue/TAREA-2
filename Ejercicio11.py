"""Agregando elemento: 'a'
  ¿'a' ya existe? No ✗
  Se agrega 'a' con frecuencia 1
  Diccionario actual: {'a': 1}

Agregando elemento: 'b'
  ¿'b' ya existe? No ✗
  Se agrega 'b' con frecuencia 1
  Diccionario actual: {'a': 1, 'b': 1}

Agregando elemento: 'a'
  ¿'a' ya existe? Sí ✓
  Frecuencia de 'a': 2
  Diccionario actual: {'a': 2, 'b': 1}


Buscando el elemento más frecuente...

Elemento: 'a'
  Frecuencia: 2
  2 > 0 → Sí ✓
  Nuevo elemento más frecuente: 'a'

Elemento: 'b'
  Frecuencia: 1
  1 > 2 → No ✗

Resultado: 'a' es el más frecuente ✓

a


Buscando frecuencia de 'a'...
  ¿'a' existe? Sí ✓
  Frecuencia: 2

2"""


class ContadorFrecuencia:

    def __init__(self):
        self.elementos = {}

    def agregar_elemento(self, elemento):
        if elemento in self.elementos:
            self.elementos[elemento] += 1
        else:
            self.elementos[elemento] = 1

    def elemento_mas_frecuente(self):
        mayor = 0
        elemento_mayor = None

        for elemento in self.elementos:
            if self.elementos[elemento] > mayor:
                mayor = self.elementos[elemento]
                elemento_mayor = elemento

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.elementos:
            return self.elementos[elemento]
        else:
            return 0

cf = ContadorFrecuencia()

cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")

print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))
