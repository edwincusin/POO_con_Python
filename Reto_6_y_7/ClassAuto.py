class Auto:
    #constructor clase
    def __init__(self,marca,modelo,anio,kilometraje=0):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.kilometraje=kilometraje
    
    #metodo imprimir informacion de la clase  -- metodo de instancia
    def mostrarInformacion(self):
        print(f"Marca: {self.marca}, modelo: {self.modelo}, año: {self.anio}")
    
    #metodo acutualizar km  -- metodo de instancia
    def actualizarKm(self,kilometraje):
        if kilometraje>self.kilometraje:
            self.kilometraje=kilometraje
        else:
            print("No puede reducir el Kilometraje")
    
    #metodo realizar viaje  -- metodo de instancia
    def realizarViaje(self, kilometros):
        if kilometros>0:
            self.kilometraje+=kilometros
        else:
            print("Cantidad de kilometros deben ser un valor positivo")
    
    #metodo estado auto -- metodo de instancia
    def estadoAuto(self):
        if self.kilometraje<20000:
            print("ESTOY COMO NUEVO")
        elif 20000<=self.kilometraje<=100000:
            print("YA ESTOY USADO")
        elif self.kilometraje>100000:
            print("YA DEJAME DESCANSAR POR FAVOR")
     
    #===================================RETO 7=========================================        
    #METODO DE CLASE: 
    @classmethod
    def autoAnio(cls,modelo):
        marca="TOYOTA"
        anio=2026
        return cls(marca,modelo,anio,kilometraje=0)
    
    #METODO ESTATICO: --funcion auxiliar
    @staticmethod
    def validar(auto1,auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "KILOMETRAJES IGUALES"
        else:
            return "KILOMETRAJES DIFERENTES"
    
    #METODO ESTATICO A CONSIDERACION -- SI REQUIERE PRIMER MANTENIMIENTO
    @staticmethod
    def requiereMantenimiento(kilometraje):
        if kilometraje <10000:
            return "Optimo, para continuar, No requiere aun mant..."
        elif 10000 <= kilometraje <=15000:
            return "Ingreso al rango donde neceistas hacer mantenimiento general"
    
    #METHODO DE CLASE A CONSIDERACION: --- VEHICULOS MITSUBISHI CLASICOS
    @classmethod
    def vehiculosClasicos(cls,anio):
        marca="Mitsubishi"
        modelo="Montero"
        kilometraje=2000000
        return cls(marca,modelo,anio,kilometraje)
        
                


    
    
    
    
    
    
# print()
# print("=======================================================")
# print("PRUEBA LLENAR MEDIANTE ARGUMENTOS DEL CONSTRUCTOR ")
# print("=======================================================")
# auto1=Auto("KIA","SOLUTO",2025)
# auto2=Auto("FORD","ESCAPE",2019,500)

# print()
# print("=======================================================")
# print("PRUEBA EJECUTAR METODO MOSTRAR INFORMACION")
# print("=======================================================")
# auto1.mostrarInformacion()
# auto2.mostrarInformacion()

# print()
# print("=======================================================")
# print("PRUEBA EJECUTAR METODO ACTUALZIAR KILOMETRAJE")
# print("=======================================================")
# auto1.actualizarKm(40000)
# auto2.actualizarKm(9999)

# print(auto1.__dict__)
# print(auto2.__dict__)
# auto1.actualizarKm(-40000)#VALORNEGATIVOS
# auto2.actualizarKm(-9999)#VALOR NEGATIVO

# print()
# print("=======================================================")
# print("PRUEBA EJECUTAR METODO REALIZAR VIAJE")
# print("=======================================================")

# auto1.realizarViaje(500)
# auto2.realizarViaje(1000)
# print(auto1.__dict__)
# print(auto2.__dict__)

# print()
# print("=======================================================")
# print("PRUEBA EJECUTAR METODO ESTADO AUTO")
# print("=======================================================")

# auto1.estadoAuto()
# auto2.estadoAuto()
        