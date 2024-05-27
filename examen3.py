Edades = [11,19,31,18,12,9,17,27,51,3,15,23,90,7]

MinInf = 6
MaxInf = 11

MinAdole = 12
MaxAdole = 17

MinJov = 18
MaxJov = 26

MinAdulto = 27

Infancia = []
Adolescentes= []
Jovenes= []
Adultos= []
for edad in Edades:
    if edad >= MinInf and edad <= MaxInf:
        Infancia.append(edad)
    elif edad >= MinAdole and edad <= MaxAdole:
        Adolescentes.append(edad)
    elif edad >= MinJov and edad <= MaxJov:
        Jovenes.append(edad)
    elif edad >= MinAdulto:
        Adultos.append(edad)
print(f"Lista de infantes: {Infancia}")
print(f"Lista de adolescentes: {Adolescentes}")
print(f"Lista de jóvenes: {Jovenes}")
print(f"Lista de adultos: {Adultos}")