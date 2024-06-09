class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def reproducirse(self):
        print(f"Yo soy el animal {self.__nombre} y puedo reproducirme")
