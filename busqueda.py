# ============================================================
# ECOFLOR - Módulo: busqueda.py
# Curso: Fundamentos de Programación - CIIN1205P
# UPN Cajamarca - 2026
# ============================================================

import datos
from validaciones import ANIO_MIN, ANIO_MAX, leer_opcion, leer_entero_rango
from datetime import datetime


def elegir_vivero_registro():
    """Solo V1 o V2 — para registros individuales."""
    print("\n  Vivero:")
    print("  1 - Vivero 1 (Sr.Francisco)")
    print("  2 - Vivero 2 (Sra.Zoila)")
    op = leer_opcion("  Opción: ", ["1", "2"])
    return datos.VIV1 if op == "1" else datos.VIV2


def elegir_vivero_consulta():
    """V1, V2 o Ambos — para consultas."""
    print("\n  Vivero:")
    print("  1 - Vivero 1 (Sr.Francisco)")
    print("  2 - Vivero 2 (Sra.Zoila)")
    print("  3 - Ambos viveros")
    op = leer_opcion("  Opción: ", ["1", "2", "3"])
    if op == "1":
        return datos.VIV1
    if op == "2":
        return datos.VIV2
    return "AMBOS"


def elegir_periodo():
    """Retorna (etiqueta, mes, anio, op)."""
    print("\n  Período:")
    print("  1 - Todo el historial")
    print("  2 - Por año")
    print("  3 - Por mes y año")
    op = leer_opcion("  Opción: ", ["1", "2", "3"])
    if op == "1":
        return "Todo el historial", 0, 0, "1"
    if op == "2":
        anio = leer_entero_rango("  Año (ej: 2026): ", ANIO_MIN, ANIO_MAX)
        return str(anio), 0, anio, "2"
    mes  = leer_entero_rango("  Mes (1-12): ", 1, 12)
    anio = leer_entero_rango("  Año (ej: 2026): ", ANIO_MIN, ANIO_MAX)
    return f"{mes:02d}/{anio}", mes, anio, "3"


def fecha_menor(fa, fb):
    """Retorna True si la fecha fa es anterior a fb (dd/mm/aaaa)."""
    da, ma, aa = int(fa[0:2]), int(fa[3:5]), int(fa[6:10])
    db, mb, ab = int(fb[0:2]), int(fb[3:5]), int(fb[6:10])
    if aa != ab:
        return aa < ab
    if ma != mb:
        return ma < mb
    return da < db


def filtrar_cosechas(vivero, op, mes, anio):
    """Búsqueda lineal: retorna índices de cosechas que cumplen el filtro."""
    indices = []
    i = 0
    while i < len(datos.fechas_c):
        ok = True
        if vivero != "AMBOS" and datos.viveros_c[i] != vivero:
            ok = False
        if ok:
            partes = datos.fechas_c[i].split("/")
            d_mes  = int(partes[1])
            d_anio = int(partes[2])
            if op == "2" and d_anio != anio:
                ok = False
            if op == "3" and (d_mes != mes or d_anio != anio):
                ok = False
        if ok:
            indices.append(i)
        i += 1
    return indices


def filtrar_incidencias(vivero, op, mes, anio):
    """Búsqueda lineal: retorna índices de incidencias que cumplen el filtro."""
    indices = []
    i = 0
    while i < len(datos.fechas_i):
        ok = True
        if vivero != "AMBOS" and datos.viveros_i[i] != vivero:
            ok = False
        if ok:
            partes = datos.fechas_i[i].split("/")
            d_mes  = int(partes[1])
            d_anio = int(partes[2])
            if op == "2" and d_anio != anio:
                ok = False
            if op == "3" and (d_mes != mes or d_anio != anio):
                ok = False
        if ok:
            indices.append(i)
        i += 1
    return indices


def ordenar_burbuja(indices, lista_fechas):
    """
    Ordena la lista de índices por fecha ascendente.
    Algoritmo de burbuja con dos while anidados.
    Solo intercambia cuando el elemento de la derecha es menor.
    """
    n = len(indices)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if fecha_menor(lista_fechas[indices[j + 1]],
                        lista_fechas[indices[j]]):
                indices[j], indices[j + 1] = indices[j + 1], indices[j]
            j += 1
        i += 1
    return indices


def buscar_por_fecha(fecha_buscada, indices, lista_fechas):
    """
    Búsqueda lineal exacta por fecha dentro de los índices filtrados.
    Retorna lista de índices coincidentes, o None si el formato es inválido.
    """
    try:
        datetime.strptime(fecha_buscada, "%d/%m/%Y")
    except ValueError:
        return None
    encontrados = []
    i = 0
    while i < len(indices):
        if lista_fechas[indices[i]] == fecha_buscada:
            encontrados.append(indices[i])
        i += 1
    return encontrados