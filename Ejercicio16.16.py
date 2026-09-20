class TransformadorLetras:

    def __init__(self):
        self.historial = {}

    def mover_letra(self, letra, desplazamiento):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"

        posicion = alfabeto.index(letra)
        nueva_posicion = (posicion + desplazamiento) % 26

        return alfabeto[nueva_posicion]

    def mover_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.mover_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


t = TransformadorLetras()

print(t.mover_letra("a", 3))

print(t.mover_palabra("hola", 3))

print(t.mover_palabra("casa", 2))

print(t.historial)
