
class Laptop:
    def __init__(self,marca,procesador, memoria, costo=500,impuesto=10):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.costo=costo
        self.impuesto=impuesto
    
    #metodos de isntancia
    def valorFinal(self):
        return self.costo+self.impuesto
    
    def valorDescuento(self,descuento):
        return (self.costo*descuento)/100

    #METODOS ESTATICOS
    @staticmethod
    def comparar_costo(lapto1,lapto2):
        if lapto1.costo ==lapto2.costo:
            return "los costos son iguales"
        else:
            return " los costos son diferentes"

    #METODOS DE CLASE==>cls es una referenia a la misma clase es ocmo un constructor alternativo
    @classmethod
    def asusLaptop(cls,costo):
        marca="AZUS"
        procesador="i5"
        memoria =32
        return cls(marca,procesador,memoria,costo)