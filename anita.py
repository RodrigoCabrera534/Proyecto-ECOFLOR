# ============================================================
# PARTE 3 - ANITA: ANÁLISIS INTEGRAL Y MENÚ PRINCIPAL
# Curso: Fundamentos de Programación - CIIN1205P
# ============================================================

from alexis import *
from becsy import *
from rodrigo import pedir_vivero, pedir_periodo, filtrar_cosechas
from jasmin import filtrar_incidencias


def analisis_integral():
    print("\n=====================================")
    print("  OPCIÓN 4 — ANÁLISIS INTEGRAL")
    print("=====================================")

    vivero = pedir_vivero()
    etiqueta, mes, anio, op_periodo = pedir_periodo()

    indices_c = filtrar_cosechas(vivero, op_periodo, mes, anio)
    indices_inc = filtrar_incidencias(vivero, op_periodo, mes, anio)

    print("\n  Vivero: " + vivero + "  |  Período: " + etiqueta)

    print("-------------------------------------")
    print("  COSECHAS")
    print("-------------------------------------")

    total_bon = 0

    if len(indices_c) == 0:
        print("  Sin registros de cosechas en este período.")
    else:
        total_ros = 0
        total_m50 = 0
        total_m60 = 0
        total_m70 = 0
        total_rj = 0
        total_rs = 0
        total_bl = 0
        total_am = 0
        total_a = 0
        total_b = 0

        p = 0
        while p < len(indices_c):
            idx = indices_c[p]
            total_bon = total_bon + bonches_c[idx]
            total_ros = total_ros + rosas_c[idx]
            total_m50 = total_m50 + m50_c[idx]
            total_m60 = total_m60 + m60_c[idx]
            total_m70 = total_m70 + m70_c[idx]
            total_rj = total_rj + rojo_c[idx]
            total_rs = total_rs + rosado_c[idx]
            total_bl = total_bl + blanco_c[idx]
            total_am = total_am + amarillo_c[idx]
            total_a = total_a + cal_a_c[idx]
            total_b = total_b + cal_b_c[idx]
            p = p + 1

        promedio = round(total_bon / len(indices_c), 2)

        medida_max = "50 cm"
        maximo_med = total_m50
        if total_m60 > maximo_med:
            medida_max = "60 cm"
            maximo_med = total_m60
        if total_m70 > maximo_med:
            medida_max = "70-90 cm"

        color_max = "Rojo"
        maximo_col = total_rj
        if total_rs > maximo_col:
            color_max = "Rosado"
            maximo_col = total_rs
        if total_bl > maximo_col:
            color_max = "Blanco"
            maximo_col = total_bl
        if total_am > maximo_col:
            color_max = "Amarillo"

        pct_a = (total_a * 100) // total_bon
        pct_b = 100 - pct_a

        print("  Registros analizados : " + str(len(indices_c)))
        print("  Total bonches        : " + str(total_bon))
        print("  Total rosas          : " + str(total_ros))
        print("  Promedio bonches/reg : " + str(promedio))
        print("  Medida más producida : " + medida_max)
        print("  Color más frecuente  : " + color_max)
        print("  % Calidad A          : " + str(pct_a) + "%")
        print("  % Calidad B          : " + str(pct_b) + "%")

    print("-------------------------------------")
    print("  INCIDENCIAS")
    print("-------------------------------------")

    plagas = 0
    total_inc = len(indices_inc)

    if total_inc == 0:
        print("  Sin incidencias en este período.")
    else:
        tipos_conocidos = ["Actividad no realizada",
                           "Plaga o enfermedad",
                           "Daño clima/infraestructura",
                           "Otra"]
        conteos_tipo = [0, 0, 0, 0]

        p = 0
        while p < len(indices_inc):
            idx = indices_inc[p]
            t = tipos_i[idx]
            j = 0
            while j < len(tipos_conocidos):
                if tipos_conocidos[j] == t:
                    conteos_tipo[j] = conteos_tipo[j] + 1
                    break
                j = j + 1
            p = p + 1

        tipo_max_nombre = tipos_conocidos[0]
        tipo_max_conteo = conteos_tipo[0]
        j = 1
        while j < len(tipos_conocidos):
            if conteos_tipo[j] > tipo_max_conteo:
                tipo_max_conteo = conteos_tipo[j]
                tipo_max_nombre = tipos_conocidos[j]
            j = j + 1

        cont_va = 0
        cont_vb = 0
        p = 0
        while p < len(indices_inc):
            idx = indices_inc[p]
            if viveros_i[idx] == "Vivero A":
                cont_va = cont_va + 1
            else:
                cont_vb = cont_vb + 1
            p = p + 1

        if cont_va >= cont_vb:
            viv_max = "Vivero A"
        else:
            viv_max = "Vivero B"

        copia = []
        p = 0
        while p < len(indices_inc):
            copia.append(indices_inc[p])
            p = p + 1
        copia = ordenar_burbuja(copia, fechas_i)
        ultima_fecha = fechas_i[copia[len(copia) - 1]]

        plagas = conteos_tipo[1]

        print("  Incidencias totales  : " + str(total_inc))
        print("  Tipo más frecuente   : " + tipo_max_nombre)
        print("  Vivero más afectado  : " + viv_max)
        print("  Última incidencia    : " + ultima_fecha)

    print("-------------------------------------")
    print("  RECOMENDACIÓN")
    print("-------------------------------------")
    hay_alerta = False

    if len(indices_c) > 0 and total_bon > 0 and pct_b > 20:
        print("  Revisar proceso de corte. Calidad B supera el 20%.")
        hay_alerta = True

    if total_inc > 0:
        if plagas * 2 > total_inc:
            print("  Más del 50% de incidencias son plagas. Aplicar control fitosanitario.")
            hay_alerta = True

    if not hay_alerta:
        print("  Producción estable. Sin alertas en el período.")

    print("=====================================")
    input("\n  [Presione Enter para volver al menú]")


def menu_principal():
    while True:
        print("\n=====================================")
        print("  ECOFLOR — GESTIÓN DE COSECHAS")
        print("=====================================")
        print("  Registros cargados: " + str(len(fechas_c)))
        print()
        print("  1. Registrar cosecha")
        print("  2. Ver historial de cosechas")
        print("  3. Registrar incidencia")
        print("  4. Análisis integral")
        print("  5. Ver incidencias")
        print("  6. Salir")
        print("=====================================")
        op = leer_opcion("  Seleccione una opción (1-6): ", ["1","2","3","4","5","6"])

        if op == "1":
            registrar_cosecha()
        elif op == "2":
            ver_historial()
        elif op == "3":
            registrar_incidencia()
        elif op == "4":
            analisis_integral()
        elif op == "5":
            ver_incidencias()
        elif op == "6":
            confirmar = leer_opcion("  ¿Seguro que desea salir? (s/n): ", ["s", "n"])
            if confirmar == "s":
                guardar_cosechas()
                guardar_incidencias()
                print("  Datos guardados.")
                print("  Hasta pronto!")
                break