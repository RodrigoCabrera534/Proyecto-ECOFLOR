# ============================================================
# PARTE 2 - JASMIN: GESTIÓN DE INCIDENCIAS (Opciones 3 y 5)
# Curso: Fundamentos de Programación - CIIN1205P
# ============================================================

from alexis import *
from becsy import *
from rodrigo import pedir_vivero, pedir_periodo


def filtrar_incidencias(vivero, op_periodo, mes, anio):
    """Filtra índices de incidencias según criterios"""
    indices = []
    i = 0
    while i < len(fechas_i):
        if vivero != "Ambos" and viveros_i[i] != vivero:
            i = i + 1
            continue
        partes = fechas_i[i].split("/")
        mi = int(partes[1])
        ai = int(partes[2])
        if op_periodo == "2" and ai != anio:
            i = i + 1
            continue
        if op_periodo == "3" and (mi != mes or ai != anio):
            i = i + 1
            continue
        indices.append(i)
        i = i + 1
    return indices


def registrar_incidencia():
    """Opción 3: Registrar una nueva incidencia"""
    print("\n=====================================")
    print("  OPCIÓN 3 — REGISTRAR INCIDENCIA")
    print("=====================================\n")

    fecha = leer_fecha()
    vivero = pedir_vivero()

    print("\n  Tipo de incidencia:")
    print("    1 - Actividad no realizada")
    print("    2 - Plaga o enfermedad")
    print("    3 - Daño por clima o infraestructura")
    print("    4 - Otra")
    op_tipo = leer_opcion("  Seleccione (1/2/3/4): ", ["1", "2", "3", "4"])
    if op_tipo == "1":
        tipo = "Actividad no realizada"
    elif op_tipo == "2":
        tipo = "Plaga o enfermedad"
    elif op_tipo == "3":
        tipo = "Daño clima/infraestructura"
    else:
        tipo = "Otra"

    detalle = leer_no_vacio("  Detalle de la incidencia (obligatorio): ")

    print("\n  Nivel de impacto:")
    print("    1 - Bajo   2 - Medio   3 - Alto")
    op_imp = leer_opcion("  Seleccione (1/2/3): ", ["1", "2", "3"])
    if op_imp == "1":
        impacto = "Bajo"
    elif op_imp == "2":
        impacto = "Medio"
    else:
        impacto = "Alto"

    obs = input("  Observación (opcional, Enter para omitir): ").strip()

    print("\n=====================================")
    print("  RESUMEN DE INCIDENCIA")
    print("=====================================")
    print("  Fecha   : " + fecha)
    print("  Vivero  : " + vivero)
    print("  Tipo    : " + tipo)
    print("  Detalle : " + detalle)
    print("  Impacto : " + impacto)
    if obs != "":
        print("  Obs     : " + obs)
    else:
        print("  Obs     : (sin observación)")
    print("=====================================")

    op = leer_opcion("  1-Guardar  2-Cancelar  → ", ["1", "2"])
    if op == "1":
        fechas_i.append(fecha)
        viveros_i.append(vivero)
        tipos_i.append(tipo)
        detalles_i.append(detalle)
        impactos_i.append(impacto)
        obs_i.append(obs)
        guardar_incidencias()
        print("  Incidencia guardada. Total: " + str(len(fechas_i)))
    else:
        print("  Registro cancelado.")


def ver_incidencias():
    """Opción 5: Ver incidencias registradas"""
    print("\n=====================================")
    print("  OPCIÓN 5 — VER INCIDENCIAS")
    print("=====================================")

    vivero = pedir_vivero()
    etiqueta, mes, anio, op_periodo = pedir_periodo()

    indices = filtrar_incidencias(vivero, op_periodo, mes, anio)
    indices = ordenar_burbuja(indices, fechas_i)

    if len(indices) == 0:
        print("  No hay incidencias para los filtros seleccionados.")
        return

    print("\n  Vivero: " + vivero + "  |  Período: " + etiqueta)
    print("  " + "-" * 72)
    print("  Fecha        Viv  Tipo                        Impacto  Detalle")
    print("  " + "-" * 72)

    p = 0
    while p < len(indices):
        idx = indices[p]
        if viveros_i[idx] == "Vivero A":
            viv_letra = "A"
        else:
            viv_letra = "B"

        detalle_corto = detalles_i[idx]
        if len(detalle_corto) > 20:
            detalle_corto = detalle_corto[0:20]

        print("  " +
              fechas_i[idx].ljust(12) +
              viv_letra.ljust(5) +
              tipos_i[idx].ljust(28) +
              impactos_i[idx].ljust(9) +
              detalle_corto)
        p = p + 1

    print("  " + "-" * 72)
    print("\n  Total incidencias mostradas: " + str(len(indices)))