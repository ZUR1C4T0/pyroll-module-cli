"""
Este archivo contiene los colores que se usan en el programa.
"""

# Estilos
SIN_ESTILO = "\033[0m"
NEGRITA = "\033[1m"

# Colores
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"


# Funciones
def rojo(texto: str) -> str:
    """
    Retorna el texto en color rojo.
    """
    return f"{ROJO}{texto}{SIN_ESTILO}"


def verde(texto: str) -> str:
    """
    Retorna el texto en color verde.
    """
    return f"{VERDE}{texto}{SIN_ESTILO}"


def amarillo(texto: str) -> str:
    """
    Retorna el texto en color amarillo.
    """
    return f"{AMARILLO}{texto}{SIN_ESTILO}"


def azul(texto: str) -> str:
    """
    Retorna el texto en color azul.
    """
    return f"{AZUL}{texto}{SIN_ESTILO}"


def magenta(texto: str) -> str:
    """
    Retorna el texto en color magenta.
    """
    return f"{MAGENTA}{texto}{SIN_ESTILO}"


def cyan(texto: str) -> str:
    """
    Retorna el texto en color cyan.
    """
    return f"{CYAN}{texto}{SIN_ESTILO}"
