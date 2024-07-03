def sumar(N1,N2):
    suma = N1 + N2
    print(f"{N1} + {N2} = {suma}")

def restar(N1,N2):
    resta = N1 - N2
    print(f"{N1} + {N2} = {resta}")

def multiplicar(N1, N2):
    multi = N1 * N2
    print(f"{N1} x {N2} = {multi}")

def dividir(N1, N2):
    if N2 == 0:
        print(f"No se puede dividir por cero")
        return
    divi = N1 / N2
    print(f"{N1} / {N2} = {divi}")

def ingresar_num():
    while True:
        try:
            N1 = float(input(f"Ingresa el número 1: "))
            N2 = float(input(f"Ingresa el número 2: "))
            return N1, N2
        except ValueError:
            print(f"Ingresa números válidos")


def main():
    while True:
        try:
            operación = int(input(f"Ingresa 1 para sumar, 2 para restar, 3 para multiplicar y 4 para dividir: "))
            match operación:
                case 1:
                    N1, N2 = ingresar_num()
                    sumar(N1,N2)
                    break
                case 2:
                    N1, N2 = ingresar_num()
                    restar(N1, N2)
                    break
                case 3:
                    N1, N2 = ingresar_num()
                    multiplicar(N1, N2)
                    break
                case 4:
                    N1, N2 = ingresar_num()
                    dividir(N1,N2)
                    break
                case _:
                    print(f"Ingresa una operación válida")
        except ValueError:
            print(f"Ingresa una opción válida")
main()