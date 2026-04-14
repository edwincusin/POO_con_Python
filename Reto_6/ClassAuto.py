class Auto:
    #constructor clase
    def __init__(self,marca,modelo,ano,kilometraje=0):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.kilometraje=kilometraje
    
    #metodo imprimir informacion de la clase
    def mostrarInformacion(self):
        print(f"Marca: {self.marca}, modelo: {self.modelo}, año: {self.ano}")
    
    #metodo acutualizar km
    def actualizarKm(self,kilometraje):
        if kilometraje>self.kilometraje:
            self.kilometraje=kilometraje
        else:
            print("No puede reducir el Kilometraje")
    
    #metodo realizar viaje
    def realizarViaje(self, kilometros):
        if kilometros>0:
            self.kilometraje+=kilometros
        else:
            print("Cantidad de kilometros deben ser un valor positivo")
    
    #metodo estado auto
    def estadoAuto(self):
        if self.kilometraje<20000:
            print("ESTOY COMO NUEVO")
        elif 20000<=self.kilometraje<=100000:
            print("YA ESTOY USADO")
        elif self.kilometraje>100000:
            print("YA DEJAME DESCANSAR POR FAVOR")
print()
print("=======================================================")
print("PRUEBA LLENAR MEDIANTE ARGUMENTOS DEL CONSTRUCTOR ")
print("=======================================================")
auto1=Auto("KIA","SOLUTO",2025)
auto2=Auto("FORD","ESCAPE",2019,500)

print()
print("=======================================================")
print("PRUEBA EJECUTAR METODO MOSTRAR INFORMACION")
print("=======================================================")
auto1.mostrarInformacion()
auto2.mostrarInformacion()

print()
print("=======================================================")
print("PRUEBA EJECUTAR METODO ACTUALZIAR KILOMETRAJE")
print("=======================================================")
auto1.actualizarKm(40000)
auto2.actualizarKm(9999)

print(auto1.__dict__)
print(auto2.__dict__)

auto1.actualizarKm(-40000)#VALORNEGATIVOS
auto2.actualizarKm(-9999)#VALOR NEGATIVO


print()
print("=======================================================")
print("PRUEBA EJECUTAR METODO REALIZAR VIAJE")
print("=======================================================")

auto1.realizarViaje(500)
auto2.realizarViaje(1000)

print(auto1.__dict__)
print(auto2.__dict__)

        