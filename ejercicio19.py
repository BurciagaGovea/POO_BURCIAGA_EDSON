frutas1 = {
    "melón","pera", "manzana", "uva",
}
frutas2 = {
    "sandía", "uva", "naranja", "melón"
}

union_frutas = frutas1 | frutas2
print(f"{union_frutas}")

union_frutas.add("guayaba")
print(f"{union_frutas}")