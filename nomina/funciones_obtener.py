"""
    Este modulo contiene las funciones que obtienen los datos de los empleados
"""
from utilidades.colores import rojo, cyan, magenta, amarillo
from utilidades.constantes import limpiar_pantalla


def obtener_nombre(titulo: str) -> str:
    """La función "obtener_nombre" solicita al usuario el nombre del empleado
    y lo retorna.

    Returns
    -------
        nombre: str
            Nombre del empleado.
    """
    limpiar_pantalla()
    print(titulo)
    nombre = input("Ingrese el nombre del empleado: ")
    return nombre


def obtener_horas_trabajadas(titulo: str) -> int:
    """La función "obtener_horas_trabajadas" solicita al usuario que ingrese el
    número de horas trabajadas y lo devuelve como un número entero.

    Parameters
    ----------
    titulo : str
        El parámetro "título" es una cadena que representa el título o solicita
        al usuario que ingrese la cantidad de horas trabajadas.

    Returns
    -------
        el número de horas trabajadas como un número entero.

    """
    limpiar_pantalla()
    print(titulo)
    try:
        horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
        return horas_trabajadas
    except ValueError:
        limpiar_pantalla()
        print(rojo("\tValor inválido\n"))
        input(cyan("Presione enter para continuar..."))
        return obtener_horas_trabajadas(titulo)


def obtener_horas_extras_trabajadas(titulo: str) -> int:
    """La función "obtener_horas_extras_trabajadas" solicita al usuario que
    ingrese el número de horas extras trabajadas y lo devuelve como un número
    entero.

    Parameters
    ----------
    titulo : str
        El parámetro "titulo" es una cadena que representa el título o
        encabezado del mensaje o mensaje que se mostrará al usuario.

    Returns
    -------
        el número de horas trabajadas como un número entero.
    """
    limpiar_pantalla()
    print(titulo)
    try:
        horas_extras_trabajadas = int(input("Ingrese las horas extras trabajadas: "))
        return horas_extras_trabajadas
    except ValueError:
        limpiar_pantalla()
        print(rojo("\tValor inválido\n"))
        input(cyan("Presione enter para continuar..."))
        return obtener_horas_extras_trabajadas(titulo)


def obtener_cargo_operativo(titulo: str) -> str:
    """La función "obtener_cargo_operativo" permite al usuario seleccionar un
    puesto de trabajo de una lista y devuelve el puesto seleccionado como una
    cadena.

    Parameters
    ----------
    titulo : str
        El parámetro `titulo` es una cadena que representa el título o
        encabezado del menú o mensaje que se muestra al usuario.

    Returns
    -------
        una cadena que representa la carga seleccionada del empleado.
    """
    limpiar_pantalla()
    print(titulo)
    print(amarillo("Seleccione el cargo del empleado"))
    print("1. Conductor")
    print("2. Oficios generales")
    print("3. Vigilante")
    try:
        opcion = int(input(magenta("\nIngrese una opción: ")))
        if opcion == 1:
            return "conductor"
        elif opcion == 2:
            return "oficios_generales"
        elif opcion == 3:
            return "vigilante"
        else:
            raise ValueError
    except ValueError:
        limpiar_pantalla()
        print(rojo("\tOpción inválida\n"))
        input(cyan("Presione enter para continuar..."))
        return obtener_cargo_operativo(titulo)
