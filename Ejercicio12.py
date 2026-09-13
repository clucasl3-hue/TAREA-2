"""Analizando múltiples rangos...

Rango: (1, 3)

  1 → se agrega ✓
  2 → se agrega ✓
  3 → se agrega ✓

Elementos:
  {1, 2, 3}


Rango: (2, 4)

  2 → ya existe, no se repite
  3 → ya existe, no se repite
  4 → se agrega ✓

Elementos:
  {1, 2, 3, 4}


Resultado final:
  [1, 2, 3, 4] ✓"""


class SelectorRango: 
 
    def crear_rango(self, inicio, fin): 
        numeros = [] 
 
        print(f"\nCreando rango desde {inicio} hasta {fin}...")
 
        for i in range(inicio, fin + 1): 
            print(f"  Agregando: {i}")
            numeros.append(i) 
 
        print(f"Resultado del rango: {tuple(numeros)} ✓")
        return tuple(numeros) 
 
    def elementos_en_multiples_rangos(self, *rangos): 
        elementos = set() 
 
        print("\nAnalizando múltiples rangos...")
 
        for rango in rangos: 
            inicio = rango[0] 
            fin = rango[1] 
 
            print(f"\nRango: ({inicio}, {fin})")
 
            for i in range(inicio, fin + 1):
                if i in elementos:
                    print(f"  {i} → ya existe, no se repite")
                else:
                    print(f"  {i} → se agrega ✓")
                
                elementos.add(i) 
 
        print(f"\nElementos únicos: {elementos}")
        print(f"Resultado final: {list(elementos)} ✓")
        
        return list(elementos) 
 
 
sr = SelectorRango() 
 
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))
