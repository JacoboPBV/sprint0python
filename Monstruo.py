class Monstruo:
    #Atributos
    nombre:str
    ataque:int
    defensa:int
    salud:int

    #Inicializamos los valores
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 15
        self.defensa = 3
        self.salud = 100

    def atacar(self, heroe):
        salud_perdida = self.ataque - heroe.defensa #Predecimos el daño que nos va a hacer

        print(self.nombre + " ataca a " + heroe.nombre)
        if salud_perdida <= 0: print("El héroe ha bloqueado el ataque") #Permitimos daños solo mayores que 0
        else:
            print("El héroe " + heroe.nombre + " ha recibido " + str(salud_perdida) + " puntos de daño.")
            heroe.salud -= salud_perdida
            print("Vida actual: " + str(heroe.salud)) #

    def esta_vivo(self):
        return self.salud > 0
