class OrganizadorListas:

    def ordenar_al_reves(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_varias(self, *listas):
        resultado = {}

        for lista in listas:
            invertida = self.ordenar_al_reves(lista)
            resultado[str(lista)] = invertida

        return resultado


organizador = OrganizadorListas()

lista1 = [1, 2, 3, 4]
lista2 = ["a", "b", "c"]

print(organizador.ordenar_al_reves(lista1))
print(organizador.invertir_varias(lista1, lista2))
