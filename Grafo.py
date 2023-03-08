

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = set()

    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].add(b)
            if self.sonDeDobleVia(a,b) == True:
                self.vertices[b].add(a)
           
    
    def sonDeDobleVia(self, a, b):
        if a in self.vertices and b in self.vertices:
            if b in g.obtenerVecinos(a) and a in g.obtenerVecinos(b):
                return True
        return False            
    
    def obtenerVecinos(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            return None

    def obtenerTodosVecinos(self):
        todos_vecinos = {}
        for v in self.vertices:
            vecinos = self.obtenerVecinos(v)
            todos_vecinos[v] = vecinos
        return todos_vecinos


g = Grafo()
g.agregarVertice("A")
g.agregarVertice("B")
g.agregarVertice("C")
g.agregarVertice("D")
g.agregarVertice("E")
g.agregarVertice("F")
g.agregarVertice("G")
g.agregarVertice("H")
g.agregarVertice("I")
g.agregarVertice("J")
g.agregarVertice("K")
g.agregarVertice("L")
g.agregarVertice("M")
g.agregarVertice("N")
g.agregarVertice("O")
g.agregarVertice("P")
g.agregarVertice("Q")
g.agregarVertice("R")
g.agregarVertice("S")
g.agregarVertice("T")
g.agregarVertice("U")
g.agregarVertice("V")
g.agregarVertice("W")
g.agregarVertice("X")
g.agregarVertice("Y")
g.agregarVertice("Z")
#añadiendo las aristas 
g.agregarArista("A", "B")
g.agregarArista("A", "C")
g.agregarArista("A", "D")
g.agregarArista("A", "Q")
g.agregarArista("B", "A")
g.agregarArista("B", "E")
g.agregarArista("C", "F")
g.agregarArista("C", "G")
g.agregarArista("D", "A")
g.agregarArista("D", "I")
g.agregarArista("E", "J")
g.agregarArista("E", "K")
g.agregarArista("F", "L")
g.agregarArista("F", "M")
g.agregarArista("G", "N")
g.agregarArista("G", "O")
g.agregarArista("H", "P")
g.agregarArista("H", "Q")
g.agregarArista("I", "R")
g.agregarArista("I", "S")
g.agregarArista("J", "T")
g.agregarArista("J", "U")
g.agregarArista("K", "V")
g.agregarArista("K", "W")
g.agregarArista("L", "X")
g.agregarArista("L", "Y")
g.agregarArista("M", "Z")


vecinos = g.obtenerTodosVecinos()
for v in vecinos:
    print("Vecinos de", v, ": ")
    for vecino in vecinos[v]:
        print(vecino)
    print() # salto de línea
 



