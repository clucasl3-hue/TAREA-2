class CombinadorNombres:

    def intercalar(self, lista1, lista2):
        resultado = []

        i = 0

        while i < len(lista1) and i < len(lista2):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

            i += 1

        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1

        while i < len(lista2):
            resultado.append(lista2[i])
            i += 1

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = listas[0]

        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)

        return resultado


c = CombinadorNombres()

lista1 = ["Ana", "Luis", "Pedro"]
lista2 = ["Sofia", "Carlos", "Maria"]

print(c.intercalar(lista1, lista2))

lista3 = ["Juan", "Elena"]

print(c.intercalar_multiples(lista1, lista2, lista3))
