from ClassAuto import Auto 
print()
print("=======================================================")
print("1. PRUEBA METODO DE CLASE  - CONSTRUCTOR ALTERNATIVO")
print("=======================================================")

vehiculoToyota =Auto.autoAnio("HILUX")
print(vehiculoToyota.__dict__)

print()
print("=======================================================")
print("2. PRUEBA METODO ESTATICO  - METODO FUNCION AUXILAR    ")
print("=======================================================")

auto1=Auto("KIA","SOLUTO",2025,70000)
auto2=Auto("FORD","ESCAPE",2019,500)

print(Auto.validar(auto1,auto2))

print()
print("=======================================================")
print("3. PRUEBA METODO ESTATICO  - A CONSIDERACION   ")
print("=======================================================")

print(Auto.requiereMantenimiento(500))

print()
print("=======================================================")
print("4. PRUEBA METODO DE CLASE  - A CONSIDERACION")
print("=======================================================")

for anio in range (1980,2000):
    vehiculoClasicos= Auto.vehiculosClasicos(anio)
    print(vehiculoClasicos.__dict__)
