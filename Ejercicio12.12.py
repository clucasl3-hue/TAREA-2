class SelectorLetras:

    def __init__(self):
        self.letras = "abcdefghijklmnopqrstuvwxyz"

    def crear_rango_letras(self, inicio, fin):
        return tuple(self.letras[inicio:fin])

    def letras_en_multiples_rangos(self, *rangos):
        resultado = set()

        for inicio, fin in rangos:
            rango = self.crear_rango_letras(inicio, fin)

            for letra in rango:
                resultado.add(letra)

        return list(resultado)


selector = SelectorLetras()

print(selector.crear_rango_letras(0, 5))
print(selector.letras_en_multiples_rangos((0, 5), (3, 8), (10, 13)))
