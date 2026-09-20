class AnalizadorNumeros:

    def buscar_factores(self, numero):
        factores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                factores.append(i)

        return tuple(factores)

    def es_equilibrado(self, numero):
        factores = self.buscar_factores(numero)

        suma = 0

        for factor in factores:
            if factor != numero:
                suma += factor

        return suma == numero

    def buscar_multiples_factores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.buscar_factores(numero)

        return resultado


a = AnalizadorNumeros()

print(a.buscar_factores(12))

print(a.es_equilibrado(6))

print(a.buscar_multiples_factores(6, 10, 12))
