from laptop import *


laptopPepito=Laptop("lenovo","i7", memoria=32)
laptopMaria=Laptop("HP", "I5",16,600)

print(Laptop.comparar_costo(laptopPepito,laptopMaria))

#usar el mtodo de clase

for numero in range(1,1001):
    asusLaptop =Laptop.asusLaptop(numero)
    print(asusLaptop.__dict__)