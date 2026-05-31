# ============================================================
# PARTE 1 - RODRIGO: GESTIÓN DE COSECHAS (Opciones 1 y 2)
# Curso: Fundamentos de Programación - CIIN1205P
# ============================================================

from alexis import *
from becsy import *

def pedir_vivero():
    print("\n  Vivero:")
    print("    1 - Vivero A")
    print("    2 - Vivero B")
    print("    3 - Ambos viveros")
    op = leer_opcion("  Seleccione (1/2/3): ", ["1", "2", "3"])
    if op == "1":
        return "Vivero A"
    elif op == "2":
        return "Vivero B"
    else:
        return "Ambos"


def pedir_periodo():
    print("\n  Período:")
    print("    1 - Todo el historial")
    print("    2 - Por año")
    print("    3 - Por mes y año")
    op = leer_opcion("  Seleccione (1/2/3): ", ["1", "2", "3"])

    mes  = 0
    anio = 0

    if op == "2":
        anio     = leer_entero_positivo("  Año (ejemplo 2026): ")
        etiqueta = "Año " + str(anio)

    elif op == "3":
        mes  = int(leer_opcion("  Mes (1-12): ",
                   ["1","2","3","4","5","6","7","8","9","10","11","12"]))
        anio = leer_entero_positivo("  Año (ejemplo 2026): ")
        nombres_mes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
                        "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        etiqueta = nombres_mes[mes - 1] + " " + str(anio)

    else:
        etiqueta = "Todo el historial"

    return etiqueta, mes, anio, op


def filtrar_cosechas(vivero, op_periodo, mes, anio):
    indices = []
    i = 0
    while i < len(fechas_c):
        if vivero != "Ambos" and viveros_c[i] != vivero:
            i = i + 1
            continue
        partes = fechas_c[i].split("/")
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


def registrar_cosecha():
    print("\n=====================================")
    print("  OPCIÓN 1 — REGISTRAR COSECHA")
    print("=====================================\n")

    fecha   = leer_fecha()
    vivero  = pedir_vivero()
    bonches = leer_entero_positivo("  Total de bonches cosechados: ")
    rosas   = bonches * 24
    print("  Rosas calculadas: " + str(bonches) + " x 24 = " + str(rosas))

    print("\n  Distribución por MEDIDA (suma debe ser " + str(bonches) + "):")
    vals_medida = leer_bloque_suma(["50 cm", "60 cm", "70-90 cm"], bonches)
    m50 = vals_medida[0]
    m60 = vals_medida[1]
    m70 = vals_medida[2]

    print("\n  Distribución por COLOR (suma debe ser " + str(bonches) + "):")
    vals_color = leer_bloque_suma(["Rojo", "Rosado", "Blanco", "Amarillo"], bonches)
    rojo     = vals_color[0]
    rosado   = vals_color[1]
    blanco   = vals_color[2]
    amarillo = vals_color[3]

    print("\n  Distribución por CALIDAD (suma debe ser " + str(bonches) + "):")
    vals_cal = leer_bloque_suma(["Calidad A", "Calidad B"], bonches)
    cal_a = vals_cal[0]
    cal_b = vals_cal[1]

    obs = input("  Observación (opcional, Enter para omitir): ").strip()

    print("\n=====================================")
    print("  RESUMEN DE COSECHA")
    print("=====================================")
    print("  Fecha   : " + fecha)
    print("  Vivero  : " + vivero)
    print("  Bonches : " + str(bonches) + "  |  Rosas: " + str(rosas))
    print("  Medidas : 50cm=" + str(m50) + "  60cm=" + str(m60) + "  70-90cm=" + str(m70))
    print("  Colores : Rojo=" + str(rojo) + "  Rosado=" + str(rosado) +
          "  Blanco=" + str(blanco) + "  Amarillo=" + str(amarillo))
    print("  Calidad : A=" + str(cal_a) + "  B=" + str(cal_b))
    if obs != "":
        print("  Obs     : " + obs)
    else:
        print("  Obs     : (sin observación)")
    print("=====================================")

    op = leer_opcion("  1-Guardar  2-Cancelar  → ", ["1", "2"])
    if op == "1":
        fechas_c.append(fecha)
        viveros_c.append(vivero)
        bonches_c.append(bonches)
        rosas_c.append(rosas)
        m50_c.append(m50)
        m60_c.append(m60)
        m70_c.append(m70)
        rojo_c.append(rojo)
        rosado_c.append(rosado)
        blanco_c.append(blanco)
        amarillo_c.append(amarillo)
        cal_a_c.append(cal_a)
        cal_b_c.append(cal_b)
        obs_c.append(obs)
        guardar_cosechas()
        print("  Cosecha guardada. Total registros: " + str(len(fechas_c)))
    else:
        print("  Registro cancelado.")


def ver_historial():
    print("\n=====================================")
    print("  OPCIÓN 2 — VER HISTORIAL")
    print("=====================================")

    vivero                         = pedir_vivero()
    etiqueta, mes, anio, op_periodo = pedir_periodo()

    indices = filtrar_cosechas(vivero, op_periodo, mes, anio)
    indices = ordenar_burbuja(indices, fechas_c)

    if len(indices) == 0:
        print("  No hay registros para los filtros seleccionados.")
        return

    print("\n  Vivero: " + vivero + "  |  Período: " + etiqueta)
    print("  " + "-" * 80)
    print("  Fecha        Viv  Bon  Rosas  50   60   70+  Rj   Rs   Bl   Am   A    B")
    print("  " + "-" * 80)

    t_bon = 0
    t_ros = 0
    t_m50 = 0
    t_m60 = 0
    t_m70 = 0
    t_rj  = 0
    t_rs  = 0
    t_bl  = 0
    t_am  = 0
    t_a   = 0
    t_b   = 0

    p = 0
    while p < len(indices):
        idx = indices[p]
        if viveros_c[idx] == "Vivero A":
            viv_letra = "A"
        else:
            viv_letra = "B"
        print("  " +
              fechas_c[idx].ljust(12) +
              viv_letra.ljust(5) +
              str(bonches_c[idx]).rjust(4) +
              str(rosas_c[idx]).rjust(7) +
              str(m50_c[idx]).rjust(5) +
              str(m60_c[idx]).rjust(5) +
              str(m70_c[idx]).rjust(5) +
              str(rojo_c[idx]).rjust(5) +
              str(rosado_c[idx]).rjust(5) +
              str(blanco_c[idx]).rjust(5) +
              str(amarillo_c[idx]).rjust(5) +
              str(cal_a_c[idx]).rjust(5) +
              str(cal_b_c[idx]).rjust(5))
        t_bon = t_bon + bonches_c[idx]
        t_ros = t_ros + rosas_c[idx]
        t_m50 = t_m50 + m50_c[idx]
        t_m60 = t_m60 + m60_c[idx]
        t_m70 = t_m70 + m70_c[idx]
        t_rj  = t_rj  + rojo_c[idx]
        t_rs  = t_rs  + rosado_c[idx]
        t_bl  = t_bl  + blanco_c[idx]
        t_am  = t_am  + amarillo_c[idx]
        t_a   = t_a   + cal_a_c[idx]
        t_b   = t_b   + cal_b_c[idx]
        p = p + 1

    print("  " + "-" * 80)
    print("  TOTALES           " +
          str(t_bon).rjust(4) +
          str(t_ros).rjust(7) +
          str(t_m50).rjust(5) +
          str(t_m60).rjust(5) +
          str(t_m70).rjust(5) +
          str(t_rj).rjust(5) +
          str(t_rs).rjust(5) +
          str(t_bl).rjust(5) +
          str(t_am).rjust(5) +
          str(t_a).rjust(5) +
          str(t_b).rjust(5))
    print("\n  Registros mostrados: " + str(len(indices)))

    while True:
        busqueda = input("\n  Buscar por fecha exacta (dd/mm/aaaa) o Enter para volver: ").strip()
        if busqueda == "":
            break
        encontrado = False
        b = 0
        while b < len(indices):
            idx = indices[b]
            if fechas_c[idx] == busqueda:
                print("\n  Resultado — " + busqueda + ":")
                print("  Vivero  : " + viveros_c[idx])
                print("  Bonches : " + str(bonches_c[idx]) + "  |  Rosas: " + str(rosas_c[idx]))
                print("  Medidas : 50cm=" + str(m50_c[idx]) +
                      "  60cm=" + str(m60_c[idx]) +
                      "  70-90cm=" + str(m70_c[idx]))
                print("  Colores : Rojo=" + str(rojo_c[idx]) +
                      "  Rosado=" + str(rosado_c[idx]) +
                      "  Blanco=" + str(blanco_c[idx]) +
                      "  Amarillo=" + str(amarillo_c[idx]))
                print("  Calidad : A=" + str(cal_a_c[idx]) + "  B=" + str(cal_b_c[idx]))
                if obs_c[idx] != "":
                    print("  Obs     : " + obs_c[idx])
                else:
                    print("  Obs     : (sin observación)")
                encontrado = True
                break
            b = b + 1
        if not encontrado:
            print("  No se encontró ningún registro con esa fecha.")