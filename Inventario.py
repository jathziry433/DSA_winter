class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_producto(self, codigo, precio):
        if codigo not in self.productos:
            self.productos [codigo] = precio

    def mostrar_productos(self):
        for codigo in self.productos:
         print(f"{codigo} $ {self.productos[codigo]}")

    def consultar_precio(self, codigo):
        if codigo  in self.productos:
            print(f"{codigo} $ {self.productos[codigo]}")

inventario = Inventario()

inventario.agregar_producto("Chetos", 18)
inventario.agregar_producto("Galletas", 10)
inventario.agregar_producto("Coca", 20)

inventario.mostrar_productos()

inventario.consultar_precio("Chetos")
