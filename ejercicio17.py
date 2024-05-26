def Cel_Fah():
    Celsius = float(input(f"Ingresa los grados celsius: "))
    Fahrenheit = (Celsius *9/5) + 32
    print(f"{Celsius} grados celsius = {Fahrenheit} grados faherenheit")

def Fah_Cel():
    Fahrenheit = float(input(f"Ingrese los grados fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5/9
    print(f"{Fahrenheit} grados fahrenheit = {Celsius} grados celsius")

while True:
    Convertir = input(f"Ingresa 1 para convertir de Celsius a Fahrenheit, 2 para Fahrenheit a Celsius y 's' para salir: ")
    if Convertir == "1":
        Cel_Fah()
    elif Convertir == "2":
        Fah_Cel()
    elif Convertir == "s":
        break


