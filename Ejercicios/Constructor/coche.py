class Coche:
    #Atributos o propiedades
    color = "negro"
    marca = "BMW"
    modelo = "M3"
    velocidad = 300
    caballaje = 200
    puestos = 4
    #Publico
    soy_publico = "Hola soy un atributo publico"
    #Privado
    __soy_privado = "Hola soy un atributo Privado"




    #Constructor
    def __init__(self,color,marca,modelo,velocidad,caballaje,puestos):
        self.color = color
        self.marca = marca  
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.puestos = puestos


    #Métodos/Acciones Acciones que hace el objeto coche. (Funciones)
    def getPrivado(self):
        return self.__soy_privado

    def setMarca (self,marca):
        self.marca = marca

    def setPuestos(self,puestos):
        self.puestos = puestos

    def getMarca(self):
        return self.marca

    def getInfo(self):
        info = "-----Información del Coche"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        info += "\n Caballaje: " + str(self.getCaballaje())
        info += "\n Puestos: " + str(self.getPuestos())
        return info


    def getPuestos(self):
        return self.puestos

    def getCaballaje(self):
        return self.caballaje

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
