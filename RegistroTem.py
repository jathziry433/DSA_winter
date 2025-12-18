class RegistroTemperaturas:
    def __init__(self):
        self.temperatura=[]

    def agragar_temperatura(sellf, temperatura ):
        sellf.temperatura.append(temperatura)

    def mostrar_temperatura(self):
        print("La temperatura es: ")
        for tem in self.temperatura:
            #Muestra cada temperatura individual que guarda en la lista 
            print (tem)

    def contador_mayores_a(self, valor):
        contador=0
        for tem in self.temperatura:
            if tem   > valor:
                contador += 1
        return contador
            
R1=RegistroTemperaturas()

R1.agragar_temperatura(19)
R1.agragar_temperatura(20)
R1.agragar_temperatura(14)

R1.mostrar_temperatura()
cantidad = R1.contador_mayores_a (10)

print(f"Cantidad de temperatura" ," ", cantidad)