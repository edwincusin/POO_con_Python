
class Laptop:
    def __init__(self,marca,procesador, memoria, costo=500,impuesto=10):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.costo=costo
        self.impuesto=impuesto
    
    def valorFinal(self):
        return self.costo+self.impuesto
    
    def valorDescuento(self,descuento):
        return (self.costo*descuento)/100

LaptopPepito=Laptop("lenovo","i7", memoria=32)

print(LaptopPepito.__dict__)
print(LaptopPepito.valorFinal())
print(f"el valor de descuento al {LaptopPepito.valorDescuento(10)}")