# ¿Cómo contrata la Alcaldía de Barrancabermeja?

Análisis reproducible de los contratos publicados en **SECOP II** por las nueve entidades del Distrito de Barrancabermeja,
con foco en los **contratos de prestación de servicios (CPS)** con personas naturales de la Alcaldía central (NIT 890201900).

Cubre el final del gobierno de Alfonso Eljach (abril de 2021 a diciembre de 2023) y el de Jonathan Vásquez (enero de 2024 al corte).
El producto final es una historia ciudadana con 26 preguntas respondidas, cada una con su tabla, su gráfica, su nivel de evidencia
y lo que **no** significa.

- **Historia lista para leer:** (un solo archivo, con las gráficas dentro).
- **Metodología y decisiones:** [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md).
- **Dictamen metodológico y límites:** [`docs/DICTAMEN_METODOLOGICO.md`](docs/DICTAMEN_METODOLOGICO.md).

## Estructura

```
notebooks/            Los siete cuadernos, en orden de ejecución
funciones/            secop_utils.py: utilidades compartidas
datos/
  brutos/             Descarga congelada de SECOP II (no se versiona; ~100 MB)
  referencias/        IPC del DANE, catálogo de entidades, Ley de Garantías, salario mínimo, revisión manual
  salidas/            Resultados de cada etapa (no se versionan; se regeneran al ejecutar)
publicacion/          Paquete público: historia, gráficas y tablas sin nombres ni documentos
docs/                 Metodología y dictamen
```

## Cómo reproducirlo

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows;  en Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

Abrir los cuadernos de `notebooks/` en VS Code o Jupyter y ejecutarlos **en orden con Restart & Run All**:

| # | Cuaderno | Qué hace |
|---|---|---|
| 01 | `01_BASE_SECOP_II.ipynb` | Congela la descarga, verifica su huella sha256 y arma el catálogo de entidades. |
| 02 | `02_CALIDAD_IDENTIDAD.ipynb` | Identidad del proveedor, duplicados, fechas y duración inclusiva. |
| 03 | `03_CPS_PERSONAS.ipynb` | Define el universo CPS y el subtipo profesional / apoyo a la gestión. |
| 04 | `04_COMPARABILIDAD.ipynb` | Pesos constantes con el IPC, ventanas comparables y dictamen de robustez. |
| 05 | `05_TRAYECTORIAS_SIMULTANEIDAD.ipynb` | Episodios por persona, recurrencia, Ley de Garantías y proveedores. |
| 06 | `06_HALLAZGOS_CIUDADANOS.ipynb` | Catálogo de hallazgos con su estado de publicación. |
| 07 | `07_HISTORIA_CIUDADANA.ipynb` | La historia ciudadana, la prueba de estrés y el paquete de `publicacion/`. |

Cada etapa verifica las huellas de la anterior y escribe un manifiesto con las suyas. Dos ejecuciones completas producen
datos, tablas y gráficas idénticos byte a byte.

## Reglas del análisis

- La Alcaldía se identifica por su NIT; el Concejo, la Personería, la Contraloría y el Hospital Regional **no** se le suman.
- Cada persona es su número de documento, nunca su nombre. **Ningún producto público lleva nombres ni documentos.**
- Nada se imputa. Los valores extremos no se borran: se marcan.
- El valor mensual equivalente **no es un salario**.
- Cada hallazgo dice si es dato descriptivo, patrón o anomalía que requiere documentos, y qué no significa.
- Lo que cambia según la ventana se publica como rango; lo que solo un expediente puede explicar se publica como pregunta.

## Fuentes

- [SECOP II · Contratos electrónicos (datos.gov.co, `jbjy-vk9h`)](https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Contratos-Electr-nicos/jbjy-vk9h)
- [DANE · Índice de precios al consumidor](https://www.dane.gov.co/index.php/estadisticas-por-tema/precios-y-inflacion/indice-de-precios-al-consumidor-ipc)
- Ley 996 de 2005 (Ley de Garantías) y [Circular 006 de Colombia Compra Eficiente](https://www.colombiacompra.gov.co/wp-content/uploads/2025/10/Circular-006-ABC-de-Ley-de-Garantias-Dig.pdf)

Los datos son públicos. El análisis, el código y los textos de este repositorio son de autoría propia.
