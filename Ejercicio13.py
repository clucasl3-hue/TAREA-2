"""INTERCALAR DOS LISTAS

Lista 1:
  [1, 2]

Lista 2:
  [3, 4]


Posición 0:
  Tomamos 1
  Tomamos 3
  Resultado = [1, 3]

Posición 1:
  Tomamos 2
  Tomamos 4
  Resultado = [1, 3, 2, 4]


Resultado:
  [1, 3, 2, 4] ✓"""


class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []

        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []

        for i in range(len(listas[0])):
            for lista in listas:
                resultado.append(lista[i])

        return resultado

cl = CombinadorListas()

print(cl.intercalar([1, 2], [3, 4]))
print(cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))
