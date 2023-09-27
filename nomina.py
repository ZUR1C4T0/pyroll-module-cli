from utilidades.colores import *


def ingresar_empleado():
    """
    La función "ingresar_empleado" imprime un mensaje y espera a que el usuario presione enter.
    """
    print(verde("\n\tIngresar empleado\n"))
    print(magenta("Tipo de empleado: "))
    print("1. Administrativo")
    print("2. Operativo")

    opcion = input("\nIngrese una opción: ")


def imprimir_nomina():
    """
    La función "imprimir_nomina" imprime la palabra "Nómina" en verde y espera a que el usuario presione
    enter para continuar.
    """
    print(verde("\n\tNómina\n"))
