"""Separando números...

¿El número 1 es par?
  1 % 2 != 0
  Resultado: NO, 1 es impar ✓
  Impares: [1]

¿El número 2 es par?
  2 % 2 = 0
  Resultado: SÍ, 2 es par ✓
  Pares: [2]

¿El número 3 es par?
  3 % 2 != 0
  Resultado: NO, 3 es impar ✓
  Impares: [1, 3]

¿El número 4 es par?
  4 % 2 = 0
  Resultado: SÍ, 4 es par ✓
  Pares: [2, 4]

¿El número 5 es par?
  5 % 2 != 0
  Resultado: NO, 5 es impar ✓
  Impares: [1, 3, 5]

Resultado final:
  Pares: [2, 4]
  Impares: [1, 3, 5]

Contando cantidades...
  Cantidad de pares: 2
  Cantidad de impares: 3
  Resultado: (2, 3) ✓"""


class AnalizadorNumeros:

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        resultado = {
            'pares': [],
            'impares': []
        }

        for numero in numeros:
            if self.es_par(numero):
                resultado['pares'].append(numero)
            else:
                resultado['impares'].append(numero)

        return resultado

    def cantidad_pares_impares(self, *numeros):
        resultado = self.separar(*numeros)

        cantidad_pares = len(resultado['pares'])
        cantidad_impares = len(resultado['impares'])

        return (cantidad_pares, cantidad_impares)

an = AnalizadorNumeros()

print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares(1, 2, 3, 4, 5))
