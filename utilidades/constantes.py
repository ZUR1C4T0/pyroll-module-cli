"""
Este archivo contiene las constantes que se usan en el programa.
"""
import os

arl = {
    "id": 1,
    "riesgo_1": 0.00522,  # 0.522%
    "riesgo_2": 0.01044,  # 1.044%
    "riesgo_4": 0.04350,  # 4.350%
}

admininstrativo = {
    "valor_hora": 20000,
    "valor_hora_extra": 25000,
    "arl": arl["riesgo_1"],
}

operativo = {
    "id": 2,
    "valor_hora": 40000,
    "valor_hora_extra": 0,
    "arl": {
        "oficios_generales": arl["riesgo_1"],
        "conductor": arl["riesgo_2"],
        "vigilante": arl["riesgo_4"],
    },
}


def limpiar_pantalla() -> None:
    """
    Esta función se encarga de limpiar la pantalla de la consola
    """
    os.system("cls" if os.name == "nt" else "clear")
