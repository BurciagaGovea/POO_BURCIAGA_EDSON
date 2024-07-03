numeros1 = {
    1,5,7,32,63,84,223,8
}
numeros2 = {
    2,64,842,5,8353,14,51
}
numeros3 = {
    13,2,53,764,93,37,1,311
}

numeros_union = numeros1 | numeros2 | numeros3

numeros_pares = set()

for i in numeros_union:
    if i%2 == 0:
        numeros_pares.add(i)

print(f"Conjunto con con números pares de la unión de 3 conjuntos: {numeros_pares}")