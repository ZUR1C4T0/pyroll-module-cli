"""
    Este módulo contiene las funciones para guardar los datos de los empleados
"""
from utilidades.constantes import limpiar_pantalla
from utilidades.colores import azul, verde, cyan


def dinero(monto: float) -> str:
    """Devuelve el monto en formato de dinero"""
    return f"$ {monto:,.0f}"


def porcentaje(monto: float) -> str:
    """Devuelve el monto en formato de porcentaje"""
    return f"{monto*100:.2f} %"


def imprimir_volante(
    nombre: str,
    cargo: str,
    horas_trabajadas: int,
    salario_bruto: int,
    horas_extras_trabajadas: int,
    horas_extras: int,
    salud: int,
    pension: int,
    arl: int,
    riesgo_arl: float,
    descuentos: int,
    salario_neto: int,
):
    """Imprime el volante de pago de un empleado"""
    limpiar_pantalla()
    print()
    print(azul("*************************************************"))
    print(azul("**************** VOLANTE DE PAGO ****************"))
    print(azul("*************************************************"))
    print()
    print(f"Nombre: {nombre}")
    print(f"Cargo: {cargo}")
    print(f"Horas trabajadas (mes): {horas_trabajadas}")
    print(f"Salario bruto: {dinero(salario_bruto)}")
    print(f"Horas extras trabajadas: {horas_extras_trabajadas}")
    print(f"Total Horas Extras: {dinero(horas_extras)}")
    print()
    print(azul("*************************************************"))
    print(azul("*************** DESCUENTOS DE LEY ***************"))
    print(azul("*************************************************"))
    print()
    print(f"Salud: {dinero(salud)}")
    print(f"Pensión: {dinero(pension)}")
    print(f"ARL ({porcentaje(riesgo_arl)}): {dinero(arl)}")
    print(f"Total descuentos: {dinero(descuentos)}")
    print()
    print(verde("Total a pagar: ") + dinero(salario_neto))
    print()
    print(azul("*************************************************"))
    print(azul("************ FIN DEL VOLANTE DE PAGO ************"))
    print(azul("*************************************************"))
    input(cyan("\nPresione ENTER para continuar..."))
