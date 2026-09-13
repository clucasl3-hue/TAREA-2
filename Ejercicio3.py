"""Agregando artículo: pan
  Precio: $2.5
  Carrito actual: {'pan': 2.5}

Agregando artículo: leche
  Precio: $3.0
  Carrito actual: {'pan': 2.5, 'leche': 3.0}

Calculando total del carrito...

  Artículo: pan → $2.5
  Total acumulado: $2.5

  Artículo: leche → $3.0
  Total acumulado: $5.5

Resultado: Total del carrito = $5.5 ✓

5.5"""


class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        total = 0

        for precio in self.articulos.values():
            total = total + precio

        return total

    def articulos_por_rango(self, precio_min, precio_max):
        lista = []

        for nombre, precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                lista.append(nombre)

        return lista

c = CarroCompras()

c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)

print(c.total_carrito())
