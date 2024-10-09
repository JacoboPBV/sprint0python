from random import randint


class Tesoro:
    beneficios:list[str] = list()

    def __init__(self):
        self.beneficios.append("Ataque")
        self.beneficios.append("Defensa")
        self.beneficios.append("Curación")

    def encontrar_tesoro(self, heroe):
        beneficio = self.beneficios.__getitem__(randint(0,2))
        print("El héroe ha encontrado un tesoro: " + beneficio)
        if beneficio == "Ataque":
            heroe.ataque += 3
            print("El ataque de " + heroe.nombre + " aumenta a " + str(heroe.ataque))
        elif beneficio == "Defensa":
            heroe.defensa += 3
            print("La defensa de " + heroe.nombre + " aumenta a " + str(heroe.defensa))
        elif beneficio == "Curación":
            heroe.salud = heroe.salud_maxima
            print("La salud de " + heroe.nombre + " ha sido restaurada a " + str(heroe.salud_maxima))