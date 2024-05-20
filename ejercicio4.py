a = 2
b = 4
c = -6
PRIM = -b
SEG = ((b**2)-(4*a*c))**0.5
DIV = 2 * a
x1 = (PRIM + SEG)//DIV
x2 = (PRIM - SEG)//DIV
print(f"{x1} {x2}")