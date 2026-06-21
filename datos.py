# ============================================================
# ECOFLOR - Módulo: datos.py
# Curso: Fundamentos de Programación - CIIN1205P
# UPN Cajamarca - 2026
# ============================================================

from datetime import datetime

ARCH_COSECHAS    = "cosechas.txt"
ARCH_INCIDENCIAS = "incidencias.txt"
VIV1 = "Vivero 1 (Sr.Francisco)"
VIV2 = "Vivero 2 (Sra.Zoila)"

# ══════════════════════════════════════════════════════════════
# LISTAS PARALELAS — COSECHAS  (30 campos en archivo)
#  [0]  fecha        [1]  vivero       [2]  bonches (total)
#  [3]  cal_a        [4]  cal_b        [5]  rosas_sueltas (siempre clase B)
#  -- Clase A — bonches: medida (sin <50cm) --
#  [6]  a50  [7]  a60  [8]  a7090
#  -- Clase A — bonches: color --
#  [9]  a_rojo  [10] a_blanco  [11] a_rosado  [12] a_amarillo
#  -- Clase B — bonches: medida (con <50cm) --
#  [13] b_men50  [14] b50  [15] b60  [16] b7090
#  -- Clase B — bonches: color --
#  [17] b_rojo  [18] b_blanco  [19] b_rosado  [20] b_amarillo
#  -- Rosas sueltas (clase B): medida (con <50cm) --
#  [21] s_men50  [22] s50  [23] s60  [24] s7090
#  -- Rosas sueltas (clase B): color --
#  [25] s_rojo  [26] s_blanco  [27] s_rosado  [28] s_amarillo
#  [29] obs
# ══════════════════════════════════════════════════════════════
fechas_c = []; viveros_c = []; bonches_c = []
cal_a_c  = []; cal_b_c   = []; rosas_sueltas_c = []
a50_c = []; a60_c = []; a7090_c = []
a_rojo_c = []; a_blanco_c = []; a_rosado_c = []; a_amarillo_c = []
b_men50_c = []; b50_c = []; b60_c = []; b7090_c = []
b_rojo_c = []; b_blanco_c = []; b_rosado_c = []; b_amarillo_c = []
s_men50_c = []; s50_c = []; s60_c = []; s7090_c = []
s_rojo_c = []; s_blanco_c = []; s_rosado_c = []; s_amarillo_c = []
obs_c = []

# ── LISTAS PARALELAS — INCIDENCIAS ───────────────────────────
fechas_i = []; viveros_i = []; tipos_i = []
detalles_i = []; impactos_i = []; obs_i = []

_LISTAS_COSECHAS = [
    fechas_c, viveros_c, bonches_c, cal_a_c, cal_b_c, rosas_sueltas_c,
    a50_c, a60_c, a7090_c, a_rojo_c, a_blanco_c, a_rosado_c, a_amarillo_c,
    b_men50_c, b50_c, b60_c, b7090_c,
    b_rojo_c, b_blanco_c, b_rosado_c, b_amarillo_c,
    s_men50_c, s50_c, s60_c, s7090_c,
    s_rojo_c, s_blanco_c, s_rosado_c, s_amarillo_c, obs_c
]


def cargar_cosechas():
    for lst in _LISTAS_COSECHAS:
        lst.clear()
    try:
        with open(ARCH_COSECHAS, "r", encoding="utf-8") as arch:
            for linea in arch:
                linea = linea.strip()
                if not linea:
                    continue
                p = linea.split(";")
                if len(p) < 29:
                    continue
                try:
                    datetime.strptime(p[0], "%d/%m/%Y")
                    if p[1] not in (VIV1, VIV2):
                        continue
                    valores = [p[0], p[1]] + [int(x) for x in p[2:29]]
                    valores.append(p[29] if len(p) > 29 else "")
                    i = 0
                    while i < len(_LISTAS_COSECHAS):
                        _LISTAS_COSECHAS[i].append(valores[i])
                        i += 1
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"  Advertencia al cargar cosechas: {e}")


def guardar_cosechas():
    try:
        with open(ARCH_COSECHAS, "w", encoding="utf-8") as arch:
            i = 0
            while i < len(fechas_c):
                campos = [str(lst[i]) for lst in _LISTAS_COSECHAS]
                arch.write(";".join(campos) + "\n")
                i += 1
        print("  ✓ Datos guardados correctamente.")
    except PermissionError:
        print("  ✗ Error: sin permiso para escribir cosechas.txt.")
    except Exception as e:
        print(f"  ✗ Error al guardar cosechas: {e}")


def cargar_incidencias():
    for lst in [fechas_i, viveros_i, tipos_i, detalles_i, impactos_i, obs_i]:
        lst.clear()
    try:
        with open(ARCH_INCIDENCIAS, "r", encoding="utf-8") as arch:
            for linea in arch:
                linea = linea.strip()
                if not linea:
                    continue
                p = linea.split(";")
                if len(p) < 5:
                    continue
                try:
                    datetime.strptime(p[0], "%d/%m/%Y")
                except ValueError:
                    continue
                if p[1] not in (VIV1, VIV2):
                    continue
                fechas_i.append(p[0]);    viveros_i.append(p[1])
                tipos_i.append(p[2]);     detalles_i.append(p[3])
                impactos_i.append(p[4]);  obs_i.append(p[5] if len(p) > 5 else "")
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"  Advertencia al cargar incidencias: {e}")


def guardar_incidencias():
    try:
        with open(ARCH_INCIDENCIAS, "w", encoding="utf-8") as arch:
            i = 0
            while i < len(fechas_i):
                linea = ";".join([
                    fechas_i[i], viveros_i[i], tipos_i[i],
                    detalles_i[i], impactos_i[i], obs_i[i]
                ])
                arch.write(linea + "\n")
                i += 1
        print("  ✓ Datos guardados correctamente.")
    except PermissionError:
        print("  ✗ Error: sin permiso para escribir incidencias.txt.")
    except Exception as e:
        print(f"  ✗ Error al guardar incidencias: {e}")
