from operaciones import suma, resta, multiplicacion, division

def main():
    print("Qué operación deseas realizar? ")
    res = input("Suma (S) / Resta (R) / Multiplicación (M) / División (D): ")
    
    error = True
    while error: #Mientras no ponga números
        #"Switch" de las posibles elecciones
        try: #Para que solo ponga números
            if res in ["S", "s"]:
                suma(int(input("Primer número: ")), int(input("Segundo número: ")))
            elif res in ["R", "r"]:
                resta(int(input("Primer número: ")), int(input("Segundo número: ")))
            elif res in ["M", "m"]:
                multiplicacion(int(input("Primer número: ")), int(input("Segundo número: ")))
            elif res in ["D", "d"]:
                division(int(input("Primer número: ")), int(input("Segundo número: ")))
            else: print("Opción no válida")

            error = False
        except ValueError: error = True

main() #Ejecutamos el main
res = input("Desea hacer más operaciones? (S/N)")
while res in ["S","s"]: #Volvemos a hacer el mismo proceso mientras escriba "S"
    main()
    res = input("Desea hacer más operaciones? (S/N)") #Se podría controlar también que solo salga del bucle con N en vez de con cualquier caracter