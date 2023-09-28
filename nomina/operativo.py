"""Módulo de operativos"""
from utilidades.colores import verde
from utilidades.constantes import Operativo
from nomina.funciones_obtener import obtener_nombre, obtener_cargo_operativo


def ingresar_operativo():
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
    # imprimir_volante()
    # guardar_nomina()
