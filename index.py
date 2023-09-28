"""
Este es el módulo principal del programa
"""
from utilidades.colores import verde, rojo, cyan, amarillo, magenta
from utilidades.constantes import limpiar_pantalla
from sub_index import ingresar_empleado, imprimir_nomina


def main():
    """
    Esta es la función principal del programa
    """
    while True:
        limpiar_pantalla()
        print(verde("\tBienvenido al sistema de nómina de la empresa\n"))
        print("1. Ingresar empleado")
        print("2. Imprimir nómina")
        print("0. Salir")

        try:
            opcion = int(input(magenta("\nIngrese una opción: ")))
            if opcion == 1:
                ingresar_empleado()
            elif opcion == 2:
                imprimir_nomina()
            elif opcion == 0:
                break
            else:
                raise ValueError
        except ValueError:
            limpiar_pantalla()
            print(rojo("\tOpción inválida\n"))
            input(cyan("Presione enter para continuar..."))

    print(amarillo("\n\t¡Gracias por usar el sistema de nómina!\n"))


if __name__ == "__main__":
    main()
