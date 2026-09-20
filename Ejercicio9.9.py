class AnalizadorCaracteres:

    def __init__(self):
        self.texto_largo = ""

    def es_numero(self, caracter):
        if caracter.isdigit():
            return True
        else:
            return False

    def contar_por_tipo(self, texto):
        numeros = 0
        letras = 0
        espacios = 0

        for caracter in texto:
            if self.es_numero(caracter):
                numeros += 1
            elif caracter.isalpha():
                letras += 1
            elif caracter == " ":
                espacios += 1

        if len(texto) > len(self.texto_largo):
            self.texto_largo = texto

        return {
            "numeros": numeros,
            "letras": letras,
            "espacios": espacios
        }


analizador = AnalizadorCaracteres()

print(analizador.contar_por_tipo("Hola 123"))
print(analizador.contar_por_tipo("Python 2026"))

print("Texto más largo:", analizador.texto_largo)
