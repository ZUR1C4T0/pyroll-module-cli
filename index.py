"""
Este es el módulo principal del programa
"""
from utilidades.colores import verde, rojo, cyan, amarillo
from utilidades.constantes import limpiar_pantalla
from nomina import ingresar_empleado, imprimir_nomina


def main():
    """
    Esta es la función principal del programa
    """
    run = True
    while run:
        limpiar_pantalla()
        print(verde("\tBienvenido al sistema de nómina de la empresa\n"))
        print("1. Ingresar empleado")
        print("2. Imprimir nómina")
        print("0. Salir")

        try:
            opcion = int(input("\nIngrese una opción: "))
            limpiar_pantalla()
            if opcion == 1:
                ingresar_empleado()
            elif opcion == 2:
                imprimir_nomina()
            elif opcion == 0:
                run = False
                continue
            else:
                raise ValueError
        except ValueError:
            print(rojo("\n\tOpción inválida\n"))
        finally:
            if run:
                input(cyan("Presione enter para continuar..."))
            else:
                print(amarillo("\n\tGracias por usar el sistema de nómina\n"))


if __name__ == "__main__":
    main()
