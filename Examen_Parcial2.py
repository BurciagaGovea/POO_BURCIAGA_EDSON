class Personaje:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self.vida = vida
        self.vida_actual = vida
        self.daño = daño
        self.mascotas = []

    def curar(self, curacion):
        print(f"{self.nombre} se curó {curacion} puntos de vida")
        self.vida_actual += curacion
        if self.vida_actual > self.vida:
            self.vida_actual = self.vida
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

    def comer(self, comida):
        print(f"{self.nombre} ha comido {comida.comida}")

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
        print(f"Hola, {personaje.nombre}, soy {self.nombre}, un {self.rol}... (texto de NPC)")

    def Describir(self):
        print(f"soy {self.nombre}, un {self.rol}")

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

class Support(Personaje): #Herencia
    def __init__(self,nombre,vida,daño,bono_daño, curacion):
        super().__init__(nombre, vida, daño)
        self.bono_daño = bono_daño
        self.curacion = curacion

    def curar(self, aliado):
        aliado.vida_actual += self.curacion
        if aliado.vida_actual > aliado.vida:
            aliado.vida_actual = aliado.vida
        print(f"{self.nombre} ha curado a {aliado.nombre} en {self.curacion} HP")

    def aum_daño(self, aliado):
        aliado.daño += self.bono_daño
        print(f"{self.nombre} ha aumentado el daño de {aliado.nombre} en {self.bono_daño} puntos de daño")

    def mostrar_stats(self):
        super().mostrar_stats()
        print(f"Bono de daño: {self.bono_daño} \nCuración: {self.curacion}")

class Comida: #Dependencia
    def __init__(self, comida):
        self.comida = comida

    def describir(self):
        print(f"solo es {self.comida}...")

def main():
    #Creación de objetos persoje
    Zelda = Personaje("Zelda", 900, 30)
    Guts = Personaje("Guts", 1000, 49)
    Dynamo = Mago("Dynamo", 700, 20, "viento", 60)
    personajes = [Zelda, Guts, Dynamo] #Lista de personajes disponibles

    #Personaje tipo soporte (No se puede seleccionar, solo usar en otro psj)
    Xuan = Support("Xuan", 1000, 10, 15, 50)
    
    #-------Objetos que pueden usar los personajes------#
    Estatua_Sendero = Estatua_curacion("Sendero verde")
    Estatua_Ciudad = Estatua_curacion("Ciudad real")
    Estatuas = [Estatua_Sendero, Estatua_Ciudad] #Lista de estatuas disponibles

    pollo = Comida("pollo")
    pescado = Comida("pescado")
    comidas = [pollo, pescado] #Lista de comidas disponibles

    Charizard = Mascota("Charizard", "Dragón", 50, 900)
    Pikachu = Mascota("Pikachu", "Ratón", 70, 500)
    mascotas = [Charizard, Pikachu] #Lista de mascotas disponibles

    Collar_Char = Collar("oro", "Charizard")
    Collar_Pik = Collar("oro", "Pikachu")

    #------Objetos para interactuar-----#
    Cantinero = NPC("Edward", "Cantinero")
    Guardia = NPC("Roy", "Guardia")
    lista_NPCs = [Cantinero, Guardia]

    while True: #Iniciar un ciclo para que el jugador seleccione un personaje
        try:
            print(f"Selecciona un personaje")
            selector = 0
            for i in personajes:
                print(f"{i.nombre} -- {selector}") #Imprimir lista de personaje
                selector +=1
            psj = int(input(f": ")) #Solicitar personaje a usar

            match psj: #Estructura para definir un personaje al jugador
                case 0:
                    jugador = personajes[psj]
                    personajes.remove(jugador) #Eliminar al personaje seleccionado de la lista de personajes (Para futurasa acciones)
                    print(f"Tu personaje es {jugador.nombre}")
                    break
                case 1:
                    jugador = personajes[psj]
                    personajes.remove(jugador)
                    print(f"Tu personaje es {jugador.nombre}")
                    break
                case 2:
                    jugador = personajes[psj]
                    personajes.remove(jugador)
                    print(f"Tu personaje es {jugador.nombre}")
                    break
                case _:
                    print(f"Ingresa un personaje adecuado")
        except ValueError: #Manejo de errores en caso de que el usuario ingrese un daro incorrecto
            print(f"Ingresa una opción adecuada")

    def accion_curar():
        while True:
            try:
                curacion = float(input((f"Ingresa la cantidad a curar: ")))
                if curacion <= 20:
                    return curacion
                else:
                    print(f"La curación debe ser menor a 21")
            except ValueError:
                print(f"Ingresa un dato válido")

    def accion_atacar():
        while True:
            try:
                selector = 0
                for i in personajes:
                    print(f"{i.nombre} -- {selector}") #Imprimir lista de personajes para atacar
                    selector +=1

                atcado = int(input((f"Ingresa el persobje a atacar: ")))
                match atcado:
                    case 0:
                        atacado_final = personajes[atcado]
                        return atacado_final
                    
                    case 1:
                        atacado_final = personajes[atcado]
                        return atacado_final

                    case _:
                        print(f"Ingresa una opción válida")

            except ValueError:
                print(f"Ingresa un dato válido")

    def accion_domesticar():
        while True:
            try:
                selector = 0
                for i in mascotas:
                    print(f"{i.nombre} -- {selector}") #Imprimir lista de mascotas a domesticar
                    selector +=1

                mascota = int(input((f"Ingresa la mascota a domesticar: ")))
                match mascota:
                    case 0:
                        mascota_final = mascotas[mascota]

                        if mascota_final == Charizard: #Asigna el collar correspondiente
                            collar_final = Collar_Char
                        elif mascota_final == Pikachu:
                            collar_final = Collar_Pik   
                        return mascota_final, collar_final
                    case 1:
                        mascota_final = mascotas[mascota]

                        if mascota_final == Charizard: #Asigna el collar correspondiente
                            collar_final = Collar_Char
                        elif mascota_final == Pikachu:
                            collar_final = Collar_Pik
                        return mascota_final, collar_final
                    case _:
                        print(f"Ingresa una opción válida")
            except ValueError:
                print(f"Ingresa un dato válido")
    
    def accion_atacar_mascota():
        while True:
            try:
                selector = 0
                for i in jugador.mascotas:
                    print(f"{i.nombre} -- {selector}") #Imprimir lista de mascotas para usar
                    selector +=1

                mascota = int(input((f"Ingresa la mascota a usar: ")))
                match mascota:
                    case 0:
                        mascota_final = jugador.mascotas[mascota]
                        return mascota_final
                    case 1:
                        mascota_final = jugador.mascotas[mascota]
                        return mascota_final
                    case 2:
                        mascota_final = jugador.mascotas[mascota]
                        return mascota_final
                    case _:
                        print(f"Ingresa una mascota correcta: ")
                    
            except ValueError:
                print(f"Ingresa una opción válida")
    
    def accion_usar_estatua():
        while True:
            try:
                selector = 0
                for i in Estatuas:
                    print(f" Estatua de {i.ubicacion} -- {selector}")
                    selector += 1
                
                estatua = int(input(f"Ingresa la estatua a usar: "))

                match estatua:
                    case 0:
                        estatua_sel = Estatuas[estatua]
                        return estatua_sel
                    case 1:
                        estatua_sel = Estatuas[estatua]
                        return estatua_sel
                    case _:
                        print(f"Ingresa una opción válida")

            except ValueError:
                print(f"Ingresa una opción válida")

    def accion_comer():
        while True:
            try:
                selector = 0
                for i in comidas:
                    print(f"{i.comida} -- {selector}")
                    selector += 1
                
                comida_sel = int(input(f"Ingresa la comida que quieras: "))

                match comida_sel:
                    case 0:
                        comida_fin = comidas[comida_sel]
                        return comida_fin
                    case 1:
                        comida_fin = comidas[comida_sel]
                        return comida_fin
                    case _:
                        print(f"Ingresa una opción válida")

            except ValueError:
                print(f"Ingresa una opción válida")

    def accion_NPC():
        while True:
            try:
                selector = 0
                for i in lista_NPCs:
                    print(f"{i.nombre} el {i.rol} -- {selector}")
                    selector += 1
                
                NPC_sel = int(input(f"Ingresa el NPC a hablar: "))

                match NPC_sel:
                    case 0:
                        NPC_final = lista_NPCs[NPC_sel]
                        return NPC_final
                    case 1:
                        NPC_final = lista_NPCs[NPC_sel]
                        return NPC_final
                    case _:
                        print(f"Ingresa una opción válida")

            except ValueError:
                print(f"Ingresa una opción válida")

    def separador():
        print(F"---------------------------------")
    while True:
        try:
            separador()
            print(f"  Selecciona qué quieres hacer")
            print(f"|---------- ACCIONES ---------|")
            print(f"| Curarse                    1|")
            print(f"| Atacar a alguien           2|")
            print(f"| Mostrar stats              3|")
            print(f"| Domesticar mascota         4|")
            print(f"| Atacar con mascota         5|")
            print(f"| Usar estatua               6|")
            print(f"| Comer                      7|")
            print(f"| Hablar con NPC             8|")
            print(f"| Usar support               9|")
            print(f"| Salir                     10|")
            separador()

            accion = int(input(f": "))

            match accion:
                case 1:
                    cantidad_curar = accion_curar()
                    jugador.curar(cantidad_curar)
                case 2:
                    sel_atacado = accion_atacar()
                    jugador.atacar(sel_atacado)
                case 3:
                    jugador.mostrar_stats()
                case 4:
                    if len(jugador.mascotas) < 3: #Verificar si el jugador puede tener más mascotas
                        sel_mascota, sel_collar = accion_domesticar()
                        jugador.tam_mascota(sel_mascota, sel_collar)
                        print(f"Mascotas de {jugador.nombre}: ")
                        for i in jugador.mascotas:
                            print(f"{i.nombre}")
                    else:
                        print(f"No puedes tener más mascotas")
                        print(f"Mascotas de {jugador.nombre}: ")
                        for i in jugador.mascotas:
                            print(f"{i.nombre}")
                case 5:
                    if len(jugador.mascotas) > 0: #Verificar si el jugador tiene mascotas
                        sel_mascota_atacar = accion_atacar_mascota()
                        sel_atacado_mascota = accion_atacar()
                        jugador.atacar_masc(sel_mascota_atacar, sel_atacado_mascota)
                    else:
                        print(f"Necesitas mascotas")
                case 6:
                    sel_estatua = accion_usar_estatua()
                    jugador.usar_estatua(sel_estatua)
                case 7: 
                    comer = accion_comer()
                    jugador.comer(comer)
                case 8:
                    sel_NPC = accion_NPC()
                    sel_NPC.Hablar(jugador)
                case 9:
                    Xuan.aum_daño(jugador)
                    Xuan.curar(jugador)
                case 10:
                    break
                case _:
                    print(f"¿Cómo llegaste aquí?")
        except ValueError:
            print(f"Ingresa una opción válida")
main()
