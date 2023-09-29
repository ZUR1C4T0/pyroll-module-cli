"""Módulo de operativos"""
from utilidades.colores import verde
from utilidades.constantes import Operativo
from nomina.funciones_guardado import imprimir_volante, guardar_nomina
from nomina.funciones_obtener import obtener_nombre, obtener_cargo_operativo


def ingresar_operativo():
    """
    La función `ingresar_operativo()` es una función que calcula e imprime
    la nómina de un operativo.
    """
    titulo = verde("\tIngresar operativo\n")
    ope = Operativo()
    _cargo = obtener_cargo_operativo(titulo)
    cargo = ope.cargo[_cargo]
    nombre = obtener_nombre(titulo)
    horas_trabajadas = ope.horas_trabajadas[_cargo]
    horas_extras_trabajadas = 0

    salario_bruto = ope.valor_hora * horas_trabajadas
    horas_extras = ope.valor_hora_extra * horas_extras_trabajadas
    base_de_cotizacion = int(salario_bruto * 0.4)

    salud = int(base_de_cotizacion * 0.125)
    pension = int(base_de_cotizacion * 0.16)
    arl = int(base_de_cotizacion * ope.riesgo_arl[_cargo])
    descuentos = salud + pension

    salario_neto = salario_bruto + horas_extras - descuentos - arl
    imprimir_volante(
        nombre,
        cargo,
        horas_trabajadas,
        salario_bruto,
        horas_extras_trabajadas,
        horas_extras,
        salud,
        pension,
        arl,
        ope.riesgo_arl[_cargo],
        descuentos,
        salario_neto,
    )
    guardar_nomina(
        nombre,
        cargo,
        horas_trabajadas,
        salario_bruto,
        horas_extras_trabajadas,
        horas_extras,
        salud,
        pension,
        arl,
        salario_neto,
    )
