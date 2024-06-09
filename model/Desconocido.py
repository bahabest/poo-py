from model.Animal import Animal


class Desconocido(Animal):
    def __init__(self, nombre, edad, rasgox):
        super().__init__(nombre, edad)
        self.__rasgox = rasgox

    def getRasgox(self):
        return self.__rasgox

    def setRasgox(self, rasgox):
        self.__rasgox = rasgox
