"""BOSQUEJO:

1. Se crea el objeto:
   cd = CalculadorDistancia()

2. Se calcula la distancia entre (0,0) y (3,4):

   Fórmula:
   √((3 - 0)² + (4 - 0)²)

   = √(3² + 4²)
   = √(9 + 16)
   = √25
   = 5.0

   Se guarda 5.0 en la lista de distancias.

3. Se busca el punto más cercano a (0,0):

   Primer punto:
   (3,4)

   Distancia:
   √((3-0)² + (4-0)²)
   = √(9 + 16)
   = √25
   = 5.0

   Punto cercano actual:
   (3,4)

4. Se revisa el siguiente punto:

   Punto:
   (1,1)

   Distancia:
   √((1-0)² + (1-0)²)
   = √(1 + 1)
   = √2
   = 1.4142...

   Se compara:
   1.4142 < 5.0 → Sí

   Entonces:
   punto_cercano = (1,1)
   distancia_minima = 1.4142...

5. Se revisa el último punto:

   Punto:
   (5,5)

   Distancia:
   √((5-0)² + (5-0)²)
   = √(25 + 25)
   = √50
   = 7.0710...

   Se compara:
   7.0710 < 1.4142 → No

   El punto más cercano sigue siendo:
   (1,1)

6. Se muestran todas las distancias calculadas:

   Primera llamada:
   5.0

   En punto_mas_cercano:
   distancia a (3,4) = 5.0
   distancia a (1,1) = 1.4142...
   distancia a (5,5) = 7.0710...

RESULTADO FINAL:

5.0

(1, 1)

[5.0, 5.0, 1.4142135623730951, 7.0710678118654755]"""


import math

class CalculadorDistancia:

    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        distancia = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = puntos[0]
        distancia_minima = self.distancia_euclidiana(referencia, punto_cercano)

        for punto in puntos[1:]:
            distancia = self.distancia_euclidiana(referencia, punto)

            if distancia < distancia_minima:
                distancia_minima = distancia
                punto_cercano = punto

        return punto_cercano

cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0, 0), (3, 4)))

print(cd.punto_mas_cercano(
    (0, 0),
    (3, 4),
    (1, 1),
    (5, 5)
))

print(cd.distancias)
