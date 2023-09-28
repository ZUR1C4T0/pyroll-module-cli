"""Módulo de administrativo"""
from utilidades.constantes import Administrativo
from utilidades.colores import verde
from nomina.funciones_guardado import imprimir_volante
from nomina.funciones_obtener import (
    obtener_nombre,
    obtener_horas_trabajadas,
    obtener_horas_extras_trabajadas,
)


def ingresar_administrativo():
    titulo = verde("\tIngresar administrativo\n")
    adm = Administrativo()
    nombre = obtener_nombre(titulo)
    horas_trabajadas = obtener_horas_trabajadas(titulo)
    horas_extras_trabajadas = obtener_horas_extras_trabajadas(titulo)

    salario_bruto = adm.valor_hora * horas_trabajadas
    horas_extras = adm.valor_hora_extra * horas_extras_trabajadas

    salud = int((salario_bruto + horas_extras) * 0.04)
    pension = salud
    arl = int((salario_bruto + horas_extras) * adm.riesgo_arl)
    descuentos = salud + pension

    salario_neto = salario_bruto + horas_extras - descuentos - arl
    imprimir_volante(
        nombre,
        adm.cargo,
        horas_trabajadas,
        salario_bruto,
        horas_extras_trabajadas,
        horas_extras,
        salud,
        pension,
        arl,
        adm.riesgo_arl,
        descuentos,
        salario_neto,
    )
    # guardar_nomina()
