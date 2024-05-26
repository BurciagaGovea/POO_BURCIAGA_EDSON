N1 = 0.0
N2 = 0.0
while True:
    N1 = float(input(f"Ingrese el número 1: "))
    N2 = float(input(f"Ingrese el número 2: "))
    suma = N1 + N2
    print(f"{N1} + {N2} = {suma}")
    Cont = input(f"Ingrese 'n' si desea parar el programa: ")
    if Cont == "n":
        break