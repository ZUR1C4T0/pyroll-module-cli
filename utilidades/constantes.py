"""
Este archivo contiene las constantes que se usan en el programa.
"""
import os

arl: dict[str, float] = {
    "riesgo_1": 0.00522,  # 0.522%
    "riesgo_2": 0.01044,  # 1.044%
    "riesgo_4": 0.04350,  # 4.350%
}


class Administrativo:
    """Clase que representa un empleado administrativo"""

    id = 1
    valor_hora = 20000
    valor_hora_extra = 25000
    riesgo_arl = arl["riesgo_1"]
    cargo = "Administrativo"


class Operativo:
    """Clase que representa un empleado operativo"""

    id = 2
    valor_hora = 40000
    valor_hora_extra = 0
    cargo: dict[str, str] = {
        "oficios_generales": "Oficios generales",
        "conductor": "Conductor",
        "vigilante": "Vigilante",
    }
    riesgo_arl: dict[str, float] = {
        "oficios_generales": arl["riesgo_1"],
        "conductor": arl["riesgo_2"],
        "vigilante": arl["riesgo_4"],
    }
    horas_trabajadas: dict[str, int] = {
        "oficios_generales": 100,
        "conductor": 160,
        "vigilante": 336,
    }


def limpiar_pantalla() -> None:
    """
    Esta función se encarga de limpiar la pantalla de la consola
    """
    os.system("cls" if os.name == "nt" else "clear")
