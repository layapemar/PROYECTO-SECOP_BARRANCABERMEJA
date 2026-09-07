import os
from pathlib import Path


EMOJI_CONTROL = "👾"


def crear_estructura():

    # ============================================================
    # RUTA BASE DEL PROYECTO
    # ============================================================

    base = Path(__file__).resolve().parent

    print(
        f"\n{EMOJI_CONTROL} Iniciando estructura del proyecto "
        "Contratación Pública Barrancabermeja\n"
    )


    # ============================================================
    # CARPETAS DEL PROYECTO
    # ============================================================

    carpetas = [

        # DATOS
        "datos/brutos/secop_ii",
        "datos/intermedios",
        "datos/procesados",

        # NOTEBOOKS
        "notebooks",

        # FUNCIONES REUTILIZABLES
        "funciones",

        # CONFIGURACIONES
        "config",

        # DOCUMENTACIÓN
        "docs",

        # ENTREGABLES
        "entregables/graficos",
        "entregables/tablas",
        "entregables/informes",
        "entregables/dashboards",

        # GITHUB / COPILOT
        ".github",
    ]


    for carpeta in carpetas:

        ruta = base / carpeta

        ruta.mkdir(
            parents=True,
            exist_ok=True
        )

        print(
            f"{EMOJI_CONTROL} Creada: {ruta}"
        )


    # ============================================================
    # ARCHIVO .gitignore
    # ============================================================

    gitignore_path = base / ".gitignore"


    if not gitignore_path.exists():

        gitignore_content = """# ============================================================
# SISTEMA
# ============================================================

desktop.ini
Thumbs.db
.DS_Store


# ============================================================
# ENTORNOS PYTHON
# ============================================================

.env
.venv/
venv/
env/

__pycache__/
*.py[cod]


# ============================================================
# JUPYTER
# ============================================================

.ipynb_checkpoints/


# ============================================================
# DATOS
# ============================================================

datos/

*.csv
*.xlsx
*.xls
*.parquet
*.feather

*.db
*.sqlite
*.duckdb


# ============================================================
# ENTREGABLES PESADOS
# ============================================================

entregables/


# ============================================================
# LOGS
# ============================================================

*.log


# ============================================================
# IDE
# ============================================================

.vscode/
.idea/
"""

        gitignore_path.write_text(
            gitignore_content,
            encoding="utf-8"
        )

        print(
            f"{EMOJI_CONTROL} Creado: {gitignore_path}"
        )

    else:

        print(
            f"{EMOJI_CONTROL} Ya existe: {gitignore_path}"
        )


    # ============================================================
    # INSTRUCCIONES PARA GITHUB COPILOT
    # ============================================================

    copilot_path = (
        base
        / ".github"
        / "copilot-instructions.md"
    )


    if not copilot_path.exists():

        copilot_content = """# INSTRUCCIONES DEL PROYECTO

- Comenzarás SIEMPRE cada respuesta con el emoji 👾.

- Responderás siempre en español de Colombia.

- Este proyecto analiza contratación pública de la Alcaldía Distrital de Barrancabermeja.

- La fuente principal será SECOP II.

- No incorporarás SECOP I salvo que se solicite explícitamente.

- Las administraciones principales del análisis son:

  - Alfonso Eljach Manrique.
  - Jonathan Vásquez Gómez.

- El foco principal de investigación será la contratación por prestación de servicios (CPS).

- Se analizarán especialmente:

  - Número de contratos CPS.
  - Número de personas naturales contratadas.
  - Duración de los contratos.
  - Valor total de los contratos.
  - Valor mensual equivalente.
  - Número de contratos por persona.
  - Contratistas recurrentes.
  - Renovaciones contractuales.
  - Personas contratadas en ambos gobiernos.
  - Contratistas que permanecen durante varios años.
  - Contratos de mayor valor.
  - Concentración de contratación.
  - Dinámicas mensuales y anuales.
  - Comportamiento durante periodos preelectorales y electorales.

- Nunca interpretarás automáticamente un patrón estadístico como corrupción, favorecimiento o irregularidad.

- Diferenciarás claramente entre:

  1. Hallazgo estadístico.
  2. Patrón que merece revisión.
  3. Evidencia documental.
  4. Interpretación periodística.

- No inventarás datos.

- Si un dato no puede comprobarse, lo señalarás expresamente.

- No mezclarás personas naturales con personas jurídicas en análisis de CPS sin indicarlo.

- Para identificar personas contratadas se priorizará el documento del proveedor sobre el nombre.

- Se deberá evitar contar varias veces el mismo contrato.

- Antes de hacer comparaciones entre administraciones se verificará que los periodos analizados sean temporalmente comparables.

- Cuando los periodos tengan diferente duración se utilizarán indicadores normalizados, por ejemplo:

  - Contratos por mes.
  - Personas contratadas por mes.
  - Valor contratado por mes.
  - CPS por persona.

- Para comparar duración contractual se utilizará principalmente la mediana y no únicamente el promedio.

- Siempre genera código para el script o notebook abierto.

- No escribas código en la ventana interactiva salvo que se solicite expresamente.

- El código deberá ser modular, legible y reproducible.

- Se priorizará pandas para manipulación inicial de datos.

- Los datos brutos nunca deberán modificarse directamente.

- Los resultados de limpieza deberán guardarse en datos/intermedios.

- Las bases finales de análisis deberán guardarse en datos/procesados.

- Los notebooks deberán ejecutarse secuencialmente y tener nombres numerados:

  01_
  02_
  03_
  04_

- No continúes con una fase avanzada si todavía no se ha validado correctamente la fase anterior.
"""

        copilot_path.write_text(
            copilot_content,
            encoding="utf-8"
        )

        print(
            f"{EMOJI_CONTROL} Creado: {copilot_path}"
        )

    else:

        print(
            f"{EMOJI_CONTROL} Ya existe: {copilot_path}"
        )


    # ============================================================
    # MENSAJE FINAL
    # ============================================================

    print("\n" + "=" * 70)

    print(
        f"{EMOJI_CONTROL} Estructura creada correctamente."
    )

    print(
        f"{EMOJI_CONTROL} Proyecto listo para comenzar el análisis SECOP II."
    )

    print("=" * 70 + "\n")


# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":

    crear_estructura()