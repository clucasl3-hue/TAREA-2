"""Lista original: [1, 2, 3]

Invirtiendo lista...

Posición 2 → valor 3
  Lista invertida hasta ahora: [3]

Posición 1 → valor 2
  Lista invertida hasta ahora: [3, 2]

Posición 0 → valor 1
  Lista invertida hasta ahora: [3, 2, 1]

Resultado: [3, 2, 1] ✓

[3, 2, 1]"""


class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado[tuple(lista)] = invertida

        return resultado

inv = InversorSecuencia()

print(inv.invertir_lista([1, 2, 3]))
