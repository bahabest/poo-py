from model.Animal import Animal
from model.Desconocido import Desconocido
from model.Experimento import Experimento
from model.Tiburon import Tiburon
from model.Perro import Perro
from model.Serpiente import Serpiente

kisame = Tiburon("Kisame", 500, 2)
kakashi = Perro("Kakashi", 38, 3)
dogmeat = Perro("Dogmeat", 200, 0)
orochimaru = Serpiente("OrochiPoronga", 70, 1000)
unknown = Desconocido("Especie desconocida", 5000, "Ojos de gato")

animales = (kisame, kakashi, dogmeat, orochimaru, unknown)

for animal in animales:
    print(f"Nombre: {animal.getNombre()}")
    print(f"Edad: {animal.getEdad()}")
    animal.reproducirse()

    if animal.__class__.__name__ == "Perro":
        print(f"Cantidad de pulgas: {animal.getCantidadPulgas()}")

    if animal.__class__.__name__ == "Serpiente":
        print(f"Cantidad de escamas: {animal.getCantidadEscamas()}")

    if animal.__class__.__name__ == "Tiburon":
        print(f"Cantidad de aletas: {animal.getCantidadAletas()}")

    if animal.__class__.__name__ == "Desconocido":
        print(f"Rasgo particular: {animal.getRasgox()}")

    print("--------------------------------------------")

exp = Experimento()
exp.experimentar()
