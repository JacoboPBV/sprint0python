class Monstruo:
    nombre = str
    ataque = int
    defensa = int
    salud = int

    def __init__(self):
        self.nombre = "Roberto"
        self.ataque = 3
        self.defensa = 1
        self.salud = 13

    def atacar(self, heroe):
        salud_perdida = self.ataque - heroe.defensa

        print(self.nombre + "ataca a " + heroe.nombre)
        if salud_perdida <= 0: print("El héroe ha bloqueado el ataque")
        else:
            print("El héroe " + heroe.nombre + " ha recibido " + salud_perdida + " puntos de daño.")
            heroe.salud -= salud_perdida

    def esta_vivo(self):
        return self.salud > 0