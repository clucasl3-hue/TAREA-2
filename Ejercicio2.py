"""Agregando múltiples palabras...

Agregando palabra: 'hola'
  Set de palabras únicas: {'hola'}
  Lista de palabras: ['hola']

Agregando palabra: 'mundo'
  Set de palabras únicas: {'hola', 'mundo'}
  Lista de palabras: ['hola', 'mundo']

Agregando palabra: 'hola'
  Set de palabras únicas: {'hola', 'mundo'}
  Lista de palabras: ['hola', 'mundo', 'hola']

Contando palabras únicas...
  Palabras únicas: {'hola', 'mundo'}
  Cantidad de palabras únicas: 2"""


class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.lista_palabras = []

    def agregar_palabra(self, palabra): 
        self.palabras_unicas.add(palabra)
        self.lista_palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, * args):
        for palabra in args:
            self.agregar_palabra(palabra)

at = AnalizadorTexto()
at.agregar_multiples("hola","mundo","hola")
at.contar_palabras()
