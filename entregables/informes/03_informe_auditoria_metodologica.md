# Auditoría metodológica y hoja de ruta de mejoras
## Proyecto: Análisis de la contratación pública en Barrancabermeja (SECOP II)
### Comparación administraciones Alfonso Eljach vs Jonathan Vásquez

**Rol:** Consultoría senior de ciencia de datos
**Fecha:** 7 de septiembre de 2026
**Alcance revisado:** `docs/proyecto-objetivos.md`, `notebooks/01_descarga_secop_ii.ipynb`, `notebooks/02_limpieza_calidad.ipynb`, bases en `datos/intermedios` y `datos/procesados`, manifiestos y auditorías.
**Corte de datos:** 2026-09-06 · 37.574 contratos · 9 entidades locales.

---

## 1. Veredicto ejecutivo

El proyecto está **muy por encima del estándar** de un análisis periodístico de datos: identidad de entidad por NIT (no por ciudad), llave de proveedor por documento, política explícita de nulos y estados, jerarquía de familias contractuales trazable, semáforo de calidad reproducible y un manifiesto metodológico versionado. La base actual (`02_v4`) merece con razón el estado *"Aprobada con advertencias controladas"*.

Sin embargo, la base **todavía no estaba lista para comparar administraciones sin sesgo**. Existían cuatro brechas que, de pasar directamente a la fase de análisis, habrían producido **conclusiones estadísticamente incorrectas** — precisamente el riesgo que un medio no puede correr. Las cuatro se han corregido en el nuevo `notebook 03`, y su impacto está cuantificado abajo.

> **El hallazgo que resume todo.** Con el dato **nominal** y la ventana **calendario** heredada, el valor mensual de los CPS de Jonathan aparece **+29 %** sobre el de Alfonso. Corrigiendo por inflación (pesos constantes) **y** comparando los **mismos meses de gobierno**, la diferencia se **invierte a −14 %**. La conclusión cambia de signo. Publicar la primera cifra sería un error de datos, no de redacción.

| Ventana de comparación | Brecha valor mensual **nominal** | Brecha **real + alineada** |
|---|---:|---:|
| 24 meses calendario (heredada, no alineada) | +29,1 % | +6,4 % |
| Año 3 al mismo corte (alineada) | +13,8 % | **−14,3 %** |
| Meses de gobierno 16–33 (nueva, alineada) | +15,4 % | **−14,3 %** |

*(+ = Jonathan paga más por mes; − = Alfonso paga más. Universo: CPS estricto de la Alcaldía, subtipo claro.)*

---

## 2. Lo que ya estaba bien hecho (y debe conservarse)

Reconocer esto importa, porque las mejoras se apoyan en estos cimientos:

- **Entidad por NIT `890201900`, no por ciudad.** Evita el error clásico de atribuir a la Alcaldía contratos de otras entidades o perder los suyos cuando `ciudad = No Definido`. La ESE Barrancabermeja se analiza aparte. Correcto y bien auditado (`flag_inconsistencia_alcaldia = 0`).
- **Identidad del proveedor por documento normalizado**, con nombre canónico solo para presentación y auditoría de documentos con varios nombres/tipos. Es la decisión correcta para medir *personas únicas* y *contratistas compartidos*.
- **Política de nulos sin imputación** y **exclusión de estados no resueltos** (borrador, anulado, cancelado…). Preserva la honestidad de cada métrica.
- **Jerarquía de familias contractuales** que prioriza el tipo SECOP y separa CPS estricto / ampliado, ESAL solo con persona jurídica, régimen especial, etc. La distinción CPS *estricto vs probable* como análisis de sensibilidad es de nivel profesional.
- **Deduplicación por llave de contrato con puntaje de completitud** (se verificó: 0 IDs duplicados en el universo).
- **Ventanas comparables y advertencia de cobertura desigual** ya presentes en el manifiesto, más el marcado de outliers por entidad/subtipo/año **sin eliminarlos**. Excelente criterio.
- **Semáforo de calidad y manifiesto versionado.** Reproducibilidad real.

---

## 3. Riesgos de sesgo detectados y su prioridad

### P0 — Habrían distorsionado la conclusión principal

**3.1 Valores nominales comparados entre años (sesgo inflacionario).**
SECOP registra pesos corrientes. La inflación colombiana del periodo fue alta y desigual (2022: 13,1 %; 2023: 9,3 %; 2024: 5,2 %; 2025: 5,1 % — DANE). Comparar el valor mensual de 2022 con el de 2025 sin deflactar **sobreestima mecánicamente** a la administración más reciente en ~20–30 %. Es la causa directa de la falsa brecha "+29 %".
→ *Corregido:* deflactor IPC mensual, valores en pesos constantes de 2025 (`valor_contrato_real`, `valor_mensual_real`).

**3.2 Ventana de comparación no alineada por año de gobierno.**
La ventana heredada de 24 meses comparaba los **años 3–4 de Alfonso** (2022–2023) contra los **años 1–2 de Jonathan** (2024–2025). El inicio y el fin de un mandato tienen dinámicas de contratación opuestas (arranque vs cierre), así que la ventana mezcla *fase del mandato* con *identidad del alcalde*. Además, el **año 4 de Alfonso es su año electoral**, con la distorsión de la ley de garantías incluida solo en su lado.
→ *Corregido:* `mes_gobierno` / `anio_gobierno` en el cuaderno 02, y ventana alineada **meses 16–33** en el 03 (18 meses en los que ambos tienen cobertura confiable); se conserva la ventana calendario, pero **marcada como secundaria**.

El desglose por año de gobierno deja ver el problema de raíz con crudeza:

| Año de gobierno | Alfonso Eljach | Jonathan Vásquez |
|---|---:|---:|
| Año 1 | **7** | 4.853 |
| Año 2 | 3.035 | 4.991 |
| Año 3 | 5.855 | 4.399 *(parcial, corte 6-sep)* |
| Año 4 | 4.790 | — |

Los 7 contratos del primer año de Alfonso no son austeridad: son ausencia de SECOP II. Por eso la comparación honesta empieza en su mes 16.

### P1 — Componente central del proyecto sin operacionalizar

**3.3 Calendario electoral y ley de garantías ausentes de la base.**
El análisis del ciclo político es, según los objetivos, un *componente principal*, pero las variables `periodo_electoral` / `periodo_preelectoral` no existían en la base y la ventana de restricción de contratación directa no estaba marcada. La evidencia empírica es contundente y no debe quedar sin variable: los CPS de la Alcaldía muestran un **pico de 2.223 contratos en junio de 2023** seguido de un **congelamiento casi total (1, 1, 4 contratos) entre julio y octubre de 2023** — la firma clásica de la carrera previa y la posterior restricción antes de la elección del 29 de octubre de 2023.
→ *Corregido en el cuaderno 02:* `periodo_electoral`, `periodo_preelectoral`, `ventana_ley_garantias`, `tipo_anio_electoral`, `dias_a_prox_eleccion`, con anclas 2019/2023/2027. La validación cruzada confirma el mecanismo: el pico de junio ocurre **justo antes** de que arranque la ventana el 29 de junio, y los pocos contratos de julio–octubre quedan correctamente marcados dentro de ella.

### P2 — Mejoras de robustez (recomendadas, no bloqueantes)

- **3.4 Claridad de subtipo CPS de Alfonso al 89,9 %** (semáforo en *warning*). Aceptable, pero al comparar "profesional vs apoyo" conviene reportar siempre el % clasificado y hacer el corte solo sobre `tipo_cps_claro` (ya se hace en las tablas nuevas).
- **3.5 Censura a la derecha en 2026.** El año en curso está incompleto (corte 6-sep) y su tercer trimestre puede tener contratos aún no publicados. Las ventanas alineadas lo neutralizan al usar el "mismo corte", pero cualquier gráfico de tendencia debe marcar 2026 como parcial.
- **3.6 Valor mensual en contratos muy cortos.** Dividir por fracciones de mes infla el equivalente mensual; el flag de outliers por percentil 0,5 %/99,5 % ya lo contiene, pero conviene reportar mediana (no media) y excluir `duracion < 1 mes` de los rankings de valor mensual.
- **3.7 `dias_adicionados` (prórrogas).** Bien auditados por separado; para "duración real" ofrecer una variante de sensibilidad que los sume, sin mezclarla con la duración pactada.

---

## 4. Qué se implementó y dónde

La corrección se repartió entre los dos cuadernos siguiendo un criterio único y defendible:

> **Los atributos deterministas del contrato viven en el `02`. Las decisiones de análisis viven en el `03`.**

Un atributo determinista depende solo de la fecha y la entidad (no admite discusión). Una decisión de análisis depende de un supuesto externo o de un criterio de comparación (sí admite discusión, y por eso debe quedar aislada y ser fácil de auditar o cambiar).

### 4.1 En `02_limpieza_calidad.ipynb` (base `02_v5`)

Se insertó la celda **18B · Año de gobierno, calendario electoral y ley de garantías**, justo después de la creación de periodos metodológicos, sin alterar ninguna otra celda:

- `mes_gobierno` (1–48) y `anio_gobierno` — posición del contrato dentro del mandato.
- `periodo_electoral` y `periodo_preelectoral` — las variables que ya pedía el documento de objetivos (sección 8) y que no existían.
- `ventana_ley_garantias` — 4 meses previos a cada elección territorial (2019, 2023, 2027).
- `tipo_anio_electoral` y `dias_a_prox_eleccion`.

El manifiesto subió a `02_v5` documentando anclas electorales e inicio de mandatos. **El semáforo de calidad quedó idéntico** (mismos 14 controles, mismos valores): la adición no alteró ninguna métrica existente.

### 4.2 En `03_ajustes_metodologicos_comparabilidad.ipynb`

No limpia, no reclasifica y **no recalcula atributos del contrato**: los verifica y los consume del `02` (falla con mensaje claro si la base no es `02_v5` o superior). Aporta solo:

1. **Deflactor IPC.** Índice mensual interpolado desde las variaciones anuales DANE (dic–dic), año base 2025, parámetros editables. Genera `valor_contrato_real` y `valor_mensual_real`. *Hook* documentado para sustituir por la serie mensual oficial del IPC antes de publicar.
2. **Ventanas alineadas.** Ventana de meses de gobierno 16–33 (la intersección real de cobertura), comparaciones nominal-vs-real por ventana, brechas, recurrencia y personas por mes en términos reales.

**Salidas:** `datos/procesados/03_base_analitica_enriquecida.parquet`, `03_cps_alcaldia_enriquecido.parquet`; `entregables/tablas/03_*.csv`; `datos/intermedios/03_manifiesto_comparabilidad.json`.

Ambos cuadernos fueron **ejecutados en cadena de extremo a extremo sin errores**, con prueba de regresión: semáforo de calidad, brechas nominal-vs-real y resumen de ventana alineada resultaron **idénticos** antes y después de repartir las variables entre cuadernos.

---

## 5. Reglas de comunicación para el medio (para evitar titulares sesgados)

Estas reglas convierten el rigor técnico en neutralidad editorial:

1. **Dinero siempre en pesos constantes.** Ninguna comparación de valores entre años o administraciones en pesos nominales. Etiquetar los gráficos: *"pesos constantes de 2025 (IPC-DANE)"*.
2. **Volúmenes solo en ventanas alineadas por mes de gobierno.** Nunca comparar un mandato completo contra otro parcial, ni año electoral contra año ordinario, sin decirlo.
3. **Cobertura ≠ actividad.** La escasez de registros de 2020–2021 es adopción tardía de SECOP, no "menos contratación". Debe advertirse siempre.
4. **La ley de garantías explica picos y caídas.** El pico de junio de 2023 y el vacío de julio–octubre son calendario electoral, no necesariamente conducta discrecional.
5. **Lenguaje de evidencia, no de acusación.** Mantener la escala de los objetivos: hallazgo estadístico → patrón relevante → caso a revisar → evidencia documental. Un patrón no es una irregularidad.

---

## 6. Recomendaciones pendientes (siguientes cuadernos)

- **Cuaderno 04 (análisis):** correr todas las métricas de los objetivos (personas únicas, recurrencia, renovaciones, contratistas compartidos, rankings) **sobre la ventana alineada y en pesos reales**, reportando siempre nominal como anexo.
- **Renovaciones (`dias_desde_contrato_anterior`):** implementar por `proveedor_llave` ordenado por fecha, con las bandas 0–7 / 8–30 / 31–90 / >90 de los objetivos.
- **Contratistas compartidos:** intersección de documentos entre administraciones con valor real acumulado en cada una.
- **Serie mensual oficial IPC:** sustituir la interpolación por la serie DANE mensual antes de publicar.
- **Prueba estadística del efecto electoral:** comparar tasa mensual de CPS dentro vs fuera de ventana de garantías con intervalos, no solo el gráfico.
- **Verificación cruzada:** validar 8–10 contratos de alto valor contra SECOP en línea (`urlproceso`) antes de cualquier ranking nominal.

---

## 7. Anexo técnico — cifras de validación

Ventana alineada (meses de gobierno 16–33; Alfonso abr-2021→sep-2022, Jonathan abr-2025→sep-2026):

| Indicador | Alfonso Eljach | Jonathan Vásquez |
|---|---:|---:|
| Personas únicas (CPS) | 3.677 | 4.348 |
| Contratos CPS | 7.649 | 7.961 |
| Contratos por persona | 2,08 | 1,83 |
| % personas con 2+ contratos | 58,7 % | 50,9 % |
| CPS por mes | 424,9 | 442,3 |
| Personas por mes | 204,3 | 241,6 |
| Valor mensual mediano **real** | ~3,48 M | ~2,98 M |

Lectura coherente y defendible: Jonathan contrata a **más personas** y con **menor recurrencia**, a un **valor mensual real algo menor**. Es una narrativa que los datos sostienen — a diferencia del "paga 29 % más" que produce el dato nominal sin alinear.

*IPC (variación anual dic–dic, DANE): 2021 5,62 % · 2022 13,12 % · 2023 9,28 % · 2024 5,20 % · 2025 5,10 %. Base del deflactor: pesos de mediados de 2025.*
