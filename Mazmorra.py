from Heroe import Heroe
from Monstruo import Monstruo
from Tesoro import Tesoro

class Mazmorra:
    heroe:Heroe
    monstruos:list[Monstruo] = list()
    tesoro:Tesoro

    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos.append(Monstruo("Esqueleto"))
        self.monstruos.append(Monstruo("Zombie"))
        self.tesoro = Tesoro()

    def jugar(self):
        print("Héroe entra en la mazmorra.")

        pierde = False
        while not pierde:
            if self.monstruos.__len__() != 0:
                monstruo = self.monstruos.pop()
                print("\nTe has encontrado con un " + monstruo.nombre)
                pierde = self.enfrentar_monstruo(monstruo)
                if not pierde:
                    self.buscar_tesoro()
            else:
                break

        if pierde:
            print("\n\nHéroe ha sido derrotado en la mazmorra.")
        else:
            print("\n\n¡" + self.heroe.nombre + " ha derrotado a todos los monstruos y ha conquistado la mazmorra!")


    def enfrentar_monstruo(self, enemigo):
        while self.heroe.esta_vivo() and enemigo.esta_vivo():
            print("Qué deseas hacer?"
                  "\n1. Atacar"
                  "\n2. Defender"
                  "\n3. Curarse")

            seguir = True
            while seguir:
                error = True
                while error:
                    try:
                        accion = int(input())
                        error = False
                    except ValueError: print("Elige un número del 1 al 3")

                    try:
                        if accion == 1:
                            self.heroe.atacar(enemigo)
                            defender = False
                            seguir = False
                        elif accion == 2:
                            self.heroe.defenderse()
                            defender = True
                            seguir = False
                        elif accion == 3:
                            self.heroe.curarse()
                            defender = False
                            seguir = False
                        else:
                            print("Acción no válida")
                            seguir = True
                    except ValueError: seguir = True
            enemigo.atacar(self.heroe)
            if defender: self.heroe.reset_defensa()
            print()

        return not self.heroe.esta_vivo()

    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)
