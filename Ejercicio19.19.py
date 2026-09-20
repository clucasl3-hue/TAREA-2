class Biblioteca:

    def __init__(self):
        self.libros = {}

    def agregar_libros(self, libro, cantidad):
        if libro in self.libros:
            self.libros[libro] += cantidad
        else:
            self.libros[libro] = cantidad

    def prestar_libros(self, libro, cantidad):
        if libro in self.libros and self.libros[libro] >= cantidad:
            self.libros[libro] -= cantidad
            return True
        else:
            return False

    def libros_bajo_stock(self, minimo):
        resultado = []

        for libro, cantidad in self.libros.items():
            if cantidad < minimo:
                resultado.append(libro)

        return resultado


b = Biblioteca()

b.agregar_libros("Don Quijote", 10)
b.agregar_libros("El Principito", 5)
b.agregar_libros("Harry Potter", 8)

print(b.libros)

print(b.prestar_libros("Don Quijote", 3))

print(b.libros)

print(b.libros_bajo_stock(8))
