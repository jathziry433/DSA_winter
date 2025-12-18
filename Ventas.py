class SistemaVentas:
    def __init__(self):
        self.vendedores = {}

    def agregar_vendedor(self, nombre):
        if nombre not in self.vendedores:
            self.vendedores[nombre] = []
            print(f"Vendedor {nombre}")
        else:
            print(f"El vendedor '{nombre}' ya existe")

    def registrar_venta(self, nombre, monto):
        if nombre in self.vendedores:
            self.vendedores[nombre].append(monto)
            print(f"Venta de ${monto} registrada para {nombre}")
        else:
            print(f"El vendedor '{nombre}' no está registrado")

    def mostrar_ventas(self):
        print("Ventas por vendedor:")
        for nombre, ventas in self.vendedores.items():
            print(f"{nombre}: {ventas}")

    def total_vendedor(self, nombre):
        if nombre in self.vendedores:
            total = 0
            for venta in self.vendedores[nombre]:
                total += venta
            print(f"Total de ventas de {nombre}: ${total}")
            return total
        else:
            print(f"El vendedor {nombre} no existe")
            return 0

    def mejor_vendedor(self):
        mayor_total = 0
        mejor = None

        for nombre in self.vendedores:
            total = 0
            for venta in self.vendedores[nombre]:
                total += venta

            if total > mayor_total:
                mayor_total = total
                mejor = nombre

        if mejor:
            print(f"Mejor vendedor: {mejor} con ${mayor_total} en ventas")
        else:
            print("No hay ventas registradas")

sistema = SistemaVentas()

sistema.agregar_vendedor("Ana")
sistema.agregar_vendedor("Luis")
sistema.agregar_vendedor("María")

sistema.registrar_venta("Ana", 500)
sistema.registrar_venta("Ana", 300)
sistema.registrar_venta("Luis", 700)
sistema.registrar_venta("Luis", 100)
sistema.registrar_venta("María", 400)
sistema.registrar_venta("María", 600)

sistema.mostrar_ventas()
sistema.mejor_vendedor()