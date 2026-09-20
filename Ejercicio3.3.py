class ListaProductos:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def total_productos(self):
        total = 0

        for precio in self.productos.values():
            total += precio

        return total

    def productos_por_rango(self, precio_min, precio_max):
        productos = []

        for nombre, precio in self.productos.items():
            if precio_min <= precio <= precio_max:
                productos.append(nombre)

        return productos


lista = ListaProductos()

lista.agregar_producto("Cuaderno", 3.50)
lista.agregar_producto("Mochila", 25)
lista.agregar_producto("Esfero", 1.50)
lista.agregar_producto("Carpeta", 4)

print(lista.productos)
print(lista.total_productos())
print(lista.productos_por_rango(3, 10))
