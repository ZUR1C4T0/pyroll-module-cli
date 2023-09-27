# Payroll Module CLI

> Interfaz de Línea de Comandos de un Módulo de Nómina

## ACTIVIDAD DE TRANSFERENCIA DEL CONOCIMIENTO

Transportes Del Gran Caribe Colombiano SCA - TansCaribeCol, ha contratado a un grupo de
tres(3) personas para desarrollar un módulo sobre la nónima del personal de esta empresa,
en este caso se solicita que este módulo sea guardado a través de un archivo plano(\*.txt)
para luego la gerencia lo carga en un módulo para la confirmación y pago de salarios de
sus empleados y trabajadores oficiales.

Debe tener en cuenta un menú principal con los siguientes requerimientos:

1. El empleado si es **ADMINISTRATIVO**, tiene una asignación de _$20,000_ hora más
   prestaciones de ley. Si trabaja horas extras, la asignación será de _$25,000_ por hora
   extra trabajada y se tiene en cuenta para sus prestaciones. Importante: La ARL para los
   administrativos es Riesgo I (0,522%)

   Requiere que en volante de pago se imprima de la siguiente forma:

   ```text
   *************************************************
   **************** VOLANTE DE PAGO ****************
   *************************************************
   Nombre: Ana Maria Jaimes González
   Cargo: Auxiliar Administrativo
   Horas Trabajadas (mes): 40
   Salario Bruto: $800,000
   Horas Extras: 20
   Total pago Horas Extras: $500,000

   *************************************************
   *************** DESCUENTOS DE LEY ***************
   *************************************************
   Salud(4%): $52,000
   Pensión: $52,000
   ARL(0,522%): $6,786
   Total Descuentos: $104,000

   Total a pagar: $1,189,214

   *************************************************
   ************ FIN DEL VOLANTE DE PAGO ************
   *************************************************
   ```

2. El empleado si es **OPERATIVO** (Trabajador Oficial), tiene una asignación de _$40,000_ por
   hora pero debe cancelar de forma autónoma los aportes a la seguridad social teniendo
   en cuenta el cargo y las horas laboradas mensualmente:

   - Conductor: 160 horas mensuales
   - Oficios Generales: 100 horas mensuales
   - Vigilancia: 336 horas mensuales

3. Tenga en cuenta que los aportes a la Seguridad Social debe hallar el Índice Base de
   cotización que equivale al 40% y luego hallar los porcentajes correspondientes:

   - Salud: 12.5%
   - Pensión: 16%
   - ARL: De acuerdo al nivel del riesgo:
     - Oficios Generales equivale al Riesgo I: 0.522%
     - Conductor, Riesgo II: 1.044%
     - Vigilancia, Riesgo IV: 4.350%

   El volante debe ser similar a la opción pero no se tiene en cuenta las horas extras,
   teniendo en cuenta que este tipo de empleado está celebrando un contrato de prestación de
   servicios.

   La información debe mostrarse en una estructura de datos(Matriz, ArrayList) y que en el
   archivo TXT debe guardarlo de la siguiente forma:

   | Nombre                    | Tipo           | Cargo                   | HT  | Salario | HE  | TPHE   | Salud  | Pension | ARL  | Total a pagar |
   | ------------------------- | -------------- | ----------------------- | --- | ------- | --- | ------ | ------ | ------- | ---- | ------------- |
   | Ana María Jaimes González | ADMINISTRATIVO | Auxiliar Administrativo | 40  | 800000  | 20  | 500000 | 52000  | 52000   | 6786 | 1189124       |
   | Blanca Luz Iglesias Serpa | OPERATIVO      | Oficios Generales       | 100 | 4000000 | 0   | 0      | 200000 | 256000  | 8352 | 3535648       |

4. Actividades de evaluación
   | Evidencias de Aprendizaje | Criterios de Evaluación | Técnicas e Instrumentos de Evaluación |
   | ------------------------- | ----------------------- | ------------------------------------- |
   | **Evidencias de Desempeño:**<br>Demostración de un proceso de codificación de software de acuerdo a una situación problema planteada por el usuario.<br>**Evidencias de Producto:**<br>Valoración del funcionamiento de la aplicación y consultas generadas en el proyecto. | Realiza algoritmos utilizando atributos, objetos, métodos.<br>Utiliza las herramientas de programación orientadas a objetos, aplicando las funciones propias de los lenguajes de programación con sus respectivos stack de acuerdo con las necesidades del software.<br>Codifica los módulos del software siguiendo estándares de programación.<br>Genera las interfaces de captura y presentación de datos para el software. | **Técnica:** Valoración del producto.<br>**Instrumento de Evaluación:** Lista de chequeo de producto. |
