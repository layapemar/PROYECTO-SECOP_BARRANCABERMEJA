# Metodología · SECOP II Barrancabermeja

## Ejecución

Abrir cada notebook de `notebooks/` en orden y usar **Run All** (cada cuaderno busca solo la carpeta raíz que contiene `funciones/secop_utils.py`, así que puede abrirse desde `notebooks/` o desde la raíz):

1. `01_BASE_SECOP_II.ipynb`
2. `02_CALIDAD_IDENTIDAD.ipynb`
3. `03_CPS_PERSONAS.ipynb`
4. `04_COMPARABILIDAD.ipynb`
5. `05_TRAYECTORIAS_SIMULTANEIDAD.ipynb`
6. `06_HALLAZGOS_CIUDADANOS.ipynb`
7. `07_HISTORIA_CIUDADANA.ipynb` — historia ciudadana en siete actos (26 preguntas, de lo general a lo particular), prueba de estrés y epílogo metodológico; produce `historia_ciudadana.md` y `historia_ciudadana.html` (un solo archivo con gráficas incrustadas)

Requisitos: Python ≥ 3.11, pandas ≥ 2.2 (probado con 3.0.2), numpy (probado con 2.4), matplotlib (3.10), openpyxl, ipython.

**Importante:** ejecutar siempre con *Restart & Run All* y sin editar los cuadernos. Una edición local puede romper la cadena (por ejemplo, borrar el cuerpo de una función en el 06). Si se cambia algo, hay que volver a ejecutar desde esa etapa.
Código común: `funciones/secop_utils.py`.

- Entrada: la última corrida bruta validada en `datos/brutos/secop_ii/corridas/`. Nunca se modifica.
- Salidas: `datos/salidas/<etapa>/`, cada una con su `manifiesto.json` (hashes). Los punteros están en `datos/salidas/punteros/`.
- Cada etapa verifica los hashes de la anterior. Si cambia un archivo, obliga a re-ejecutar desde esa etapa.
- Salidas deterministas: dos ejecuciones completas producen datos, tablas y gráficas idénticos byte a byte (verificado con 120 archivos). Solo los manifiestos y punteros cambian, porque guardan la hora y el entorno.
- Las salidas de la v1 (`datos/intermedios`, `datos/05_pat`, `datos/06_pub`, `datos/07_storytelling`) no se usan ni se tocan.

## Correcciones frente a la auditoría

| Hallazgo de auditoría | Corrección | Dónde |
|---|---|---|
| B1 · Volumen y continuidad dependían de la ventana | Ventana principal: enero–agosto del 3.er año (2022 vs 2026). Los 17 meses quedan como sensibilidad. Cada métrica lleva un dictamen de robustez | 04, 06 |
| B2 · Honorarios atribuidos al gobierno | Serie semestral en pesos constantes, con tramos antes, durante y después del cambio de gobierno. El contraste A vs J queda `NO_PUBLICABLE` | 04, 06 |
| B3 · Empresas "Por revisar" (S.A.S. con puntos) | Razón social sin puntuación, patrón de NIT empresarial y personas naturales con NIT | 02 |
| B4 · Concejo atribuido al alcalde | Concejo = no atribuible; categoría propia en los solapes | 01, 05 |
| B5 · Rótulos de periodo falsos en el 07 | Rótulos tomados de las fechas reales; control que bloquea los rótulos de la v1 | 06, 07 |
| B6 · Ley de Garantías | Conteo de contratación directa en los periodos de restricción, con fuentes en `datos/referencias/ley_garantias_periodos.csv` | 05, 06 |
| Subtipo "ambiguo" con profesión explícita | Desempate por la profesión u oficio nombrado en el objeto (Decreto 1082 de 2015); concordancia con la etiqueta literal del 98 % | 03 |
| B7 · Clasificador sin validar | Plantilla `datos/referencias/03_revision_manual_cps.csv`; % de ambiguos por año y estado de validación heredado | 03, 04, 06 |
| Solapes por terminación anticipada | Pares con contrato `terminado` separados de los robustos | 05 |
| Duplicados exactos | Se marcan; el secundario no es válido | 02 |
| Días perdidos por convención exclusiva | Duración inclusiva e intervalos `[inicio, fin+1)` | 02 |
| ¿Sumar días adicionados? | Prueba empírica: la fecha final ya los incluye, así que no se suman | 02 |
| Bootstrap con falsa precisión | Eliminado | 04 |
| Nombres en productos públicos | Solo en `uso_interno_verificacion/`; control de nombres y documentos en el 07 | 05, 07 |
| Cuaderno 07 pobre analíticamente | Reescrito (v3): pulso diario de contratistas, calendario de firmas, Ley de Garantías 2022/2023/2026, transición de gobierno, rotación, duración, prórrogas, honorarios y reparto, dependencias, obra y convenios, otras entidades, calidad de datos | 07 |
| Rutas no portables | Rutas relativas con `/`; lectura de punteros con `\` heredados | utils |

## Tareas pendientes (no se pueden automatizar sin datos externos)

1. **Validación del subtipo:** diligenciar `datos/referencias/03_revision_manual_cps.csv` y re-ejecutar desde el 03.
2. **Cobertura de 2021 y otras entidades:** el 01 lo consulta automáticamente si hay internet (`VERIFICAR_COBERTURA_EXTERNA = True`). El resultado queda en `datos/salidas/01_base/verificaciones_externas.csv`.
3. **Expedientes:** Q07 a Q09 y Q11 son `SOLO_INVESTIGACION`. Las listas con nombres y URL están en `datos/salidas/05_patrones/uso_interno_verificacion/` y `datos/salidas/06_hallazgos/q07_extremos_para_verificar.csv`.

## Productos del 07

- `datos/salidas/07_historia/historia_ciudadana.html`: la historia completa en un solo archivo para compartir (gráficas incrustadas).
- `datos/salidas/07_historia/historia_ciudadana.md`: la misma historia con gráficas enlazadas (`graficos/`).
- `datos/salidas/07_historia/insights_ciudadanos.csv`: las 26 preguntas con respuesta, nivel de evidencia, estado, universo, límite y tabla de soporte.
- `datos/salidas/07_historia/tablas/`: una tabla por pregunta, la prueba de estrés, el embudo del dato, las decisiones metodológicas y el retrato compuesto; sin nombres ni documentos.
- `datos/salidas/07_historia/uso_interno_verificacion/`: listas con proveedores y enlaces para verificar (no publicar).
- `datos/referencias/restricciones_electorales.csv` y `datos/referencias/salario_minimo.csv`: referencias externas con su fuente (se crean si no existen; editables).

## Qué es público y qué no

- **Público:** `datos/salidas/07_historia/historia_ciudadana.html` (o `.md` con `graficos/`), `07_historia/tablas/`, `07_historia/insights_ciudadanos.csv` y el catálogo del 06.
- **Trabajo interno (no publicar):** las etapas 01 a 05 y todas las carpetas `uso_interno_verificacion/`, que contienen ids de contrato, URLs de SECOP y nombres.
- **Dictamen metodológico final:** `docs/DICTAMEN_METODOLOGICO.md`.
