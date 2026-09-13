"""¿12 es divisible por 1?
  Sí → 12 % 1 = 0 ✓
  Divisores = [1]

¿12 es divisible por 2?
  Sí → 12 % 2 = 0 ✓
  Divisores = [1, 2]

¿12 es divisible por 3?
  Sí → 12 % 3 = 0 ✓
  Divisores = [1, 2, 3]

¿12 es divisible por 4?
  Sí → 12 % 4 = 0 ✓
  Divisores = [1, 2, 3, 4]

¿12 es divisible por 5?
  No ✗

¿12 es divisible por 6?
  Sí ✓
  Divisores = [1, 2, 3, 4, 6]

¿12 es divisible por 7?
  No ✗

¿12 es divisible por 8?
  No ✗

¿12 es divisible por 9?
  No ✗

¿12 es divisible por 10?
  No ✗

¿12 es divisible por 11?
  No ✗

¿12 es divisible por 12?
  Sí ✓
  Divisores = [1, 2, 3, 4, 6, 12]

Resultado:
  (1, 2, 3, 4, 6, 12) ✓"""


class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        suma = 0

        for i in range(1, numero):
            if numero % i == 0:
                suma += i

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado

df = DivisorFinder()

print(df.encontrar_divisores(12))
print(df.es_perfecto(6))
print(df.encontrar_multiples_divisores(6, 10, 12))
