class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
     
    def  es_mayor_de_edad(self):
        return self.edad >= 18
  
persona1=Persona('Juan Lopez', 20)
persona2=Persona('Luis Rivas', 15)

persona1.saludar()
persona2.saludar()

print(persona1.es_mayor_de_edad())
print(persona2.es_mayor_de_edad())