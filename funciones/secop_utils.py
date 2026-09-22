"""Utilidades comunes del proyecto SECOP II Barrancabermeja (versión 2)."""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

VERSION_PIPELINE = "2.0.0"
NIT_ALCALDIA = "890201900"
NIT_ESE = "829001846"
ADMINS = ["Alfonso Eljach", "Jonathan Vásquez"]
COLORES = {"Alfonso Eljach": "#2a78d6", "Jonathan Vásquez": "#eb6834", "neutro": "#7a7a74"}

# Columnas con tipo conocido al leer CSV intermedios
FECHAS = [
    "fecha_firma", "fecha_inicio", "fecha_fin", "fecha_referencia", "inicio", "fin_excl", "mes", "mes_firma",
]
NUMERICAS = [
    "valor_contrato", "valor_pagado", "dias_adicionados", "duracion_dias_excl",
    "duracion_dias_incl", "meses_equivalentes", "valor_mensual_equiv",
    "valor_mensual_equiv_real", "ipc_indice", "factor_ipc", "valor_contrato_real",
]
PREFIJOS_BOOL = ("es_", "flag_", "apto_", "en_")
TEXTO_PROTEGIDO = ("documento", "nit", "id_contrato", "proceso", "codigo", "id_par")  # identificadores: siempre texto


# ---------- rutas ----------
def ruta_proyecto() -> Path:
    """Sube desde el directorio actual hasta encontrar la carpeta 'datos'."""
    actual = Path.cwd().resolve()
    for candidata in [actual, *actual.parents]:
        if (candidata / "datos").is_dir() and (candidata / "notebooks").is_dir():
            return candidata
    raise FileNotFoundError("No se encontró la raíz del proyecto (carpetas datos/ y notebooks/).")


def rel(ruta: Path, raiz: Path) -> str:
    """Ruta relativa portable (siempre con '/')."""
    return Path(ruta).resolve().relative_to(raiz).as_posix()


def abs_desde_rel(texto: str, raiz: Path) -> Path:
    """Convierte una ruta relativa (acepta '\\' heredados) en absoluta dentro del proyecto."""
    destino = (raiz / Path(*re.split(r"[\\/]+", str(texto)))).resolve()
    if raiz not in destino.parents and destino != raiz:
        raise RuntimeError(f"Ruta fuera del proyecto: {texto}")
    return destino


# ---------- hashes y json ----------
def sha256_archivo(ruta: Path, bloque: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with Path(ruta).open("rb") as f:
        for trozo in iter(lambda: f.read(bloque), b""):
            h.update(trozo)
    return h.hexdigest()


def sha_texto(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def escribir_json(ruta: Path, contenido) -> None:
    Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(ruta).with_suffix(".tmp")
    tmp.write_text(json.dumps(contenido, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    tmp.replace(ruta)


def leer_json(ruta: Path):
    return json.loads(Path(ruta).read_text(encoding="utf-8"))


# ---------- escritura y lectura tabular ----------
def guardar_csv(df: pd.DataFrame, ruta: Path) -> Path:
    """CSV determinista: mismo contenido -> mismo hash."""
    Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    salida = df.copy()
    for c in salida.columns:
        if pd.api.types.is_datetime64_any_dtype(salida[c]):
            salida[c] = salida[c].dt.strftime("%Y-%m-%d")
    salida.to_csv(ruta, index=False, encoding="utf-8-sig", float_format="%.6f", lineterminator="\n")
    return Path(ruta)


def leer_csv(ruta: Path) -> pd.DataFrame:
    """Lee con tipos: fechas, números y banderas booleanas estrictas."""
    df = pd.read_csv(ruta, dtype=str, keep_default_na=True, encoding="utf-8-sig", low_memory=False)
    for c in df.columns:
        if c in FECHAS or c.startswith("fecha_") or c.startswith("inicio_") or c.startswith("fin_"):
            convertida = pd.to_datetime(df[c], errors="coerce", format="%Y-%m-%d")
            if (df[c].notna() & convertida.isna()).any():
                raise ValueError(f"Fechas no interpretables en {c}")
            df[c] = convertida
        elif c in NUMERICAS or c.startswith(("n_", "valor_", "dias_", "meses_", "pct_", "mediana_", "p25_", "p75_")):
            convertida = pd.to_numeric(df[c], errors="coerce")
            if (df[c].notna() & convertida.isna()).any():
                continue  # columna textual con prefijo numérico: se deja como texto
            df[c] = convertida
        elif set(df[c].dropna().unique()) <= {"True", "False"} and df[c].notna().any():
            if df[c].isna().any():
                raise ValueError(f"Bandera con nulos: {c}")
            df[c] = df[c].eq("True")
        elif not any(t in c for t in TEXTO_PROTEGIDO):
            convertida = pd.to_numeric(df[c], errors="coerce")
            if df[c].notna().any() and not (df[c].notna() & convertida.isna()).any():
                df[c] = convertida  # columna enteramente numérica
    return df


# ---------- manifiestos y punteros ----------
def carpeta_etapa(raiz: Path, etapa: str) -> Path:
    ruta = raiz / "datos" / "salidas" / etapa
    ruta.mkdir(parents=True, exist_ok=True)
    return ruta


def cerrar_etapa(raiz: Path, etapa: str, version_nb: str, entradas: dict, salidas: dict,
                 reglas: dict, conteos: dict, estado: str, alertas: list | None = None) -> dict:
    """Escribe manifiesto (hashes) y puntero de la etapa."""
    manifiesto = {
        "etapa": etapa,
        "version_notebook": version_nb,
        "version_pipeline": VERSION_PIPELINE,
        "estado": estado,
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "entorno": {"pandas": pd.__version__, "numpy": np.__version__},
        "entradas": entradas,
        "reglas": reglas,
        "conteos": conteos,
        "alertas": alertas or [],
        "salidas": {k: {"ruta": rel(v, raiz), "sha256": sha256_archivo(v)} for k, v in salidas.items()},
    }
    ruta_man = carpeta_etapa(raiz, etapa) / "manifiesto.json"
    escribir_json(ruta_man, manifiesto)
    puntero = {"etapa": etapa, "estado": estado, "manifiesto": rel(ruta_man, raiz),
               "sha256_manifiesto": sha256_archivo(ruta_man)}
    escribir_json(raiz / "datos" / "salidas" / "punteros" / f"{etapa}.json", puntero)
    return manifiesto


def abrir_etapa(raiz: Path, etapa: str) -> tuple[dict, dict]:
    """Verifica puntero, manifiesto y hash de cada salida. Devuelve (manifiesto, rutas)."""
    ruta_p = raiz / "datos" / "salidas" / "punteros" / f"{etapa}.json"
    if not ruta_p.exists():
        raise FileNotFoundError(f"Ejecute primero la etapa {etapa}.")
    puntero = leer_json(ruta_p)
    ruta_m = abs_desde_rel(puntero["manifiesto"], raiz)
    if sha256_archivo(ruta_m) != puntero["sha256_manifiesto"]:
        raise RuntimeError(f"El manifiesto {etapa} cambió después de crear el puntero.")
    man = leer_json(ruta_m)
    if man["estado"].startswith("BLOQUEADO"):
        raise RuntimeError(f"La etapa {etapa} quedó bloqueada: {man['alertas']}")
    rutas = {}
    for nombre, info in man["salidas"].items():
        ruta = abs_desde_rel(info["ruta"], raiz)
        if sha256_archivo(ruta) != info["sha256"]:
            raise RuntimeError(f"Cambió el archivo {nombre} de la etapa {etapa}. Re-ejecute la etapa.")
        rutas[nombre] = ruta
    return man, rutas


def huella_entrada(man: dict) -> dict:
    return {"etapa": man["etapa"], "version": man["version_notebook"],
            "sha256_salidas": {k: v["sha256"] for k, v in man["salidas"].items()}}


# ---------- controles ----------
class Controles:
    """Acumula controles; los críticos fallidos bloquean la etapa."""

    def __init__(self):
        self.filas = []

    def agregar(self, prueba, resultado, esperado, severidad="Crítica", pasa=None):
        if pasa is None:
            pasa = resultado == esperado
        self.filas.append({"prueba": prueba, "resultado": str(resultado), "esperado": str(esperado),
                           "severidad": severidad, "pasa": bool(pasa)})

    def tabla(self) -> pd.DataFrame:
        return pd.DataFrame(self.filas)

    def bloqueos(self) -> list:
        t = self.tabla()
        return t.loc[(~t["pasa"]) & t["severidad"].eq("Crítica"), "prueba"].tolist()

    def alertas(self) -> list:
        t = self.tabla()
        return t.loc[(~t["pasa"]) & ~t["severidad"].eq("Crítica"), "prueba"].tolist()


# ---------- texto e identidad ----------
def normalizar_texto(serie: pd.Series) -> pd.Series:
    def _n(v):
        if pd.isna(v):
            return pd.NA
        t = unicodedata.normalize("NFKD", str(v).strip().lower())
        t = "".join(ch for ch in t if not unicodedata.combining(ch))
        t = re.sub(r"\s+", " ", t)
        return t or pd.NA
    return serie.map(_n).astype("string")


def sin_puntuacion(serie: pd.Series) -> pd.Series:
    """'s.a.s.' -> 's a s'; permite detectar razones sociales con puntos."""
    t = serie.fillna("").str.replace(r"[^a-z0-9ñ ]", " ", regex=True)
    return t.str.replace(r"\s+", " ", regex=True).str.strip()


def normalizar_documento(serie: pd.Series) -> pd.Series:
    t = serie.astype("string").str.upper().str.strip().str.replace(r"[^A-Z0-9]", "", regex=True)
    return t.mask(t.eq(""), pd.NA)


def extraer_url(valor):
    if valor is None or (not isinstance(valor, (dict, list)) and pd.isna(valor)):
        return pd.NA
    if isinstance(valor, dict):
        valor = valor.get("url") or ""
    m = re.search(r"https?://[^\s'\"}>,]+", str(valor))
    return m.group(0) if m else pd.NA


# ---------- intervalos ----------
def unir_intervalos(intervalos) -> list:
    """Intervalos semiabiertos [inicio, fin); une solapes y adyacencias."""
    orden = sorted((i, f) for i, f in intervalos if pd.notna(i) and pd.notna(f) and i < f)
    unidos = []
    for i, f in orden:
        if unidos and i <= unidos[-1][1]:
            unidos[-1][1] = max(unidos[-1][1], f)
        else:
            unidos.append([i, f])
    return unidos


def dias_cubiertos(intervalos) -> int:
    return int(sum((f - i).days for i, f in unir_intervalos(intervalos)))


def cobertura_por_persona(df: pd.DataFrame, inicio, fin_excl, col_doc="documento_identidad") -> pd.DataFrame:
    """Días únicos cubiertos por persona dentro de [inicio, fin_excl)."""
    inicio, fin_excl = pd.Timestamp(inicio), pd.Timestamp(fin_excl)
    d = df.loc[df["fecha_inicio"].lt(fin_excl) & df["fin_excl"].gt(inicio)].copy()
    d["i"] = d["fecha_inicio"].clip(lower=inicio)
    d["f"] = d["fin_excl"].clip(upper=fin_excl)
    filas = []
    for doc, g in d.groupby(col_doc, sort=True):
        dias = dias_cubiertos(zip(g["i"], g["f"]))
        if dias > 0:
            filas.append({col_doc: doc, "dias_cubiertos": dias, "meses_cubiertos": dias / 30.4375,
                          "contratos": g["id_contrato"].nunique()})
    return pd.DataFrame(filas, columns=[col_doc, "dias_cubiertos", "meses_cubiertos", "contratos"])


def mediana(serie) -> float:
    s = pd.to_numeric(pd.Series(serie), errors="coerce").dropna()
    return float(s.median()) if len(s) else np.nan


def cuantil(serie, q) -> float:
    s = pd.to_numeric(pd.Series(serie), errors="coerce").dropna()
    return float(s.quantile(q)) if len(s) else np.nan


def cambio_pct(a, b) -> float:
    return 100 * (b / a - 1) if pd.notna(a) and pd.notna(b) and a else np.nan
