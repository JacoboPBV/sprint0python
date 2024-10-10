def suma(a, b):
    print(a+b)

def resta(a, b):
    print(a-b)

def multiplicacion(a, b):
    print(a*b)

def division(a, b):
    """
    if b == 0: print("Error")
    else: print(a/b)
    """
    try: #Otra forma de hacerlo sin errores
        print(a/b)
    except ZeroDivisionError: print("Error: División por 0")