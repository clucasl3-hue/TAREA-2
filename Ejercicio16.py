"""Palabra original:
  hola

Desplazamiento:
  3

Codificando letra por letra...

Letra: 'h'
  h → k
  Palabra hasta ahora: k

Letra: 'o'
  o → r
  Palabra hasta ahora: kr

Letra: 'l'
  l → o
  Palabra hasta ahora: kro

Letra: 'a'
  a → d
  Palabra hasta ahora: krod

Resultado:
  hola → krod ✓

Historial:
  {'hola': 'krod'}"""


class CodificadorCesar:

    def __init__(self):

        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):

        codigo = ord(letra)

        nuevo_codigo = (codigo - ord('a') + desplazamiento) % 26 + ord('a')

        return chr(nuevo_codigo)

    def codificar_palabra(self, palabra, desplazamiento):
        palabra_codificada = ""

        for letra in palabra:
            palabra_codificada += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = palabra_codificada

        return palabra_codificada

cc = CodificadorCesar()

palabra = input("Ingrese una palabra: ")
desplazamiento = int(input("Ingrese el desplazamiento (1-25): "))

resultado = cc.codificar_palabra(palabra, desplazamiento)

print("Palabra codificada:", resultado)
print("Historial:", cc.historial)
