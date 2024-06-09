from model.Animal import Animal


class Serpiente(Animal):

    def __init__(self, nombre, edad, cantidad_escamas):
        super().__init__(nombre, edad)
        self.__cantidad_escamas = cantidad_escamas

    def getCantidadEscamas(self):
        return self.__cantidad_escamas

    def setCantidadEscamas(self, cantidad_escamas):
        self.__cantidad_escamas = cantidad_escamas

    def reproducirse(self):
        print(f"Yo soy {super().getNombre()} y puedo poner huevos por fuera")