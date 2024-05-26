peso = float(input("Ingres el peso del paquete: "))
precio1kg = 50
precio1a5 = 100
precio5a10 = 200
precio10a_ = 500



if peso < 1:
    print(f"El precio del envío es de {precio1kg}")
elif peso >= 1 and peso < 5:
    print(f"El precio del envío es de {precio1a5}")
elif peso >= 5 and peso < 10:
    print(f"El precio del envío es de {precio5a10}")
else:
    print(f"El precio del envío es de {precio10a_}")
