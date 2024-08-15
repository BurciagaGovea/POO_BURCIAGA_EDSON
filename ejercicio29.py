def main():
    while True:
        try:    
            print(f"|----------          ---------|")
            print(f"         Watcha wanna see?")
            print(f"|----------          ---------|")
            print(f"| Abstracción                1|")
            print(f"| Encapsulamiento            2|")
            print(f"| Herencia                   3|")
            print(f"| Polimorfsmo                4|")
            print(f"| Salir                      5|")
            print(f"|----------          ---------|")
            accion = int(input(f": "))

            match accion:
                case 1:
                    abstraccion()
                case 2:
                    encapsulamiento()
                case 3:
                    herencia()
                case 4:
                    polimorfismo()
                case 5:
                    break
                case _:
                    raise ValueError
        except ValueError:
            print(f"Ingresa una opción válida")

def abstraccion():
    print("La abstracción es un principio de la programación orientada a objetos que se centra en ocultar los detalles complejos y mostrar solo la información esencial. Permite a los desarrolladores trabajar con modelos simplificados de objetos sin preocuparse por su implementación interna.")

def encapsulamiento():
    print("El encapsulamiento se refiere a la práctica de agrupar datos y métodos que operan sobre esos datos en una sola unidad llamada objeto. Además, se protege el acceso a los datos internos del objeto mediante el uso de modificadores de acceso, evitando que otros objetos o funciones modifiquen el estado del objeto de manera no controlada.")

def herencia():
    print("La herencia es un mecanismo que permite crear nuevas clases basadas en clases existentes. La nueva clase, conocida como clase derivada o subclase, hereda los atributos y métodos de la clase base o superclase. Esto promueve la reutilización del código y facilita la creación de jerarquías de clases.")

def polimorfismo():
    print("El polimorfismo es la capacidad de un objeto para tomar muchas formas. En POO, permite que diferentes clases sean tratadas a través de una interfaz común, generalmente mediante la implementación de métodos con el mismo nombre pero con comportamientos diferentes en cada clase. Esto facilita la extensión y modificación del código sin alterar la interfaz pública.")

main()