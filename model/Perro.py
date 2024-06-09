from model.Animal import Animal


class Perro(Animal):

    def __init__(self, nombre, edad, cantidad_pulgas):
        super().__init__(nombre, edad)
        self.__cantidad_pulgas = cantidad_pulgas

    def getCantidadPulgas(self):
        return self.__cantidad_pulgas

    def setCantidadPulgas(self, cantidad_pulgas):
        self.__cantidad_pulgas = cantidad_pulgas

    def reproducirse(self):
        print(f"Yo soy {super().getNombre()} y puedo tener sexo")
