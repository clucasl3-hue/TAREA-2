class Peliculas:

    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, nombre, genero):
        pelicula = (nombre, genero)
        self.peliculas.append(pelicula)

    def peliculas_accion(self):
        accion = []

        for pelicula in self.peliculas:
            if pelicula[1] == "Accion":
                accion.append(pelicula)

        return accion

    def eliminar_pelicula(self, nombre):
        for pelicula in self.peliculas:
            if pelicula[0] == nombre:
                self.peliculas.remove(pelicula)
                break


peliculas = Peliculas()

peliculas.agregar_pelicula("Avatar", "Ciencia Ficcion")
peliculas.agregar_pelicula("Avengers", "Accion")
peliculas.agregar_pelicula("Batman", "Accion")

print(peliculas.peliculas)
print(peliculas.peliculas_accion())

peliculas.eliminar_pelicula("Avengers")

print(peliculas.peliculas)
