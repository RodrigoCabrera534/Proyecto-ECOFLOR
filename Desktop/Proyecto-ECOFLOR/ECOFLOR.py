# ============================================================
# ECOFLOR - Sistema de Gestión de Cosechas de Rosas
# Curso   : Fundamentos de Programación - CIIN1205P
# Docente : Pereda Cabanillas, Edwuard Jhonatan
# UPN     : Universidad Privada del Norte - Cajamarca
# Equipo  : Cabrera Sanchez, Rodrigo Alejandro
#           Lezcano Moreno, Mariana Jasmín
#           Sánchez Hernández, Hilter Alexis
#           Sandoval Villanueva, Becsy Yomar
#           Yopla Huamán, Ana Elizabeth
# ============================================================

ARCH_C = "cosechas.txt"
ARCH_I = "incidencias.txt"
VIV1   = "Vivero 1 (Sr.Francisco)"
VIV2   = "Vivero 2 (Sra.Zoila)"

# Arreglos paralelos - cosechas (T3)
fechas_c   = []
viveros_c  = []
bonches_c  = []
rosas_c    = []
m50_c      = []
m60_c      = []
m70_c      = []
rojo_c     = []
rosado_c   = []
blanco_c   = []
amarillo_c = []
cal_a_c    = []
cal_b_c    = []
obs_c      = []

# Arreglos paralelos - incidencias 
fechas_i   = []
viveros_i  = []
tipos_i    = []
detalles_i = []
impactos_i = []
obs_i      = []


# ── VALIDACIÓN DE ENTRADAS ─────────────────────

def leer_fecha():
    # Pide y valida fecha dd/mm/aaaa. Reintenta si hay error.
    while True:
        ent = input("  Fecha (dd/mm/aaaa): ").strip()
        p = ent.split("/")
        if len(p) != 3:
            print("  Error: use el formato dd/mm/aaaa.")
            continue
        if not (p[0].isdigit() and p[1].isdigit() and p[2].isdigit()):
            print("  Error: solo dígitos separados por /")
            continue
        d = int(p[0])
        m = int(p[1])
        a = int(p[2])
        if d < 1 or d > 31:
            print("  Error: día entre 1 y 31.")
            continue
        if m < 1 or m > 12:
            print("  Error: mes entre 1 y 12.")
            continue
        if a < 2010 or a > 2100:
            print("  Error: año entre 2010 y 2100.")
            continue
        return ent


def leer_entero_positivo(msg):
    # Pide entero >= 1. Reintenta si hay texto, cero o negativo.
    while True:
        ent = input(msg).strip()
        if not ent.isdigit():
            print("  Error: ingrese solo números enteros (ej: 20).")
            continue
        v = int(ent)
        if v >= 1:
            return v
        print("  Error: debe ser mayor o igual a 1.")


def leer_entero_no_negativo(msg):
    # Pide entero >= 0. Reintenta si hay texto o negativo.
    while True:
        ent = input(msg).strip()
        if not ent.isdigit():
            print("  Error: ingrese solo números enteros (ej: 5).")
            continue
        v = int(ent)
        if v >= 0:
            return v
        print("  Error: debe ser mayor o igual a 0.")


def leer_opcion(msg, opciones):
    # Pide una opción válida de la lista. Reintenta si no está.
    while True:
        ent = input(msg).strip()
        if ent in opciones:
            return ent
        print("  Error: opciones válidas -> " + ", ".join(opciones))


def leer_no_vacio(msg):
    # Pide texto no vacío. Reintenta si el usuario solo presiona Enter.
    while True:
        ent = input(msg).strip()
        if ent != "":
            return ent
        print("  Error: este campo no puede estar vacío.")


def leer_bloque_suma(campos, total):
    # Pide un entero por cada campo y valida que sumen 'total'
    while True:
        valores = []
        k = 0
        while k < len(campos):
            v = leer_entero_no_negativo("    " + campos[k] + ": ")
            valores.append(v)
            k = k + 1
        suma = 0
        k = 0
        while k < len(valores):
            suma = suma + valores[k]
            k = k + 1
        if suma == total:
            print("  Suma correcta: " + str(suma))
            return valores
        print("  Error: suma=" + str(suma) + " debe ser " + str(total) + ". Reintente.")


# ── ARCHIVOS  ───────────────────────────────────

def cargar_cosechas():
    # Lee cosechas.txt línea por línea y llena los arreglos paralelos.
    global fechas_c, viveros_c, bonches_c, rosas_c
    global m50_c, m60_c, m70_c
    global rojo_c, rosado_c, blanco_c, amarillo_c
    global cal_a_c, cal_b_c, obs_c
    fechas_c   = []
    viveros_c  = []
    bonches_c  = []
    rosas_c    = []
    m50_c      = []
    m60_c      = []
    m70_c      = []
    rojo_c     = []
    rosado_c   = []
    blanco_c   = []
    amarillo_c = []
    cal_a_c    = []
    cal_b_c    = []
    obs_c      = []
    try:
        arch = open(ARCH_C, "r", encoding="utf-8")
        linea = arch.readline()
        while linea != "":
            p = linea.strip().split(";")
            if len(p) == 14:
                fechas_c.append(p[0])
                viveros_c.append(p[1])
                bonches_c.append(int(p[2]))
                rosas_c.append(int(p[3]))
                m50_c.append(int(p[4]))
                m60_c.append(int(p[5]))
                m70_c.append(int(p[6]))
                rojo_c.append(int(p[7]))
                rosado_c.append(int(p[8]))
                blanco_c.append(int(p[9]))
                amarillo_c.append(int(p[10]))
                cal_a_c.append(int(p[11]))
                cal_b_c.append(int(p[12]))
                obs_c.append(p[13])
            linea = arch.readline()
        arch.close()
        print("  Cosechas cargadas: " + str(len(fechas_c)) + " registros.")
    except FileNotFoundError:
        print("  cosechas.txt no encontrado (0 registros).")


def guardar_cosechas():
    # Escribe todos los arreglos de cosechas en cosechas.txt.
    arch = open(ARCH_C, "w", encoding="utf-8")
    i = 0
    while i < len(fechas_c):
        linea = (fechas_c[i] + ";" + viveros_c[i] + ";" +
                 str(bonches_c[i]) + ";" + str(rosas_c[i]) + ";" +
                 str(m50_c[i]) + ";" + str(m60_c[i]) + ";" + str(m70_c[i]) + ";" +
                 str(rojo_c[i]) + ";" + str(rosado_c[i]) + ";" +
                 str(blanco_c[i]) + ";" + str(amarillo_c[i]) + ";" +
                 str(cal_a_c[i]) + ";" + str(cal_b_c[i]) + ";" +
                 obs_c[i] + "\n")
        arch.write(linea)
        i = i + 1
    arch.close()


def cargar_incidencias():
    # Lee incidencias.txt línea por línea y llena los arreglos paralelos.
    global fechas_i, viveros_i, tipos_i, detalles_i, impactos_i, obs_i
    fechas_i   = []
    viveros_i  = []
    tipos_i    = []
    detalles_i = []
    impactos_i = []
    obs_i      = []
    try:
        arch = open(ARCH_I, "r", encoding="utf-8")
        linea = arch.readline()
        while linea != "":
            p = linea.strip().split(";")
            if len(p) == 6:
                fechas_i.append(p[0])
                viveros_i.append(p[1])
                tipos_i.append(p[2])
                detalles_i.append(p[3])
                impactos_i.append(p[4])
                obs_i.append(p[5])
            linea = arch.readline()
        arch.close()
        print("  Incidencias cargadas: " + str(len(fechas_i)) + " registros.")
    except FileNotFoundError:
        print("  incidencias.txt no encontrado (0 registros).")


def guardar_incidencias():
    # Escribe todos los arreglos de incidencias en incidencias.txt.
    arch = open(ARCH_I, "w", encoding="utf-8")
    i = 0
    while i < len(fechas_i):
        linea = (fechas_i[i] + ";" + viveros_i[i] + ";" +
                 tipos_i[i] + ";" + detalles_i[i] + ";" +
                 impactos_i[i] + ";" + obs_i[i] + "\n")
        arch.write(linea)
        i = i + 1
    arch.close()


# ── FILTRADO Y ORDENAMIENTO  ────────────────────

def pedir_vivero_registro():
    print("\n  Vivero:")
    print("    1 - " + VIV1)
    print("    2 - " + VIV2)
    op = leer_opcion("  Seleccione (1/2): ", ["1", "2"])
    if op == "1":
        return VIV1
    return VIV2


def pedir_vivero_consulta():
    print("\n  Vivero:")
    print("    1 - " + VIV1)
    print("    2 - " + VIV2)
    print("    3 - Ambos")
    op = leer_opcion("  Seleccione (1/2/3): ", ["1", "2", "3"])
    if op == "1":
        return VIV1
    if op == "2":
        return VIV2
    return "Ambos"


def pedir_periodo():
    # Retorna (etiqueta, mes, año, op).
    print("\n  Período:")
    print("    1 - Todo el historial")
    print("    2 - Por año")
    print("    3 - Por mes y año")
    op = leer_opcion("  Seleccione (1/2/3): ", ["1", "2", "3"])
    mes  = 0
    año = 0
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    if op == "2":
        while True:
            año = leer_entero_positivo("  Año (ej: 2026): ")
            if 2010 <= año <= 2100:
                break
            print("  Error: año debe ser entre 2010 y 2100.")
        etiqueta = "Año " + str(año)
    elif op == "3":
        mes = int(leer_opcion("  Mes (1-12): ",
              ["1","2","3","4","5","6","7","8","9","10","11","12"]))
        while True:
            año = leer_entero_positivo("  Año (ej: 2026): ")
            if 2010 <= año <= 2100:
                break
            print("  Error: año debe ser entre 2010 y 2100.")
        etiqueta = meses[mes - 1] + " " + str(año)
    else:
        etiqueta = "Todo el historial"
    return etiqueta, mes, año, op


def fecha_menor(fa, fb):
    # Devuelve True si fa es ESTRICTAMENTE anterior a fb. (T4: split)
    pa = fa.split("/")
    pb = fb.split("/")
    aa = int(pa[2])
    ab = int(pb[2])
    ma = int(pa[1])
    mb = int(pb[1])
    da = int(pa[0])
    db = int(pb[0])
    if aa != ab:
        return aa < ab
    if ma != mb:
        return ma < mb
    return da < db


def filtrar_cosechas(vivero, op, mes, año):
    # Búsqueda lineal: devuelve índices que cumplen el filtro. 
    indices = []
    i = 0
    while i < len(fechas_c):
        if vivero != "Ambos" and viveros_c[i] != vivero:
            i = i + 1
            continue
        p = fechas_c[i].split("/")
        mi = int(p[1])
        ai = int(p[2])
        if op == "2" and ai != año:
            i = i + 1
            continue
        if op == "3" and (mi != mes or ai != año):
            i = i + 1
            continue
        indices.append(i)
        i = i + 1
    return indices


def filtrar_incidencias(vivero, op, mes, año):
    # Búsqueda lineal: devuelve índices que cumplen el filtro. (T3)
    indices = []
    i = 0   
    while i < len(fechas_i):
        if vivero != "Ambos" and viveros_i[i] != vivero:
            i = i + 1
            continue
        p = fechas_i[i].split("/")
        mi = int(p[1])
        ai = int(p[2])
        if op == "2" and ai != año:
            i = i + 1
            continue
        if op == "3" and (mi != mes or ai != año):
            i = i + 1
            continue
        indices.append(i)
        i = i + 1
    return indices


def ordenar_burbuja(indices, arreglo_fechas):
    # Ordenamiento burbuja por fecha ascendente. 
    # CORRECCIÓN: solo intercambia si el elemento derecho es
    # estrictamente menor que el izquierdo (evita swap en iguales).
    n = len(indices)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if fecha_menor(arreglo_fechas[indices[j+1]], arreglo_fechas[indices[j]]):
                aux          = indices[j]
                indices[j]   = indices[j+1]
                indices[j+1] = aux
            j = j + 1
        i = i + 1
    return indices


# ── OPCIÓN 1: REGISTRAR COSECHA ────────────

def registrar_cosecha():
    print("\n=== OPCIÓN 1 - REGISTRAR COSECHA ===\n")
    fecha   = leer_fecha()
    vivero  = pedir_vivero_registro()
    bonches = leer_entero_positivo("  Total de bonches cosechados: ")
    rosas   = bonches * 24
    print("  Rosas = " + str(bonches) + " x 24 = " + str(rosas))

    print("\n  MEDIDAS (deben sumar " + str(bonches) + " bonches):")
    vm  = leer_bloque_suma(["50 cm", "60 cm", "70-80-90 cm"], bonches)
    m50 = vm[0]
    m60 = vm[1]
    m70 = vm[2]

    print("\n  COLORES (deben sumar " + str(bonches) + " bonches):")
    vc       = leer_bloque_suma(["Rojo", "Rosado", "Blanco", "Amarillo"], bonches)
    rojo     = vc[0]
    rosado   = vc[1]
    blanco   = vc[2]
    amarillo = vc[3]

    print("\n  CALIDAD (deben sumar " + str(bonches) + " bonches):")
    vq    = leer_bloque_suma(["Calidad A", "Calidad B"], bonches)
    cal_a = vq[0]
    cal_b = vq[1]

    obs = input("  Observación (Enter para omitir): ").strip()

    print("\n  --- RESUMEN ---")
    print("  Fecha   : " + fecha + "   Vivero: " + vivero)
    print("  Bonches : " + str(bonches) + "   Rosas: " + str(rosas))
    print("  Medidas : 50cm=" + str(m50) + "  60cm=" + str(m60) + "  70-80-90cm=" + str(m70))
    print("  Colores : Rojo=" + str(rojo) + "  Rosado=" + str(rosado) +
          "  Blanco=" + str(blanco) + "  Amarillo=" + str(amarillo))
    print("  Calidad : A=" + str(cal_a) + "  B=" + str(cal_b))
    if obs != "":
        print("  Obs     : " + obs)

    if leer_opcion("  ¿Guardar? (1-Sí / 2-No): ", ["1", "2"]) == "1":
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
        print("  Guardado. Total cosechas: " + str(len(fechas_c)))
    else:
        print("  Registro cancelado.")


# ── OPCIÓN 2: HISTORIAL DE COSECHAS ──────────────

def ver_historial():
    print("\n=== OPCIÓN 2 - HISTORIAL DE COSECHAS ===")
    print("  (Todos los valores numéricos están en BONCHES)")
    vivero = pedir_vivero_consulta()
    etiqueta, mes, año, op = pedir_periodo()
    indices = filtrar_cosechas(vivero, op, mes, año)
    indices = ordenar_burbuja(indices, fechas_c)

    if len(indices) == 0:
        print("  Sin registros para el filtro seleccionado.")
        input("\n  Presione Enter para volver al menú...")
        return

    print("\n  Vivero : " + vivero)
    print("  Período: " + etiqueta)
    SEP = "  " + "-" * 120
    # Column widths (ajustables): fecha, vivero, bonches, rosas, m50, m60, m70,
    # rojo, rosado, blanco, amarillo, cal A, cal B
    w_fecha = 12
    w_viv   = 4
    w_bon   = 6
    w_ros   = 8
    w_m50   = 7
    w_m60   = 7
    w_m70   = 12
    w_rj    = 7
    w_rs    = 7
    w_bl    = 7
    w_am    = 9
    w_a     = 6
    w_b     = 6

    print(SEP)
    # Fila de categorías (agrupaciones centradas)
    print("  " +
        "Fecha".ljust(w_fecha) +
        "Viv".ljust(w_viv) +
        "Bon".rjust(w_bon) +
        "Rosas".rjust(w_ros) +
        "  " + "-MEDIDA-".center(w_m50 + w_m60 + w_m70) +
        "  " + "-COLOR-".center(w_rj + w_rs + w_bl + w_am) +
        "  " + "-CALIDAD-".center(w_a + w_b))
    # Fila de nombres de columna
    print("  " +
        "".ljust(w_fecha) +
        "".ljust(w_viv) +
        "".rjust(w_bon) +
        "".rjust(w_ros) +
        "50cm".rjust(w_m50) +
        "60cm".rjust(w_m60) +
        "70-80-90cm".rjust(w_m70) +
        "Rojo".rjust(w_rj) +
        "Rosado".rjust(w_rs) +
        "Blanco".rjust(w_bl) +
        "Amarillo".rjust(w_am) +
        "A".rjust(w_a) +
        "B".rjust(w_b))
    print(SEP)

    t_bon = 0
    t_ros = 0
    t_50  = 0
    t_60  = 0
    t_70  = 0
    t_rj  = 0
    t_rs  = 0
    t_bl  = 0
    t_am  = 0
    t_a   = 0
    t_b   = 0

    p = 0
    while p < len(indices):
        i = indices[p]
        if viveros_c[i] == VIV1:
            v = "V1"
        else:
            v = "V2"
        print("  " + fechas_c[i].ljust(w_fecha) + v.ljust(w_viv) +
            str(bonches_c[i]).rjust(w_bon) + str(rosas_c[i]).rjust(w_ros) +
            str(m50_c[i]).rjust(w_m50) + str(m60_c[i]).rjust(w_m60) + str(m70_c[i]).rjust(w_m70) +
            str(rojo_c[i]).rjust(w_rj) + str(rosado_c[i]).rjust(w_rs) +
            str(blanco_c[i]).rjust(w_bl) + str(amarillo_c[i]).rjust(w_am) +
            str(cal_a_c[i]).rjust(w_a) + str(cal_b_c[i]).rjust(w_b))
        t_bon = t_bon + bonches_c[i]
        t_ros = t_ros + rosas_c[i]
        t_50  = t_50  + m50_c[i]
        t_60  = t_60  + m60_c[i]
        t_70  = t_70  + m70_c[i]
        t_rj  = t_rj  + rojo_c[i]
        t_rs  = t_rs  + rosado_c[i]
        t_bl  = t_bl  + blanco_c[i]
        t_am  = t_am  + amarillo_c[i]
        t_a   = t_a   + cal_a_c[i]
        t_b   = t_b   + cal_b_c[i]
        p = p + 1

    print(SEP)
    # Totales alineados con las mismas anchuras
    print("  " + "TOTALES".ljust(w_fecha + w_viv) +
        str(t_bon).rjust(w_bon) + str(t_ros).rjust(w_ros) +
        str(t_50).rjust(w_m50) + str(t_60).rjust(w_m60) + str(t_70).rjust(w_m70) +
        str(t_rj).rjust(w_rj) + str(t_rs).rjust(w_rs) +
        str(t_bl).rjust(w_bl) + str(t_am).rjust(w_am) +
        str(t_a).rjust(w_a) + str(t_b).rjust(w_b))
    print(SEP)
    print("  Registros: " + str(len(indices)))
    print("  V1 = " + VIV1 + "   |   V2 = " + VIV2)

    # Búsqueda lineal por fecha exacta
    while True:
        busq = input("\n  Buscar fecha exacta (dd/mm/aaaa) o Enter para volver: ").strip()
        if busq == "":
            break
        encontrado = False
        b = 0
        while b < len(indices):
            i = indices[b]
            if fechas_c[i] == busq:
                print("  Fecha  : " + fechas_c[i] + "   Vivero: " + viveros_c[i])
                print("  Bonches: " + str(bonches_c[i]) + "   Rosas:" + str(rosas_c[i]))
                print("  Medidas: 50cm=" + str(m50_c[i]) +
                      "  60cm=" + str(m60_c[i]) + "      70-80-90cm=   " + str(m70_c[i]))
                print("  Colores: Rojo= " + str(rojo_c[i]) + "  Rosado= " + str(rosado_c[i]) +
                      "  Blanco= " + str(blanco_c[i]) + "  Amarillo=" + str(amarillo_c[i]))
                print("  Calidad: A= " + str(cal_a_c[i]) + "  B= " + str(cal_b_c[i]))
                if obs_c[i] != "":
                    print("  Obs    : " + obs_c[i])
                encontrado = True
                break
            b = b + 1
        if not encontrado:
            print("  No se encontró ningún registro con esa fecha.")


# ── OPCIÓN 3: REGISTRAR INCIDENCIA ────────

def registrar_incidencia():
    print("\n=== OPCIÓN 3 - REGISTRAR INCIDENCIA ===\n")
    fecha  = leer_fecha()
    vivero = pedir_vivero_registro()

    print("\n  Tipo de incidencia:")
    print("    1 - Actividad no realizada")
    print("    2 - Plaga o enfermedad")
    print("    3 - Daño clima o infraestructura")
    print("    4 - Otra")
    op_t = leer_opcion("  Seleccione (1/2/3/4): ", ["1","2","3","4"])
    tipos_nom = ["Actividad no realizada", "Plaga o enfermedad",
                 "Daño clima/infraestructura", "Otra"]
    tipo = tipos_nom[int(op_t) - 1]

    detalle = leer_no_vacio("  Detalle (obligatorio): ")

    print("\n  Nivel de impacto:")
    print("    1 - Bajo   2 - Medio   3 - Alto")
    op_i    = leer_opcion("  Seleccione (1/2/3): ", ["1","2","3"])
    imp_nom = ["Bajo", "Medio", "Alto"]
    impacto = imp_nom[int(op_i) - 1]

    obs = input("  Observación (Enter para omitir): ").strip()

    print("\n  --- RESUMEN ---")
    print("  Fecha  : " + fecha + "   Vivero: " + vivero)
    print("  Tipo   : " + tipo + "   Impacto: " + impacto)
    print("  Detalle: " + detalle)
    if obs != "":
        print("  Obs    : " + obs)

    if leer_opcion("  ¿Guardar? (1-Sí / 2-No): ", ["1","2"]) == "1":
        fechas_i.append(fecha)
        viveros_i.append(vivero)
        tipos_i.append(tipo)
        detalles_i.append(detalle)
        impactos_i.append(impacto)
        obs_i.append(obs)
        guardar_incidencias()
        print("  Guardado. Total incidencias: " + str(len(fechas_i)))
    else:
        print("  Registro cancelado.")


# ── OPCIÓN 4: VER INCIDENCIAS ────────────────────

def ver_incidencias():
    print("\n=== OPCIÓN 4 - VER INCIDENCIAS ===")
    vivero = pedir_vivero_consulta()
    etiqueta, mes, año, op = pedir_periodo()
    indices = filtrar_incidencias(vivero, op, mes, año)
    indices = ordenar_burbuja(indices, fechas_i)

    if len(indices) == 0:
        print("  Sin registros para el filtro seleccionado.")
        input("\n  Presione Enter para volver al menú...")
        return

    print("\n  Vivero : " + vivero)
    print("  Período: " + etiqueta)
    SEP = "  " + "-" * 72
    print(SEP)
    print("  " +
          "Fecha".ljust(12) +
          "Viv".ljust(4) +
          "Tipo".ljust(28) +
          "Impacto".ljust(9) +
          "Detalle")
    print(SEP)

    p = 0
    while p < len(indices):
        i = indices[p]
        if viveros_i[i] == VIV1:
            v = "V1"
        else:
            v = "V2"
        det = detalles_i[i]
        if len(det) > 18:
            det = det[0:18] + ".."
        print("  " + fechas_i[i].ljust(12) + v.ljust(4) +
              tipos_i[i].ljust(28) + impactos_i[i].ljust(9) + det)
        if obs_i[i] != "":
            print("    Obs: " + obs_i[i])
        p = p + 1

    print(SEP)
    print("  Total: " + str(len(indices)) + " incidencias.")
    print("  V1 = " + VIV1 + "   |   V2 = " + VIV2)

    # Búsqueda lineal por fecha exacta 
    while True:
        busq = input("\n  Buscar fecha exacta (dd/mm/aaaa) o Enter para volver: ").strip()
        if busq == "":
            break
        encontrado = False
        b = 0
        while b < len(indices):
            i = indices[b]
            if fechas_i[i] == busq:
                print("  Fecha  : " + fechas_i[i] + "   Vivero: " + viveros_i[i])
                print("  Tipo   : " + tipos_i[i] + "   Impacto: " + impactos_i[i])
                print("  Detalle: " + detalles_i[i])
                if obs_i[i] != "":
                    print("  Obs    : " + obs_i[i])
                encontrado = True
                break
            b = b + 1
        if not encontrado:
            print("  No se encontró ningún registro con esa fecha.")


# ── OPCIÓN 5: ANÁLISIS INTEGRAL──────────────────

def analisis_integral():
    print("\n=== OPCIÓN 5 - ANÁLISIS INTEGRAL ===")
    vivero = pedir_vivero_consulta()
    etiqueta, mes, año, op = pedir_periodo()

    ic = filtrar_cosechas(vivero, op, mes, año)
    ii = filtrar_incidencias(vivero, op, mes, año)
    ii = ordenar_burbuja(ii, fechas_i)

    print("\n  Vivero : " + vivero)
    print("  Período: " + etiqueta)

    # ── Estadísticas de cosechas ──────────────────────────────
    print("\n  " + "=" * 46)
    print("  COSECHAS")
    print("  " + "=" * 46)
    pct_b     = 0
    total_bon = 0
    if len(ic) == 0:
        print("  Sin cosechas en este período.")
    else:
        total_ros = 0
        total_m50 = 0
        total_m60 = 0
        total_m70 = 0
        total_rj  = 0
        total_rs  = 0
        total_bl  = 0
        total_am  = 0
        total_a   = 0
        total_b   = 0
        p = 0
        while p < len(ic):
            idx       = ic[p]
            total_bon = total_bon + bonches_c[idx]
            total_ros = total_ros + rosas_c[idx]
            total_m50 = total_m50 + m50_c[idx]
            total_m60 = total_m60 + m60_c[idx]
            total_m70 = total_m70 + m70_c[idx]
            total_rj  = total_rj  + rojo_c[idx]
            total_rs  = total_rs  + rosado_c[idx]
            total_bl  = total_bl  + blanco_c[idx]
            total_am  = total_am  + amarillo_c[idx]
            total_a   = total_a   + cal_a_c[idx]
            total_b   = total_b   + cal_b_c[idx]
            p = p + 1

        prom  = round(total_bon / len(ic), 2)
        pct_a = (total_a * 100) // total_bon
        pct_b = 100 - pct_a

        # Medida más producida
        medida_max = "50 cm"
        max_med    = total_m50
        if total_m60 > max_med:
            medida_max = "60 cm"
            max_med    = total_m60
        if total_m70 > max_med:
            medida_max = "70-80-90 cm"

        # Color más frecuente
        color_max = "Rojo"
        max_col   = total_rj
        if total_rs > max_col:
            color_max = "Rosado"
            max_col   = total_rs
        if total_bl > max_col:
            color_max = "Blanco"
            max_col   = total_bl
        if total_am > max_col:
            color_max = "Amarillo"

        print("  Registros    : " + str(len(ic)))
        print("  Total bonches: " + str(total_bon) +
              "   Total rosas: " + str(total_ros))
        print("  Prom/cosecha : " + str(prom) + " bonches")
        print("  " + "-" * 46)
        print("  Medida mayor : " + medida_max)
        print("  Color mayor  : " + color_max)
        print("  " + "-" * 46)
        print("  Calidad A    : " + str(pct_a) + "%  (" + str(total_a) + " bon)")
        print("  Calidad B    : " + str(pct_b) + "%  (" + str(total_b) + " bon)")

    # ── Conteo de incidencias por tipo ────────────────────────
    print("\n  " + "=" * 46)
    print("  INCIDENCIAS")
    print("  " + "=" * 46)
    total_inc = len(ii)
    plagas    = 0
    if total_inc == 0:
        print("  Sin incidencias en este período.")
    else:
        tipos_k = ["Actividad no realizada", "Plaga o enfermedad",
                   "Daño clima/infraestructura", "Otra"]
        conteos = [0, 0, 0, 0]
        p = 0
        while p < len(ii):
            t = tipos_i[ii[p]]
            j = 0
            while j < len(tipos_k):
                if tipos_k[j] == t:
                    conteos[j] = conteos[j] + 1
                    break
                j = j + 1
            p = p + 1

        tipo_max = tipos_k[0]
        max_t    = conteos[0]
        j = 1
        while j < len(tipos_k):
            if conteos[j] > max_t:
                max_t    = conteos[j]
                tipo_max = tipos_k[j]
            j = j + 1

        plagas = conteos[1]
        print("  Total            : " + str(total_inc))
        print("  Tipo más frecuente: " + tipo_max)
        print("  " + "-" * 46)
        k = 0
        while k < len(tipos_k):
            print("  " + tipos_k[k].ljust(28) + ": " + str(conteos[k]))
            k = k + 1

    # ── Recomendaciones automáticas ───────────────────────────
    print("\n  " + "=" * 46)
    print("  RECOMENDACIONES")
    print("  " + "=" * 46)
    alerta = False
    if len(ic) > 0 and total_bon > 0 and pct_b > 20:
        print("  [!] Calidad B supera el 20%. Revisar proceso de corte.")
        alerta = True
    if total_inc > 0 and plagas * 2 > total_inc:
        print("  [!] Más del 50% son plagas. Aplicar control fitosanitario.")
        alerta = True
    if not alerta:
        print("  [OK] Producción estable. Sin alertas en el período.")

    input("\n  [Presione Enter para volver al menú]")


# ── MENÚ PRINCIPAL ──────────────────────────────────

def menu_principal():
    # Bucle principal: 6 opciones, correspondencia 1:1 con funciones.
    while True:
        print("\n===================================")
        print("  ECOFLOR - GESTIÓN DE COSECHAS")
        print("===================================")
        print("  Cosechas   : " + str(len(fechas_c)))
        print("  Incidencias: " + str(len(fechas_i)))
        print()
        print("  1. Registrar cosecha")
        print("  2. Ver historial de cosechas")
        print("  3. Registrar incidencia")
        print("  4. Ver incidencias")
        print("  5. Análisis integral")
        print("  6. Salir")
        print("===================================")
        op = leer_opcion("  Opción (1-6): ", ["1","2","3","4","5","6"])
        if op == "1":
            registrar_cosecha()
        elif op == "2":
            ver_historial()
        elif op == "3":
            registrar_incidencia()
        elif op == "4":
            ver_incidencias()
        elif op == "5":
            analisis_integral()
        elif op == "6":
            if leer_opcion("  ¿Confirmar salida? (s/n): ", ["s","n"]) == "s":
                guardar_cosechas()
                guardar_incidencias()
                print("  Datos guardados. Saliendo...")
                break


# ── INICIO ───────────────────────────────────────────────────
print("  Iniciando...")
cargar_cosechas()
cargar_incidencias()
menu_principal()