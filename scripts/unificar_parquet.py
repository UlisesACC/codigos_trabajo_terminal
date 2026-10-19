#!/usr/bin/env python3
"""Une los archivos Parquet con igual nombre base y distinto año.

Ejemplo: lineups_advanced_2024.parquet + lineups_advanced_2025.parquet
         -> datos_globales/leaguedash/lineups_advanced_global.parquet
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("Instala las dependencias: python -m pip install pandas pyarrow")

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "datos_a_usar" / "wnba_stats"
DESTINO = RAIZ / "datos_globales"
PATRON = re.compile(r"^(?P<nombre>.+)_(?P<anio>(?:19|20)\d{2})\.parquet$", re.IGNORECASE)


def descubrir(categoria: str | None, desde: int | None, hasta: int | None):
    grupos = defaultdict(list)
    omitidos = []
    for ruta in sorted(ORIGEN.rglob("*.parquet")):
        # Las carpetas y los nombres base forman conjuntamente la identidad.
        relativo = ruta.parent.relative_to(ORIGEN)
        if categoria and (not relativo.parts or relativo.parts[0] != categoria):
            continue
        m = PATRON.fullmatch(ruta.name)
        if not m:
            omitidos.append(ruta.relative_to(RAIZ))
            continue
        anio = int(m["anio"])
        if (desde is not None and anio < desde) or (hasta is not None and anio > hasta):
            continue
        grupos[(relativo, m["nombre"])].append((anio, ruta))
    return grupos, omitidos


def unir(carpeta: Path, nombre: str, entradas: list[tuple[int, Path]], sobrescribir: bool):
    salida = DESTINO / carpeta / f"{nombre}_global.parquet"
    if salida.exists() and not sobrescribir:
        print(f"[EXISTENTE] {salida.relative_to(RAIZ)}; usa --sobrescribir para regenerar")
        return "existente"

    tablas = []
    conjuntos_columnas = []
    for anio, origen in sorted(entradas):
        tabla = pd.read_parquet(origen, engine="pyarrow")
        if "anio" in tabla.columns:
            # Si ya existe anio, verificar en vez de descartar información.
            valores = set(pd.to_numeric(tabla["anio"], errors="coerce").dropna().astype(int))
            if valores and valores != {anio}:
                raise ValueError(f"'anio' no coincide con el nombre en {origen}")
            tabla["anio"] = anio
        else:
            tabla.insert(0, "anio", anio)
        conjuntos_columnas.append(set(tabla.columns))
        tablas.append(tabla)
    if len({frozenset(cols) for cols in conjuntos_columnas}) > 1:
        print("  [AVISO] Diferencias de columnas entre años; las ausentes quedarán nulas.")

    tabla_global = pd.concat(tablas, ignore_index=True, sort=False)
    tabla_global["anio"] = tabla_global["anio"].astype("int32")
    salida.parent.mkdir(parents=True, exist_ok=True)
    temporal = salida.with_name(salida.name + ".tmp")
    try:
        tabla_global.to_parquet(temporal, engine="pyarrow", compression="snappy", index=False)
        temporal.replace(salida)
    finally:
        temporal.unlink(missing_ok=True)
    print(f"[OK] {salida.relative_to(RAIZ)} | {len(entradas)} archivos | {len(tabla_global):,} filas")
    return "creado"


def main():
    p = argparse.ArgumentParser(description="Unifica Parquet anuales por carpeta y nombre exacto sin año.")
    p.add_argument("--categoria", help="Ejemplo: leaguedash, player_impact, shots")
    p.add_argument("--desde", type=int, help="Primer año, incluido")
    p.add_argument("--hasta", type=int, help="Último año, incluido")
    p.add_argument("--sobrescribir", action="store_true", help="Reemplaza globales ya generados")
    p.add_argument("--solo-multiples", action="store_true", help="Excluye familias con un único archivo anual")
    p.add_argument("--listar", action="store_true", help="Muestra agrupaciones, sin leer ni escribir Parquet")
    args = p.parse_args()
    if not ORIGEN.is_dir():
        p.error(f"No existe la carpeta: {ORIGEN}")
    if args.desde is not None and args.hasta is not None and args.desde > args.hasta:
        p.error("--desde debe ser menor o igual a --hasta")

    grupos, omitidos = descubrir(args.categoria, args.desde, args.hasta)
    trabajos = [(carpeta, nombre, entradas) for (carpeta, nombre), entradas in sorted(grupos.items())
                if not args.solo_multiples or len(entradas) > 1]
    print(f"Familias encontradas: {len(trabajos)}")
    print(f"Parquet sin año al final (no combinados): {len(omitidos)}")
    for ruta in omitidos:
        print(f"[SIN AÑO] {ruta}")
    if args.listar:
        for carpeta, nombre, entradas in trabajos:
            años = sorted(a for a, _ in entradas)
            print(f"{carpeta}/{nombre}: {len(entradas)} archivos ({min(años)}–{max(años)})")
        return

    fallos = []
    contador = 0
    for carpeta, nombre, entradas in trabajos:
        try:
            estado = unir(carpeta, nombre, entradas, args.sobrescribir)
            if estado == "creado":
                contador += 1
        except (OSError, ValueError, TypeError, ImportError) as exc:
            detalle = f"{carpeta}/{nombre}: {type(exc).__name__}: {exc}"
            fallos.append(detalle)
            print(f"[ERROR] {detalle}", file=sys.stderr)
    print(f"\nGlobales generados: {contador}; errores: {len(fallos)}")
    if fallos:
        reporte = RAIZ / "errores_unificacion.txt"
        reporte.write_text("\n".join(fallos) + "\n", encoding="utf-8")
        print(f"Consulta {reporte}")
        sys.exit(1)


if __name__ == "__main__":
    main()
