"""
    Este módulo contiene las funciones que ejecutará el menú principal del
    programa.
"""
import os
from nomina.administrativo import ingresar_administrativo
from nomina.operativo import ingresar_operativo
from utilidades.colores import verde, rojo, cyan, magenta
from utilidades.constantes import limpiar_pantalla, Administrativo, Operativo


def ingresar_empleado() -> None:
    """La función "ingresar_empleado" permite al usuario ingresar información
    de un nuevo empleado, ya sea administrativo u operativo.

    Returns
    -------
        nada.
    """
    limpiar_pantalla()
    print(verde("\tIngresar empleado\n"))
    print("1. Administrativo")
    print("2. Operativo")
    print("0. Volver")

    try:
        opcion = int(input(magenta("\nIngrese una opción: ")))
        if opcion == Administrativo().id:
            ingresar_administrativo()
        elif opcion == Operativo().id:
            ingresar_operativo()
        elif opcion == 0:
            return None
        else:
            raise ValueError
    except ValueError:
        limpiar_pantalla()
        print(rojo("\tOpción inválida\n"))
        input(cyan("Presione enter para continuar..."))
        return ingresar_empleado()


def imprimir_nomina():
    """
    La función "imprimir_nomina" imprime el contenido de un archivo llamado
    "nomina.txt" y espera a que el usuario presione enter para continuar.
    """
    limpiar_pantalla()
    print(verde("\tNómina\n"))

    existe_archivo = os.path.exists("nomina.txt")

    if not existe_archivo:
        print(rojo("No hay empleados registrados\n"))
        input(cyan("Presione enter para continuar..."))
        return None

    with open(file="nomina.txt", mode="r", encoding="utf8") as nomina:
        print(nomina.read())
        input(cyan("\nPresione enter para continuar..."))
