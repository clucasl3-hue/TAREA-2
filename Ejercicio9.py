"""Analizando texto: 'Hola123'

Analizando letra: 'H'
  ¿Es un dígito? No
  ¿Es una letra? Sí ✓
  ¿Es vocal? No
  Resultado: consonante ✓
  Consonantes: 1

Analizando letra: 'o'
  ¿Es un dígito? No
  ¿Es una letra? Sí ✓
  ¿Es vocal? Sí ✓
  Vocales: 1

Analizando letra: 'l'
  ¿Es un dígito? No
  ¿Es una letra? Sí ✓
  ¿Es vocal? No
  Resultado: consonante ✓
  Consonantes: 2

Analizando letra: 'a'
  ¿Es un dígito? No
  ¿Es una letra? Sí ✓
  ¿Es vocal? Sí ✓
  Vocales: 2

Analizando letra: '1'
  ¿Es un dígito? Sí ✓
  Dígitos: 1

Analizando letra: '2'
  ¿Es un dígito? Sí ✓
  Dígitos: 2

Analizando letra: '3'
  ¿Es un dígito? Sí ✓
  Dígitos: 3

Resultado final:
  Vocales: 2
  Consonantes: 2
  Dígitos: 3

{'vocales': 2, 'consonantes': 2, 'digitos': 3}"""


class AnalizadorString:
    def __init__(self):
        self.texto = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        self.texto = texto

        conteo = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for letra in texto:
            if letra.isdigit():
                conteo["digitos"] += 1
            elif letra.isalpha():
                if self.solo_vocales(letra):
                    conteo["vocales"] += 1
                else:
                    conteo["consonantes"] += 1

        return conteo

astr = AnalizadorString()

print(astr.contar_por_tipo("Hola123"))
