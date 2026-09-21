class AnalizadorFrases:

    def __init__(self):
        self.palabras = []

    def buscar_palabras(self, texto, inicio):
        resultado = []

        for palabra in texto.split():
            if palabra.startswith(inicio):
                resultado.append(palabra)

        return resultado

    def agrupar_palabras(self, texto):
        resultado = {}

        self.palabras = texto.split()

        for palabra in self.palabras:
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_sin_repetir(self):
        return set(self.palabras)


a = AnalizadorFrases()

texto = "casa carro camino perro casa sol"

print(a.buscar_palabras(texto, "ca"))

print(a.agrupar_palabras(texto))

print(a.palabras_sin_repetir())
