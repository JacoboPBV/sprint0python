class Heroe:
    nombre:str
    ataque:int
    defensa:int
    salud:int
    salud_maxima:int

    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 12
        self.defensa = 5
        self.salud_maxima = 100
        self.salud = self.salud_maxima

    def atacar(self, enemigo):
        salud_perdida = self.ataque - enemigo.defensa

        print("Héroe ataca a " + enemigo.nombre)
        if salud_perdida <= 0: print("El enemigo ha bloqueado el ataque")
        else:
            print("El enemigo " + enemigo.nombre + " ha recibido " + str(salud_perdida) + " puntos de daño.")
            enemigo.salud -= salud_perdida

    def curarse(self):
        salud_recuperada = 25
        if self.salud + salud_recuperada > self.salud_maxima: self.salud = self.salud_maxima
        else: self.salud += salud_recuperada
        print("Héroe se ha curado. Salud actual: " + str(self.salud))

    def defenderse(self):
        self.defensa += 5
        print("Héroe se defiende. Defensa aumentada temporalmente a " + str(self.defensa))

    def reset_defensa(self):
        self.defensa -= 5
        print("La defensa de " + self.nombre + " vuelve a la normalidad")

    def esta_vivo(self):
        return self.salud > 0
