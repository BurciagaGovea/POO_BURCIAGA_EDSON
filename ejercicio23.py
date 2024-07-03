class Personaje:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self.vida = vida
        self.vida_actual = vida
        self.daño = daño
        self.armas = {}
        self.mascotas = []

    def curar(self, curacion):
        print(f"{self.nombre} se curó {curacion} puntos de vida")
        self.vida_actual += curacion
        print(f"{self.nombre} ahora tiene {self.vida_actual} puntos de vida")

    def atacar(self, atacado):
        print(f"{self.nombre} atacó con {self.daño} puntos de daño a {atacado.nombre}")
        atacado.vida_actual -= self.daño
        print(f"{atacado.nombre} ahora tiene {atacado.vida_actual} HP")

    def mostrar_stats(self):
        print(f"STATS DE {self.nombre}")
        print(f"Nombre: {self.nombre} \nHP: {self.vida_actual}/{self.vida} \nDaño: {self.daño}")


def main ():
    Zelda = Personaje("Zelda", 900, 30)
    Guts = Personaje("Guts", 1000, 49)

    Guts.atacar(Zelda)

    Zelda.atacar(Guts)

    Guts.mostrar_stats()
    Guts.curar(19)
    Guts.mostrar_stats

main()