class Grupo:
    def __init__ (self, nombre_grupo):
        self.nombre_grupo=nombre_grupo
        self.calificaciones=[]
    
    def agregar_calificaciones(self,calificacion):
        self.calificaciones.append(calificacion)
        print(f"Se agrego la calificacion {calificacion} al grupo {self.nombre_grupo}")
    
    def mostrar_calificaciones (self):
         elementos=len(self.calificaciones)
         for elemento in range (elementos):
             print(f"{elemento +1}   {self.calificaciones [elemento]}")

    def obtener_calificaciones(self, indice):
        print (f"Indcice {indice} calificaciones {self.calificaciones[indice - 1]}")

G1=Grupo("Tercero A")
G2= Grupo("Cuarto A")

G1.agregar_calificaciones(70)
G1.agregar_calificaciones(80)

G2.agregar_calificaciones(100)
G2.agregar_calificaciones(90)

G1.mostrar_calificaciones()
G2.mostrar_calificaciones()

G1.obtener_calificaciones(indice=2)