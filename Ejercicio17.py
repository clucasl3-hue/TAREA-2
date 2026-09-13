""" BOSQUEJO:

1. Se crea el objeto:
   ae = AgrupadorEdades()

2. Se llama:
   ae.agrupar_por_categoria(5, 15, 30, 70)

3. Se revisa cada edad:

   Edad = 5
   5 < 12 → niño
   niño = [5]

   Edad = 15
   15 < 12 → No
   15 < 18 → Sí
   adolescente = [15]

   Edad = 30
   30 < 12 → No
   30 < 18 → No
   30 < 65 → Sí
   adulto = [30]

   Edad = 70
   70 < 12 → No
   70 < 18 → No
   70 < 65 → No
   70 >= 65 → mayor
   mayor = [70]

4. Resultado de la agrupación:

   niño = [5]
   adolescente = [15]
   adulto = [30]
   mayor = [70]

5. Se llama:
   ae.edad_promedio_categoria("adulto")

6. Se obtiene la categoría adulto:
   edades = [30]

7. Se calcula la suma:
   suma = 30

8. Se calcula la cantidad:
   cantidad = 1

9. Se calcula el promedio:
   promedio = 30 / 1
   promedio = 30.0

RESULTADO FINAL:

{'niño': [5], 'adolescente': [15], 'adulto': [30], 'mayor': [70]}
30.0"""


class AgrupadorEdades:

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.agrupado = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.agrupado[categoria].append(edad)

        return self.agrupado

    def edad_promedio_categoria(self, categoria):
        edades = self.agrupado.get(categoria, [])

        if len(edades) == 0:
            return 0

        return sum(edades) / len(edades)

ae = AgrupadorEdades()

print(ae.agrupar_por_categoria(5, 15, 30, 70))

print(ae.edad_promedio_categoria("adulto"))
