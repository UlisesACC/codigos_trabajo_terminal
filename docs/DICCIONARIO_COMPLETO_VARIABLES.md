# Diccionario completo de variables de los Parquet WNBA

**Este documento se genera desde los archivos binarios .parquet, NO desde los archivos .md de descripcion.**

El codigo incluido abajo inspecciona directamente todos los esquemas de datos_a_usar/wnba_stats/, separa familias por carpeta y nombre exacto sin anio y actualiza este MISMO Markdown.

**Estado:** pendiente de ejecutar la inspeccion local. No se presentan columnas como verificadas hasta leer los archivos fisicos.

## Ejecutar desde Git Bash en la raiz de codigos_trabajo_terminal

Primero instala pyarrow:

    python -m pip install pyarrow

Despues ejecuta este comando para actualizar unicamente este archivo:

    python -c "from pathlib import Path; p=Path('docs/DICCIONARIO_COMPLETO_VARIABLES.md'); s=p.read_text(encoding='utf-8'); exec(s.split('<!-- INICIO_SCRIPT -->')[1].split('<!-- FIN_SCRIPT -->')[0])"

El documento resultante contiene todas las columnas de cada familia, tipos fisicos, significado cuando puede sustentarse, archivos exactos y cantidad de filas. Si una variable no tiene descripcion validada se indica explicitamente.

## Codigo generador integrado

<!-- INICIO_SCRIPT -->
from pathlib import Path
from collections import defaultdict
import re
import sys

try:
    import pyarrow.parquet as pq
except ImportError:
    sys.exit("Instala pyarrow: python -m pip install pyarrow")

root = Path.cwd()
file = root / "docs" / "DICCIONARIO_COMPLETO_VARIABLES.md"
folder = root / "datos_a_usar" / "wnba_stats"
if not folder.is_dir() or not file.exists():
    sys.exit("Ejecutar desde la raiz del repositorio codigos_trabajo_terminal.")

meaning = {
    "game_id":"Identificador del partido",
    "team_id":"Identificador del equipo",
    "player_id":"Identificador de jugadora",
    "person_id":"Identificador de la persona en la jugada (no siempre una jugadora)",
    "season":"Anio de la temporada",
    "season_type":"Tipo de temporada, segun dataset",
    "game_date":"Fecha del partido",
    "action_number":"Numero secuencial de accion en el partido",
    "period":"Periodo del partido",
    "clock":"Reloj del partido en el instante del evento",
    "action_type":"Tipo general de evento",
    "sub_type":"Subtipo de evento",
    "description":"Descripcion textual de la accion",
    "team_name":"Nombre del equipo",
    "team_abbreviation":"Abreviatura del equipo",
    "player_name":"Nombre de jugadora",
    "group_id":"Identificador del grupo o alineacion",
    "group_name":"Nombre del grupo o alineacion",
    "gp":"Partidos disputados",
    "w":"Victorias",
    "l":"Derrotas",
    "pts":"Puntos anotados",
    "points":"Puntos anotados",
    "ast":"Asistencias",
    "assists":"Asistencias",
    "reb":"Rebotes totales",
    "rebounds_total":"Rebotes totales",
    "oreb":"Rebotes ofensivos",
    "dreb":"Rebotes defensivos",
    "stl":"Robos de balon",
    "blk":"Bloqueos",
    "tov":"Perdidas de balon",
    "turnovers":"Perdidas de balon",
    "fgm":"Tiros de campo encestados",
    "fga":"Tiros de campo intentados",
    "fg_pct":"Proporcion de tiros de campo convertidos",
    "fg3m":"Triples encestados",
    "fg3a":"Triples intentados",
    "fg3_pct":"Proporcion de triples encestados",
    "ftm":"Tiros libres encestados",
    "fta":"Tiros libres intentados",
    "ft_pct":"Proporcion de tiros libres encestados",
    "off_rating":"Indicador de eficiencia ofensiva",
    "def_rating":"Indicador de eficiencia defensiva",
    "net_rating":"Diferencia de eficiencia ofensiva y defensiva",
    "poss":"Numero de posesiones",
    "usg_pct":"Proporcion de uso ofensivo",
    "ts_pct":"Porcentaje de tiro verdadero",
    "efg_pct":"Porcentaje efectivo de tiro de campo",
    "shot_result":"Resultado del intento de tiro",
    "shot_distance":"Distancia del tiro (pies)",
    "shot_value":"Valor del tiro en puntos",
    "x_legacy":"Coordenada horizontal del tiro",
    "y_legacy":"Coordenada vertical del tiro",
}
def note(col):
    if col in meaning:
        return meaning[col]
    if col.endswith("_rank") and col[:-5] in meaning:
        return "Posicion en clasificacion de: " + meaning[col[:-5]].lower()
    return "Significado no verificado; campo detectado en el Parquet."
def clean(value):
    return str(value).replace("|", "/").replace("\n", " ")
family=defaultdict(list)
bad=[]
allfiles=sorted(folder.rglob("*.parquet"))
for p in allfiles:
    relative=p.relative_to(folder)
    match=re.fullmatch(r"(.+)_((?:19|20)\d{2})\.parquet",p.name)
    key=(relative.parent.as_posix(),match.group(1) if match else p.stem)
    try:
        obj=pq.ParquetFile(p)
        cols={f.name:str(f.type) for f in obj.schema_arrow}
        family[key].append((p,obj.metadata.num_rows,cols))
    except Exception as e:
        bad.append((p,str(e)))
lines=["## Diccionario construido desde archivos Parquet","",
       f"Archivos encontrados: {len(allfiles)}. Familias: {len(family)}. Errores: {len(bad)}.","",
       "Los tipos y nombres provienen del esquema fisico de TODOS los archivos de cada familia.",
       "Las descripciones que no se hayan verificado se distinguen expresamente.",""]
counter=0
for (group,name),items in sorted(family.items()):
    cols=defaultdict(list)
    for p,rows,schema in items:
        for c,t in schema.items(): cols[c].append(t)
    counter+=len(cols)
    lines+=["### "+group+"/"+name,"",
            "Archivos: "+str(len(items))+"; filas totales: "+str(sum(r for p,r,c in items))+".",
            "", "**Archivos de origen:**",""]
    lines += ["- "+p.relative_to(root).as_posix()+" ("+str(rows)+" filas)" for p,rows,c in items]
    lines += ["","| Variable | Tipo(s) real(es) | Descripcion | Archivos que la incluyen |",
              "|---|---|---|---|"]
    for c,types in sorted(cols.items()):
        lines.append("| "+clean(c)+" | "+", ".join(sorted(set(types)))+" | "+clean(note(c))+" | "+str(len(types))+"/"+str(len(items))+" |")
    lines.append("")
if bad:
    lines+=["## Archivos con errores de lectura",""]
    lines+=["- "+p.relative_to(root).as_posix()+": "+clean(reason) for p,reason in bad]
lines+=["## Totales","",f"Variables por familia: {counter}. Archivos analizados correctamente: {len(allfiles)-len(bad)}.",""]
start="<!-- INICIO_DATOS_GENERADOS -->"
end="<!-- FIN_DATOS_GENERADOS -->"
original=file.read_text(encoding="utf-8")
if start not in original or end not in original:
    sys.exit("Faltan marcadores del diccionario.")
left,right=original.split(start,1)
_,after=right.split(end,1)
file.write_text(left+start+"\n\n"+"\n".join(lines)+"\n"+end+after,encoding="utf-8")
print("Diccionario actualizado:",len(allfiles)-len(bad),"Parquet,",len(family),"familias,",counter,"columnas por familia.")

<!-- FIN_SCRIPT -->

<!-- INICIO_DATOS_GENERADOS -->

Pendiente de inspeccion de archivos Parquet en la computadora local.

<!-- FIN_DATOS_GENERADOS -->
