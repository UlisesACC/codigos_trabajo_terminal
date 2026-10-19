# Unificar Parquet por nombre y temporada

El script `scripts/unificar_parquet.py` recorre `datos_a_usar/wnba_stats/**` y agrupa únicamente los archivos de la **misma carpeta y el mismo nombre sin el sufijo `_AAAA.parquet`**.

Ejemplos: `lineups_advanced_2024.parquet` + `lineups_advanced_2025.parquet` producen `datos_globales/leaguedash/parquet/lineups_advanced_global.parquet`; `lineups_opponent` produce otro archivo, nunca se mezcla con `advanced`. Se añade `anio` como columna entera y se conservan las demás.

## Instalación

```bash
python -m pip install pandas pyarrow
```

## Uso desde la raíz del repositorio

Primero puedes listar los grupos encontrados sin procesar datos:

```bash
python scripts/unificar_parquet.py --listar
```

Generar todas las familias:

```bash
python scripts/unificar_parquet.py
```

Solo player_impact:

```bash
python scripts/unificar_parquet.py --categoria player_impact
```

Solo leaguedash entre 2024 y 2026:

```bash
python scripts/unificar_parquet.py --categoria leaguedash --desde 2024 --hasta 2026
```

Volver a crear resultados existentes:

```bash
python scripts/unificar_parquet.py --sobrescribir
```

Generar únicamente familias con dos o más archivos:

```bash
python scripts/unificar_parquet.py --solo-multiples
```

Los archivos de origen no se modifican. Los globales se guardan en `datos_globales/` preservando su carpeta relativa. Esta salida está ignorada por Git porque puede resultar pesada. Los archivos que no tienen sufijo de año se muestran como `[SIN AÑO]` y no se incorporan a ninguna familia. Si falla alguna familia se registra en `errores_unificacion.txt` y el programa continúa con las restantes.
