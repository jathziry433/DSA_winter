class CuantaBancaria:
    def __init__ (self, nombre,saldo):
        self.nombre= nombre
        self.saldo= saldo

    #NO regresa nada solo imprime la informacion 
    def mostrar_info(self):
        print(f"El titular es {self.nombre} y  el saldo es de: {self.saldo} ")

    # Solo accesa a la instancia y actualiza     
    def depositar(self, cantidad):
         self.cantidad=cantidad
         if self.cantidad > 0:
             self.saldo += self.cantidad
             print(f"Se deposito {self.cantidad} el nuevo saldo es de: {self.saldo}")
    def retirar(self,cantidad):
        if self.cantidad <=self.cantidad:
            self.saldo -=self.cantidad
            print(f"se retiro {self.cantidad} el nuvo saldo es de: {self.saldo}")
        if self.saldo < self.cantidad:
            print ("El saldo es insuficiente")

persona1=CuantaBancaria ("Mario Perez", 2500)    
persona2=CuantaBancaria ("Maria Lopez", 1500) 

persona1.mostrar_info()
persona2.mostrar_info()

persona1.depositar(1000)
persona2.depositar(200)

persona1.retirar(12000)
persona2.retirar(2000)