class Personaje:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self.vida = vida
        self.vida_actual = vida
        self.daño = daño
        #self.armas = {}
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
    
    def tam_mascota(self,mascota, collar):
        mascota.poner_coll(collar)
        self.mascotas.append(mascota)
        print(f"{self.nombre} ha domesticado a {mascota.nombre}")

    def atacar_masc(self, mascota, atacado):
        print(f"{self.nombre} usó a {mascota.nombre} para atacar a {atacado.nombre}")
        mascota.atacar(atacado)

    def usar_estatua(self, estatua):
        self.vida_actual = self.vida
        print(f"{self.nombre} ha usado la estatua de {estatua.ubicacion} para curarse por completo")

class Mascota: #Agregación
    def __init__(self, nombre, tipo, ataque, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.vida = vida
        self.collar = None
    
    def atacar(self, atacado):
        print(f"{self.nombre} atacó con {self.ataque} puntos de daño a {atacado.nombre}")
        atacado.vida_actual -= self.ataque
        print(f"{atacado.nombre} ahora tiene {atacado.vida_actual} HP")
    
    def describirse(self):
        print(f"--Descripción de {self.nombre}--\nMe llamo {self.nombre} \nSoy de tipo {self.tipo}")
        self.collar.describir()

    def poner_coll(self, collar):
        self.collar = collar

class NPC: #Asociación
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
    
    def Hablar(self, personaje):
        print(f"Hola, {personaje.nombre}... (texto de NPC)")

    def Describir(self):
        print(f"Soy {self.nombre}, un {self.rol}")

class Collar: #Composición
    def __init__(self, material, nombre_coll):
        self.material = material
        self.nombre = nombre_coll

    def describir(self):
        print(f"Este collar es de {self.material} y tiene grabado el nombre de {self.nombre}")

class Mago(Personaje): #Herencia
    def __init__(self, nombre, vida, daño, tipo_magia, daño_magia):
        super().__init__(nombre, vida, daño)
        self.tipo_magia = tipo_magia
        self.daño_magia = daño_magia
    
    def usar_magia(self, atacado):
        print(f"{self.nombre} usó magia de {self.tipo_magia} para atacar a {atacado.nombre} con {self.daño_magia} puntos de daño")
        atacado.vida_actual -= self.daño_magia
        print(f"{atacado.nombre} ahora tiene {atacado.vida_actual} HP")
    
    def mostrar_stats(self):
        super().mostrar_stats()
        print(f"Magia: {self.tipo_magia} \nDaño de magia: {self.daño_magia}")

class Estatua_curacion: #Dependencia
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion

    def describir(self):
        print(f"Esta estatua se encuentra en {self.ubicacion}")

def main ():
    #Zelda = Personaje("Zelda", 900, 30)
    Guts = Personaje("Guts", 1000, 49)
    Dynamo = Mago("Dynamo", 700, 20, "viento", 60)

    Estatua_Sendero = Estatua_curacion("Sendero verde")
    Estatua_Sendero.describir()

    #Dynamo.atacar(Zelda) #Ataque normal
    Dynamo.usar_magia(Guts) #Ataque de magia
    Guts.atacar(Dynamo)
    #Dynamo.curar(33)
    Guts.mostrar_stats()
    Guts.usar_estatua(Estatua_Sendero)
    Guts.mostrar_stats()

    #Collar_Char = Collar("oro", "Charizard")

    #Guts.atacar(Zelda)
    #Zelda.atacar(Guts)

    #Guts.mostrar_stats()
    #Guts.curar(19)
    #Guts.mostrar_stats()

    #Charizard = Mascota("Charizard", "Dragón", 50, 900)

    #Guts.tam_mascota(Charizard, Collar_Char)
    #Guts.atacar_masc(Charizard, Zelda)
    #Charizard.describirse()

    #Cantinero = NPC("Edward", "Cantinero")
    #Cantinero.Describir()
    #Cantinero.Hablar(Guts)
    #Cantinero.Hablar(Zelda)
main()