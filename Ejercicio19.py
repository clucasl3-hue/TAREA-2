"""BOSQUEJO:

1. Se crea el objeto:
   inv = Inventario()

2. Se agrega stock de "pan":

   Producto = "pan"
   Cantidad = 50

   "pan" no existe en el inventario.

   Entonces:
   productos["pan"] = 50

   Inventario:
   {"pan": 50}

3. Se resta stock de "pan":

   Producto = "pan"
   Cantidad a restar = 30

   Se verifica:
   "pan" existe → Sí
   50 >= 30 → Sí

   Entonces:
   50 - 30 = 20

   Stock de pan:
   20

   Retorna:
   True

4. Se buscan productos con bajo stock:

   minimo = 15

   Se revisa "pan":
   cantidad = 20

   Se compara:
   20 < 15 → No

   Por lo tanto, "pan" no se agrega a la lista.

5. Resultado de productos_bajo_stock:

   []

RESULTADO FINAL:

True
[]"""


class Inventario:

    def __init__(self):
        self.productos = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.productos and self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            return True
        else:
            return False

    def productos_bajo_stock(self, minimo):
        productos_bajos = []

        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                productos_bajos.append(producto)

        return productos_bajos

inv = Inventario()

inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.productos_bajo_stock(15))
