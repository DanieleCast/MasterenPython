class persona:
    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellido

    def getAltura(self):
        return self.altura

    def getEdad (self):
        return self.edad

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellido(self,apellido):
        self.apellido = apellido

    def setAltura(self,altura):
        self.altura= altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        print("Estoy Hablando")

    def caminar(self):
        print("Estoy Caminando")

class Informatico(persona):

    def __init__(self):
        self.lenguajes= "Python, C+, C"

    def getLenguajes(self):
        return self.lenguajes
    
    def aprenderLenguajes(self, lenguajes):
        self.lenguajes += ", " + lenguajes
        return self.lenguajes
