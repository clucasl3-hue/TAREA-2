class RegistroPuntajes:

    def __init__(self):
        self.puntajes = {}

    def registrar(self, jugador, puntaje):
        self.puntajes[jugador] = puntaje

    def jugadores_destacados(self, puntaje_minimo):
        destacados = []

        for jugador, puntaje in self.puntajes.items():
            if puntaje >= puntaje_minimo:
                destacados.append(jugador)

        return destacados

    def mejor_jugador(self):
        mejor = ""
        mayor_puntaje = 0

        for jugador, puntaje in self.puntajes.items():
            if puntaje > mayor_puntaje:
                mayor_puntaje = puntaje
                mejor = jugador

        return mejor, mayor_puntaje


r = RegistroPuntajes()

r.registrar("Carlos", 85)
r.registrar("Ana", 95)
r.registrar("Luis", 78)
r.registrar("Maria", 90)

print(r.puntajes)

print(r.jugadores_destacados(85))

print(r.mejor_jugador())
