Edades = [11,19,31,18,12,9,17,27,51,3]
MayoresEdad = []
MenorerEdad = []
for edad in Edades:
    if edad >= 18:
        MayoresEdad.append(edad)
    else:
        MenorerEdad.append(edad)
print(f"Lista de mayores de edad: {MayoresEdad}")
print(f"Lista de menores de edad: {MenorerEdad}")