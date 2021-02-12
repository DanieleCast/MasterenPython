from coche import Coche

carro = Coche("Amarillo","Renault","Clio",150,200,4)
carro1 = Coche("Rojo","Mustang","Ford",500,400,2)

print(carro.getColor())

print(carro.getInfo())

print(carro1.getInfo())

#Detectar tipado 

if type(carro1) == Coche:
    print("Es un objeto del tipo coche")
else: print("No es un objeto del tipo coche")