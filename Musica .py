class ListaReproduccion:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.canciones = []
    def agregar_cancion (self, cancion):
        self.canciones.append(cancion)
        print(f"Se agrego la cancion {cancion} a la lista de reproduccion: {self.nombre}")   
          
    #"Elemento" es una espcie de contador para recorrer la lista
    def mostrar_cancion (self):
         elementos=len(self.canciones)
         for elemento in range (elementos):
             print(f"{elemento +1} - {self.canciones[elemento]}")

L1=ListaReproduccion("banda")
L2=ListaReproduccion("pop")

L1.agregar_cancion("Si es posible")
L2.agregar_cancion("Rosa pastel")

L1.mostrar_cancion()
L2.mostrar_cancion()