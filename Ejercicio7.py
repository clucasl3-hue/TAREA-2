"""Agregando persona: Ana
  Edad: 28
  Personas actuales: {'Ana': 28}

Agregando persona: Bob
  Edad: 17
  Personas actuales: {'Ana': 28, 'Bob': 17}


Buscando personas con edad mayor o igual a 18...

¿Ana tiene 28 años y cumple con la edad mínima?
  28 >= 18 → Sí ✓

¿Bob tiene 17 años y cumple con la edad mínima?
  17 >= 18 → No ✗

Personas mayores encontradas:
  ['Ana']

['Ana']


Calculando edad promedio...
  Edades: [28, 17]
  Suma de edades: 45
  Cantidad de personas: 2
  Promedio: 22.5

22.5"""


class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        lista = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                lista.append(nombre)

        return lista

    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0

        suma = sum(self.personas.values())
        return suma / len(self.personas)

gp = GestorPersonas()

gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)

print(gp.personas_mayores(18))
print(gp.edad_promedio())
