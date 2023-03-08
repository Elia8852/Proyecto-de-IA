# Importaciones
import osmread as os
import math
import requests
import polyline 
import folium
import tkinter as tk





class Interface:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Map")
        self.ventana1.geometry("350x250")
        self.ventana1.config(bg="gray")
        
        self.latitudtxt1 = tk.Entry(self.ventana1)
        self.latitudtxt1.grid(column=1,row=1)
        self.longitudtxt2 = tk.Entry(self.ventana1)
        self.longitudtxt2.grid(column=1,row=2)
        self.latitudtxt3 = tk.Entry(self.ventana1)
        self.latitudtxt3.grid(column=1,row=3)
        self.longitudtxt4 = tk.Entry(self.ventana1)
        self.longitudtxt4.grid(column=1,row=4)

        self.distancia=tk.Label(self.ventana1, text="La distancia es: ", height=2)
        self.distancia.config(bg="gray")
        self.distancia.grid(column=1, row=6)



        self.latitud1=tk.Label(self.ventana1, text="Ingresa la latitud del punto 1: ", height=2)
        self.latitud1.config(bg="gray")
        self.latitud1.grid(column=0, row=1)
        
        self.latitud2=tk.Label(self.ventana1, text="Ingresa la latitud del punto 2: ",height=2)
        self.latitud2.grid(column=0, row=4)
        self.latitud2.config(bg="gray")
        


        self.longitud1=tk.Label(self.ventana1, text="Ingresa la longitud del punto 1: ", height=2)
        self.longitud1.grid(column=0, row=2)
        self.longitud1.config(bg="gray")
        


        self.longitud2=tk.Label(self.ventana1, text="Ingresa la longitud del punto 2: ", height=2)
        self.longitud2.grid(column=0, row=3)
        self.longitud2.config(bg="gray")
        
        
        self.calcularBtn=tk.Button(self.ventana1, text="Mostrar en mapa",command=self.Mostrar_map)
        self.calcularBtn.grid(column=0, row=6)
        
        self.calcularBtn=tk.Button(self.ventana1, text="Calcular Distancia",command=self.distancia_funcion)
        self.calcularBtn.grid(column=0, row=7)
        
        
        self.ventana1.mainloop()
        
        

    

    def Mostrar_map(self):
        
        latitud1= self.latitudtxt1.get()
        longitud1 = self.longitudtxt2.get()
        latitud2 = self.latitudtxt3.get()
        longitud2= self.longitudtxt4.get()
        
        

        # Hacer una solicitud HTTP a la API de rutas de OpenStreetMap para el camino más largo
        url2 = f"http://router.project-osrm.org/route/v1/driving/{longitud1},{latitud1};{longitud2},{latitud2}?steps=true&annotations=true"
        response2 = requests.get(url2)

        # Decodificar los puntos de la ruta devueltos por la API para el camino más largo
        route2 = []
        for leg in response2.json()['routes'][0]['legs']:
            for step in leg['steps']:
                route2.extend(polyline.decode(step['geometry']))

        # Crear un mapa centrado en el punto de inicio
        m = folium.Map(location=[latitud1, longitud1], zoom_start=13)

        # Agregar un marcador para el punto de inicio
        folium.Marker(location=[latitud1, longitud1], tooltip="Punto 1").add_to(m)

        # Agregar un marcador para el punto de destino
        folium.Marker(location=[latitud2, longitud2], tooltip="Punto 2").add_to(m)


        # Agrega la ruta en azul
        folium.PolyLine(locations=route2, color='blue', weight=5).add_to(m)

        # Mostrar el mapa en el navegador
        m.show_in_browser()



    def distancia_funcion(self):
            # Convertir las latitudes y longitudes de grados a radianes
            latitud1= self.latitudtxt1.get()
            longitud1 = self.longitudtxt2.get()
            latitud2 = self.latitudtxt3.get()
            longitud2= self.longitudtxt4.get()

            latitud11= float(latitud1)
            longitud11= float(longitud1)
            latitud22 =float(latitud2)
            longitud22=float(longitud2)


            latitud1 = math.radians(latitud11)
            longitud1 = math.radians(longitud11)
            latitud2 = math.radians(latitud22)
            longitud2 = math.radians(longitud22)

            # Calcular la diferencia entre las latitudes y longitudes
            dlat = latitud2 - latitud1
            dlon = longitud2 - longitud1

            # Aplicar la fórmula de Haversine
            a = math.sin(dlat / 2) ** 2 + math.cos(latitud1) * math.cos(latitud2) * math.sin(dlon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distancia_km = 6371 * c
            print(f"la distancia es {distancia_km:.2f} km")
        
            self.distancia1=tk.Label(self.ventana1, text=f"{distancia_km:.2f} km", height=2)
            self.distancia1.config(bg="gray")
            self.distancia1.grid(column=1, row=7)
            return distancia_km
        
#Creacion de clase Grafo, con todas sus funciones
class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = set()

    def agregarArista(self, a, b):
        if a in self.vertices and b not in self.vertices:
            self.vertices[a].add(b)
            if self.doblevia(a,b) == True:
                self.vertices[b].add(a)
           
    def doblevia(self, a, b):
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

# Creacion de la funcion que calcula la distancia




app = Interface()
#grafo y datos de el grafo
g = Grafo()

vertices = []
edges = []
ruta = r"C:\Users\Windows 10\Desktop\ITLA-C1-2023\Inteligencia artificial\Proyecto 1\santo_domingo.osm"
contador = 0
for i in os.parse_file(ruta):
    if isinstance(i,os.Node): 
            nodo = i.id
            nodo2=i.id+1
            
            

            if nodo2 not in i:
                nodo2 = nodo2+1
                edges.append([nodo, nodo2])
                g.agregarVertice(nodo)
                g.agregarArista(nodo,nodo2)

            for i in g.vertices:
                g.agregarArista(nodo,nodo2)
            contador = contador+1
    if contador==10:
        break    

    
    
        
#imprime todos los nodos con sus vecinos     
vecinos = g.obtenerTodosVecinos()
for v in vecinos:
    print("Vecinos de", v, ": ")
    for vecino in vecinos[v]:
        print(vecino)
    print() # salto de línea



      
# Encontrar la distancia más corta entre dos nodos usando el algoritmo de Dijkstra





for entidad in os.parse_file(ruta):
    if isinstance(entidad, os.Node):
        tags = entidad.tags
        if 'peso' in tags:
            peso = tags['peso']
            print(f"El nodo {entidad.id} tiene un peso de {peso}".format(entidad.id, peso))    




          

############################################################################

# Visual  ar el mapa en la ventana



    




        
        
    

    
    
    

    




   









