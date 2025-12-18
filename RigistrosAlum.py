class RegistroAlumnos:
    def __init__(self):
        self.alumnos = {}

    def agregar_alumno(self, nombre):
        self.alumnos[nombre] = []

    def agregar_calificacion(self, nombre, calificacion):
       #Si el alumno existe  se agrega la calificaccion
       if nombre in self.alumnos:
           self.alumnos[nombre].append(calificacion)
       else:
           print("{nombre} no existe")

    def mostrar_registro(self):
        for alumno in self.alumnos:
            print(f"{alumno} :{self.alumnos[alumno]}")
    
    def promedio_alumno(self, nombre):
        #Si el alumno existe imprime el promedio 
        if nombre in self.alumnos:
            calificaciones = self.alumnos[nombre]
            promedio=sum(calificaciones)/(len(calificaciones))
            print(f"{nombre}, promedio: {promedio} - {calificaciones}")
        else:
            print("{nombre} no existe")

tics=RegistroAlumnos()

tics.agregar_alumno("Juan")
tics.agregar_alumno("Jose")
tics.agregar_alumno("Ana")

tics.agregar_calificacion("Juan", 8)
tics.agregar_calificacion("Juan", 9)
tics.agregar_calificacion("Juan", 10)
tics.agregar_calificacion("Ana", 5)
tics.agregar_calificacion("Ana", 10)
tics.agregar_calificacion("Ana", 5)
tics.agregar_calificacion("Ana", 9)
tics.mostrar_registro()
tics.promedio_alumno("Juan")
tics.promedio_alumno("Ana")
