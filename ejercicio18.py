Precios = {
    "uva": 15,
    "pera": 10,
    "manzana": 20,
    "papa": 40
}

descuento = 0.5

for i in Precios:
    print(f"Precio normal de {i}: {Precios[i]}")
    descuentoHecho = Precios[i]*(1-descuento)
    print(f"Precio con descuento de {i}: {descuentoHecho}")
