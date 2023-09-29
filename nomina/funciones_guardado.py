"""
    Este módulo contiene las funciones para guardar los datos de los empleados
"""
import os
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


def guardar_nomina(
    nombre: str,
    cargo: str,
    horas_trabajadas: int,
    salario_bruto: int,
    horas_extras_trabajadas: int,
    horas_extras: int,
    salud: int,
    pension: int,
    arl: int,
    salario_neto: int,
):
    """Guarda la nómina en un archivo de texto"""
    nombre_archivo = "nomina.txt"
    formato_tabla = (
        "{:<20} {:<18} {:<3} {:<13} {:<3} {:<11} {:<10} {:<10} {:<10} {:<13}"
    )
    existe_archivo = os.path.exists(nombre_archivo)

    with open(file=nombre_archivo, mode="a", encoding="utf8") as archivo:
        # Si el archivo no existe, se crea el encabezado
        if not existe_archivo:
            encabezado = [
                "Nombre",
                "Cargo",
                "HT",
                "Salario",
                "HE",
                "TPHE",
                "Salud",
                "Pensión",
                "ARL",
                "Total a pagar",
            ]
            archivo.write(formato_tabla.format(*encabezado) + "\n")
            # Linea divisora
            archivo.write("-" * 121 + "\n")

        # Se guarda la información del empleado
        empleado = [
            nombre,
            cargo,
            horas_trabajadas,
            dinero(salario_bruto),
            horas_extras_trabajadas,
            dinero(horas_extras),
            dinero(salud),
            dinero(pension),
            dinero(arl),
            dinero(salario_neto),
        ]
        archivo.write(formato_tabla.format(*empleado) + "\n")
