# PROYECTO

## ANÁLISIS DE LA CONTRATACIÓN PÚBLICA EN BARRANCABERMEJA


# 1. CONTEXTO

Este proyecto busca analizar las dinámicas de contratación pública de la Alcaldía Distrital de Barrancabermeja utilizando información disponible en SECOP II.

Debido a las diferencias históricas en la implementación de SECOP II, no se asumirá automáticamente que todos los años de ambas administraciones tienen el mismo nivel de cobertura.

Antes de realizar cualquier comparación se deberán establecer periodos homogéneos y metodológicamente comparables.

## 3.2 Personas naturales contratadas

Determinar cuántas personas naturales diferentes fueron contratadas mediante CPS durante cada administración.

Diferenciar entre:

* Número de contratos.
* Número de personas únicas.
* Número de contratos por persona.

## 3.3 Duración de los contratos

Analizar cuánto duran los contratos de prestación de servicios en cada administración.

Calcular:

* Duración promedio.
* Duración mediana.
* Percentiles de duración.
* Distribución de contratos por rangos de meses.

Rangos iniciales:

* Hasta 3 meses.
* Más de 3 y hasta 4 meses.
* Más de 4 y hasta 6 meses.
* Más de 6 y hasta 9 meses.
* Más de 9 y hasta 12 meses.
* Más de 12 meses.

## 3.4 Valor mensual equivalente

No limitar el análisis al valor total de cada contrato.

Calcular:

Valor mensual equivalente = Valor del contrato / Duración estimada en meses.

Esto permitirá identificar diferencias entre contratos de distinto tiempo de ejecución.

## 3.5 Contratistas recurrentes

Identificar personas que hayan recibido varios contratos dentro de una misma administración.

Determinar:

* Contratos por persona.
* Primera contratación.
* Última contratación.
* Número de años con contratación.
* Valor acumulado contratado.
* Tiempo acumulado contratado.

## 3.6 Renovaciones y continuidad

Analizar si una persona recibe contratos consecutivos o cercanos temporalmente.

Calcular los días existentes entre la terminación de un contrato y el inicio del siguiente.

Clasificar inicialmente las renovaciones en:

* 0 a 7 días.
* 8 a 30 días.
* 31 a 90 días.
* Más de 90 días.

## 3.7 Contratistas compartidos entre gobiernos

Identificar personas naturales que hayan tenido contratos durante las administraciones de Alfonso Eljach y Jonathan Vásquez.

Determinar:

* Número de personas compartidas.
* Porcentaje de continuidad.
* Número de contratos recibidos en cada administración.
* Valor contratado en cada administración.
* Duración acumulada.

## Preguntas principales

* ¿Aumenta el número de personas naturales contratadas?

* ¿Aparecen más contratistas nuevos?

* ¿Aumentan las renovaciones?

* ¿Cambian las duraciones de los contratos?

* ¿Cambian los valores mensuales?

* ¿Existen picos particulares de contratación?


# VARIABLES PRINCIPALES

La base analítica deberá incluir, cuando estén disponibles, las siguientes variables:

* ID del contrato.
* Número del contrato.
* Fecha de firma.
* Fecha de inicio.
* Fecha de terminación.
* Año.
* Mes.
* Administración.
* Año de gobierno.
* Tipo de contrato.
* Modalidad de contratación.
* Objeto contractual.
* Descripción.
* Documento del proveedor.
* Tipo de documento.
* Nombre del proveedor.
* Persona natural o jurídica.
* Valor del contrato.
* Duración en días.
* Duración estimada en meses.
* Valor mensual equivalente.
* Código UNSPSC.

# 8. VARIABLES DERIVADAS

Durante el procesamiento se crearán variables como:

* alcalde
* año
* mes
* año_gobierno
* es_cps
* es_persona_natural
* duracion_dias
* duracion_meses
* valor_mensual_equivalente
* numero_contratos_persona
* contrato_numero_persona
* es_recontratacion
* dias_desde_contrato_anterior
* contratista_compartido
* periodo_electoral
* periodo_preelectoral

# 9. INDICADORES PRINCIPALES

## Volumen

* Número total de CPS.
* CPS por mes.
* CPS por año.

## Personas

* Número de personas naturales.
* Personas contratadas por mes.
* Personas nuevas.
* Personas recurrentes.

## Recurrencia

* Contratos por persona.
* Personas con 2 o más contratos.
* Personas con 3 o más contratos.
* Personas con 5 o más contratos.

## Duración

* Duración promedio.
* Duración mediana.
* Distribución por rangos.

## Valores

* Valor total contratado.
* Valor mediano por contrato.
* Valor mensual equivalente.
* Valor acumulado por persona.

## Continuidad

* Personas contratadas por ambos gobiernos.
* Porcentaje de contratistas que continúan.
* Tiempo promedio de permanencia.

# 10. PREGUNTAS SEMILLA

## Contratación

* ¿Cómo evoluciona la contratación?

* ¿Existen meses con concentraciones atípicas de contratos?

## Personas

* ¿Cuántas personas diferentes contrata cada administración?

* ¿Una administración utiliza más contratos para contratar a menos personas?

* ¿Cuántos contratos recibe normalmente una persona?

## Duración

* ¿Cuánto dura normalmente un CPS?

* ¿Existen diferencias importantes entre administraciones?

* ¿Predominan contratos de cuatro, seis, ocho o más meses?

## Valores

* ¿Cuáles son los CPS de mayor valor?

* ¿Cuáles tienen mayor valor mensual equivalente?

* ¿Qué personas acumulan mayores valores contratados?

## Permanencia

* ¿Qué personas reciben contratos repetidamente?

* ¿Quiénes permanecen durante varios años?

* ¿Qué contratistas pasan de una administración a otra?

# 11. CRITERIOS METODOLÓGICOS

Los datos serán tratados como evidencia estadística.

Un patrón encontrado en SECOP II no será considerado automáticamente una irregularidad.

Se distinguirá entre:

1. Hallazgo estadístico.
2. Patrón relevante.
3. Caso que requiere revisión documental.
4. Evidencia documental comprobada.

No se utilizarán expresiones como corrupción, clientelismo, favorecimiento, direccionamiento o irregularidad únicamente a partir de correlaciones o patrones estadísticos.

# 12. PRINCIPIOS DE CALIDAD DE DATOS

Antes de cualquier análisis se deberá:

* Revisar duplicados.
* Revisar valores nulos.
* Normalizar documentos.
* Normalizar nombres.
* Identificar personas naturales.
* Separar personas jurídicas.
* Revisar estados contractuales.
* Revisar contratos anulados o cancelados.
* Validar fechas.
* Validar valores monetarios.
* Identificar posibles registros duplicados.

# 13. ESTRUCTURA DE DATOS

## datos/brutos

Información descargada directamente de SECOP II.

No deberá modificarse.

## datos/intermedios

Información limpia, homologada y transformada.

## datos/procesados

Bases definitivas destinadas al análisis.

## notebooks

Proceso analítico reproducible.

## entregables

Tablas, gráficos, informes y dashboards producidos a partir del análisis.

# 14. RESULTADO ESPERADO

Construir una investigación basada en datos que permita explicar de manera comprensible cómo funcionan las dinámicas de contratación por prestación de servicios en Barrancabermeja y cómo cambian entre administraciones y diferentes momentos del ciclo político.

El propósito no será partir de una acusación, sino permitir que los datos revelen patrones, diferencias, continuidades y casos que posteriormente puedan ser verificados mediante investigación periodística y fuentes documentales.
