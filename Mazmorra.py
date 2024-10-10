from Heroe import Heroe
from Monstruo import Monstruo
from Tesoro import Tesoro

class Mazmorra:
    heroe:Heroe
    monstruos:list[Monstruo] = list()
    tesoro:Tesoro

    def __init__(self, heroe):
        self.heroe = heroe
        #Inicializamos la lista de monstruos
        self.monstruos.append(Monstruo("Esqueleto"))
        self.monstruos.append(Monstruo("Zombie"))
        
        self.tesoro = Tesoro()

    def jugar(self):
        print("Héroe entra en la mazmorra.")

        pierde = False
        while not pierde:
            if self.monstruos.__len__() != 0:
                monstruo = self.monstruos.pop() #Sacamos al monstruo de la lista (actúa como pila)
                print("\nTe has encontrado con un " + monstruo.nombre)
                pierde = self.enfrentar_monstruo(monstruo)
                if not pierde:
                    self.buscar_tesoro()
            else:
                break #pierde = True por lo que es victoria del Héroe

        if pierde:
            print("\n\nHéroe ha sido derrotado en la mazmorra.")
        else:
            print("\n\n¡" + self.heroe.nombre + " ha derrotado a todos los monstruos y ha conquistado la mazmorra!")


    def enfrentar_monstruo(self, enemigo):
        while self.heroe.esta_vivo() and enemigo.esta_vivo(): #Mientras ambos sigan vivos, continua el combate
            print("Qué deseas hacer?"
                  "\n1. Atacar"
                  "\n2. Defender"
                  "\n3. Curarse")

            seguir = True
            while seguir:
                error = True
                while error:
                    try: #Solo puede poner números del 1 al 3
                        accion = int(input())
                        error = False
                        if accion == 1:
                            self.heroe.atacar(enemigo)
                            seguir = False
                        elif accion == 2:
                            self.heroe.defenderse()
                            seguir = False
                        elif accion == 3:
                            self.heroe.curarse()
                            seguir = False
                        else:
                            print("Acción no válida")
                            seguir = True
                    except ValueError:
                        print("Elige un número del 1 al 3")
                        seguir = True
                        
            enemigo.atacar(self.heroe)
            if accion == 2: self.heroe.reset_defensa() #Si acción fue defenderse, reset_defensa()¡
            print()

        return not self.heroe.esta_vivo()

    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe)
