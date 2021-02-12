
#Programación Orientada a Objetos. (POO OOP)

#Definir una clase: Molde para crear objetos.

class Coche:
    #Atributos o propiedades
    color = "negro"
    marca = "BMW"
    modelo = "M3"
    velocidad = 300
    caballaje = 200
    puestos = 4
    #Métodos/Acciones Acciones que hace el objeto coche. (Funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad (self):
        return self.velocidad 

# Fin definicion de clase.

coche = Coche()
coche.setColor("Púrpura")
coche.setModelo("Carrera")
print(coche.marca, coche.getColor(), coche.getModelo())
print(f"Velocidad Actual: {coche.getVelocidad()}")
coche.acelerar()    
coche.acelerar()
coche.acelerar()
coche.acelerar()
print(f"Velocidad Actual: {coche.getVelocidad()}")
coche.frenar()
print(f"Velocidad Actual: {coche.getVelocidad()}")

coche2 = Coche()
print("--------------------------------------------")
coche2.setColor("Verde")
coche2.setModelo("Mustang")
print(coche2.getColor(), coche2.marca, coche2.getModelo())
print(type(coche2))