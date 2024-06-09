from model.Animal import Animal


class Tiburon(Animal):

    def __init__(self, nombre, edad, cantidad_aletas):
        super().__init__(nombre, edad)
        self.__cantidad_aletas = cantidad_aletas

    def getCantidadAletas(self):
        return self.__cantidad_aletas

    def setCantidadAletas(self, cantidad_aletas):
        self.__cantidad_aletas = cantidad_aletas

    def reproducirse(self):
        print(f"Yo soy {super().getNombre()} y puedo poner huevos dentro de mi cuerpo")
