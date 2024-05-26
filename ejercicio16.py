promedio1 = float(input(f"Ingresa el primer promedio: "))
promedio2 = float(input(f"Ingresa el segundo promedio: "))
promedio3 = float(input(f"Ingresa el tercer promedio: "))

if promedio1 > promedio2 and promedio1 > promedio3:
    mayor = promedio1
elif promedio2 > promedio1 and promedio2 > promedio3:
    mayor = promedio2
else:
    mayor = promedio3

print(f"El mayor promedio es: {mayor}")
