"""BOSQUEJO:

1. Se crea el objeto:
   ap = AnalizadorPatrones()

2. Se buscan palabras que comiencen con "el":

   Texto:
   "el gato está aquí"

   Patron:
   "el"

   Se divide el texto:
   ["el", "gato", "está", "aquí"]

   Se revisa cada palabra:

   "el" → empieza con "el" → Sí
   Se agrega a la lista.

   "gato" → empieza con "el" → No

   "está" → empieza con "el" → No

   "aquí" → empieza con "el" → No

   Resultado:
   ["el"]

3. Se agrupan las palabras por longitud:

   Texto:
   "el gato está aquí"

   Se divide:
   ["el", "gato", "está", "aquí"]

   Palabra "el":
   longitud = 2

   Se crea la categoría 2:
   2 → ["el"]

   Palabra "gato":
   longitud = 4

   Se crea la categoría 4:
   4 → ["gato"]

   Palabra "está":
   longitud = 4

   La categoría 4 ya existe:
   4 → ["gato", "está"]

   Palabra "aquí":
   longitud = 4

   La categoría 4 ya existe:
   4 → ["gato", "está", "aquí"]

   Resultado:
   {
       2: ["el"],
       4: ["gato", "está", "aquí"]
   }

4. Se buscan palabras únicas:

   self.palabras =
   ["el", "gato", "está", "aquí"]

   Se convierte la lista en un conjunto:

   {"el", "gato", "está", "aquí"}

   No hay palabras repetidas.

RESULTADO FINAL:

["el"]

{2: ["el"], 4: ["gato", "está", "aquí"]}

{"el", "gato", "está", "aquí"}"""


class AnalizadorPatrones:

    def __init__(self):
        self.palabras = []

    def encontrar_palabras(self, texto, patron):
        palabras_encontradas = []

        for palabra in texto.split():
            if palabra.startswith(patron):
                palabras_encontradas.append(palabra)

        return palabras_encontradas

    def agrupar_por_longitud(self, texto):
        self.palabras = texto.split()

        agrupado = {}

        for palabra in self.palabras:
            longitud = len(palabra)

            if longitud not in agrupado:
                agrupado[longitud] = []

            agrupado[longitud].append(palabra)

        return agrupado

    def palabras_unicas(self):
        return set(self.palabras)

ap = AnalizadorPatrones()

print(ap.encontrar_palabras("el gato está aquí", "el"))

print(ap.agrupar_por_longitud("el gato está aquí"))

print(ap.palabras_unicas())
