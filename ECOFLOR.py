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

VIV1 = "V1"
VIV2 = "V2"

# arreglos para cosechas
fechas_c = []
viveros_c = []
bonches_c = []
rosas_c = []
m50_c = []
m60_c = []
m70_c = []
rojo_c = []
rosado_c = []
blanco_c = []
amarillo_c = []
cal_a_c = []
cal_b_c = []

# arreglos para incidencias
fechas_i = []
viveros_i = []
tipos_i = []
detalles_i = []
impactos_i = []
obs_i      = []


# ── VALIDACIÓN DE ENTRADAS ─────────────────────

def leer_fecha():
    # Pide y valida fecha dd/mm/aaaa. Reintenta si hay error.
    while True:
        p = input("  Fecha (dd/mm/aaaa): ").strip().split('/')
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
        if a < 1900:
            print("  Error: año inválido.")
            continue
        return f"{d:02d}/{m:02d}/{a:04d}"


def leer_entero_positivo(msg):
    while True:
        ent = input(msg).strip()
        if not ent.isdigit():
            print("  Error: ingrese solo números enteros (ej: 20).")
            continue
        v = int(ent)
        if v >= 1:
            return v
        print("  Error: valor debe ser >= 1.")


def leer_entero_no_negativo(msg):
    while True:
        ent = input(msg).strip()
        if not ent.isdigit():
            print("  Error: ingrese solo números enteros (ej: 5).")
            continue
        v = int(ent)
        if v >= 0:
            return v
        print("  Error: valor debe ser >= 0.")


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
    # Lee una lista de enteros cuyo total debe ser 'total'.
    while True:
        vals = []
        suma = 0
        for c in campos:
            v = leer_entero_no_negativo("  " + c + ": ")
            vals.append(v)
            suma += v
        if suma != total:
            print("  Error: suma=" + str(suma) + " debe ser " + str(total) + ". Reintente.")
            continue
        return vals


# ── ARCHIVOS  ───────────────────────────────────

def cargar_cosechas():
    # Lee cosechas.txt línea por línea y llena los arreglos paralelos.
    global fechas_c, viveros_c, bonches_c, rosas_c
    global m50_c, m60_c, m70_c
    global rojo_c, rosado_c, blanco_c, amarillo_c
    global cal_a_c, cal_b_c
    fechas_c = []
    viveros_c = []
    bonches_c = []
    rosas_c = []
    m50_c = []
    m60_c = []
    m70_c = []
    rojo_c = []
    rosado_c = []
    blanco_c = []
    amarillo_c = []
    cal_a_c = []
    cal_b_c = []
    try:
        with open(ARCH_C, 'r', encoding='utf-8') as arch:
            for linea in arch:
                linea = linea.strip()
                if linea == '':
                    continue
                campos = linea.split('|')
                # formato esperado: fecha|vivero|bonches|rosas|m50|m60|m70|rojo|rosado|blanco|amarillo|cal_a|cal_b|obs
                fechas_c.append(campos[0])
                viveros_c.append(campos[1])
                bonches_c.append(int(campos[2]))
                rosas_c.append(int(campos[3]))
                m50_c.append(int(campos[4]))
                m60_c.append(int(campos[5]))
                m70_c.append(int(campos[6]))
                rojo_c.append(int(campos[7]))
                rosado_c.append(int(campos[8]))
                blanco_c.append(int(campos[9]))
                amarillo_c.append(int(campos[10]))
                cal_a_c.append(int(campos[11]))
                cal_b_c.append(int(campos[12]))
    except FileNotFoundError:
        # No hay archivo aún; empezamos vacíos
        pass


def guardar_cosechas():
    with open(ARCH_C, 'w', encoding='utf-8') as arch:
        for i in range(len(fechas_c)):
            campos = [fechas_c[i], viveros_c[i], str(bonches_c[i]), str(rosas_c[i]),
                      str(m50_c[i]), str(m60_c[i]), str(m70_c[i]),
                      str(rojo_c[i]), str(rosado_c[i]), str(blanco_c[i]), str(amarillo_c[i]),
                      str(cal_a_c[i]), str(cal_b_c[i])]
            arch.write('|'.join(campos) + '\n')


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
        with open(ARCH_I, 'r', encoding='utf-8') as arch:
            for linea in arch:
                linea = linea.strip()
                if linea == '':
                    continue
                campos = linea.split('|')
                # fecha|vivero|tipo|detalle|impacto|obs
                fechas_i.append(campos[0])
                viveros_i.append(campos[1])
                tipos_i.append(campos[2])
                detalles_i.append(campos[3])
                impactos_i.append(campos[4])
                obs_i.append(campos[5] if len(campos) > 5 else '')
    except FileNotFoundError:
        pass


def guardar_incidencias():
    with open(ARCH_I, 'w', encoding='utf-8') as arch:
        for i in range(len(fechas_i)):
            campos = [fechas_i[i], viveros_i[i], tipos_i[i], detalles_i[i], impactos_i[i], obs_i[i]]
            arch.write('|'.join(campos) + '\n')


# ── FILTRADO Y ORDENAMIENTO  ────────────────────

def pedir_vivero_registro():
    print("\n  Vivero:")
    print("    1 - " + VIV1)
    print("    2 - " + VIV2)
    op = leer_opcion("  Opción: ", ["1","2"]) 
    return VIV1 if op == "1" else VIV2


def pedir_vivero_consulta():
    print("\n  Vivero:")
    print("    1 - " + VIV1)
    print("    2 - " + VIV2)
    print("    3 - Ambos viveros")
    op = leer_opcion("  Opción: ", ["1","2","3"]) 
    if op == "1":
        return VIV1
    if op == "2":
        return VIV2
    return VIV1 + ',' + VIV2


def pedir_periodo():
    # Retorna (etiqueta, mes, año, op).
    print("\n  Período:")
    print("    1 - Todo el historial")
    print("    2 - Por año")
    print("    3 - Por mes y año")
    op = leer_opcion("  Opción: ", ["1","2","3"]) 
    if op == "1":
        return ("Todo", 0, 0, op)
    if op == "2":
        año = leer_entero_positivo("  Año: ")
        return (str(año), 0, año, op)
    mes = leer_entero_positivo("  Mes (1-12): ")
    año = leer_entero_positivo("  Año: ")
    return (f"{mes:02d}/{año}", mes, año, op)


def fecha_menor(fa, fb):
    # compara fechas dd/mm/aaaa
    da, ma, aa = map(int, fa.split('/'))
    db, mb, ab = map(int, fb.split('/'))
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
        ok = True
        if vivero != VIV1 + ',' + VIV2:
        if op == "2" and año != 0:
            if int(fechas_c[i].split('/')[-1]) != año:
                ok = False
        if op == "3":
            if int(fechas_c[i].split('/')[-1]) != año or int(fechas_c[i].split('/')[1]) != mes:
                ok = False
        if ok:
            indices.append(i)
        i += 1
    return indices


def filtrar_incidencias(vivero, op, mes, año):
    # Búsqueda lineal: devuelve índices que cumplen el filtro. (T3)
    indices = []
    i = 0   
    while i < len(fechas_i):
        ok = True
        if vivero != VIV1 + ',' + VIV2:
            if vivero != viveros_i[i]:
                ok = False
        if op == "2" and año != 0:
            if int(fechas_i[i].split('/')[-1]) != año:
                ok = False
        if op == "3":
            if int(fechas_i[i].split('/')[-1]) != año or int(fechas_i[i].split('/')[1]) != mes:
                ok = False
        if ok:
            indices.append(i)
        i += 1
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
            a_idx = indices[j]
            b_idx = indices[j+1]
            if fecha_menor(arreglo_fechas[b_idx], arreglo_fechas[a_idx]):
                indices[j], indices[j+1] = indices[j+1], indices[j]
            j += 1
        i += 1
    return indices


# OPCIÓN 1: REGISTRAR COSECHA

def registrar_cosecha():
    print("\n=== OPCIÓN 1 - REGISTRAR COSECHA ===\n")
    fecha   = leer_fecha()
    vivero  = pedir_vivero_registro()
    bonches = leer_entero_positivo("  Total de bonches cosechados: ")
    rosas   = leer_entero_no_negativo("  Rosas totales: ")
    # lee medidas
    m50 = leer_entero_no_negativo("    50cm: ")
    m60 = leer_entero_no_negativo("    60cm: ")
    m70 = leer_entero_no_negativo("    70-90cm: ")
    cal_a = leer_entero_no_negativo("  Cal. A: ")
    cal_b = leer_entero_no_negativo("  Cal. B: ")
    obs = input("  Observación (Enter para omitir): ").strip()

    print("\n  --- RESUMEN ---")
    print("  Fecha   : " + fecha + "   Vivero: " + vivero)
    print("  Bonches : " + str(bonches) + "   Rosas: " + str(rosas))
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
        rojo_c.append(0)
        rosado_c.append(0)
        blanco_c.append(0)
        amarillo_c.append(0)
        cal_a_c.append(cal_a)
        cal_b_c.append(cal_b)
        guardar_cosechas()
        print("  Registro guardado.")
    else:
        print("  Registro cancelado.")


# OPCIÓN 2: HISTORIAL DE COSECHAS

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
    print(SEP)
    print("  " + "Fecha".ljust(12) + "Viv".ljust(4) + "Bon".rjust(6) + "Rosas".rjust(8) + "  50cm".rjust(7) + "60cm".rjust(7) + "70-80-90cm".rjust(12) + "Rojo".rjust(7) + "Rosado".rjust(7) + "Blanco".rjust(7) + "Amarillo".rjust(9) + "A".rjust(6) + "B".rjust(6))
    print(SEP)

*** End Patch# ============================================================
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

VIV1 = "V1"
VIV2 = "V2"

# arreglos para cosechas
fechas_c = []
viveros_c = []
bonches_c = []
rosas_c = []
m50_c = []
m60_c = []
m70_c = []
rojo_c = []
rosado_c = []
blanco_c = []
amarillo_c = []
cal_a_c = []
cal_b_c = []

# arreglos para incidencias
fechas_i = []
viveros_i = []
tipos_i = []
detalles_i = []
impactos_i = []
obs_i      = []


# ── VALIDACIÓN DE ENTRADAS ─────────────────────

def leer_fecha():
    # Pide y valida fecha dd/mm/aaaa. Reintenta si hay error.
    while True:
        p = input("  Fecha (dd/mm/aaaa): ").strip().split('/')
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
        if a < 1900:
            print("  Error: año inválido.")
            continue
        return f"{d:02d}/{m:02d}/{a:04d}"


def leer_entero_positivo(msg):
    while True:
        ent = input(msg).strip()
        if not ent.isdigit():
            print("  Error: ingrese solo números enteros (ej: 20).")
            continue
        v = int(ent)
        if v >= 1:
            return v
        print("  Error: valor debe ser >= 1.")


def leer_entero_no_negativo(msg):
    while True:
        ent = input(msg).strip()
        if not ent.isdigit():
            print("  Error: ingrese solo números enteros (ej: 5).")
            continue
        v = int(ent)
        if v >= 0:
            return v
        print("  Error: valor debe ser >= 0.")


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
    # Lee una lista de enteros cuyo total debe ser 'total'.
    while True:
        vals = []
        suma = 0
        for c in campos:
            v = leer_entero_no_negativo("  " + c + ": ")
            vals.append(v)
            suma += v
        if suma != total:
            print("  Error: suma=" + str(suma) + " debe ser " + str(total) + ". Reintente.")
            continue
        return vals


# ── ARCHIVOS  ───────────────────────────────────

def cargar_cosechas():
    # Lee cosechas.txt línea por línea y llena los arreglos paralelos.
    global fechas_c, viveros_c, bonches_c, rosas_c
    global m50_c, m60_c, m70_c
    global rojo_c, rosado_c, blanco_c, amarillo_c
    global cal_a_c, cal_b_c
    fechas_c = []
    viveros_c = []
    bonches_c = []
    rosas_c = []
    m50_c = []
    m60_c = []
    m70_c = []
    rojo_c = []
    rosado_c = []
    blanco_c = []
    amarillo_c = []
    cal_a_c = []
    cal_b_c = []
    try:
        with open(ARCH_C, 'r', encoding='utf-8') as arch:
            for linea in arch:
                linea = linea.strip()
                if linea == '':
                    continue
                campos = linea.split('|')
                # formato esperado: fecha|vivero|bonches|rosas|m50|m60|m70|rojo|rosado|blanco|amarillo|cal_a|cal_b|obs
                fechas_c.append(campos[0])
                viveros_c.append(campos[1])
                bonches_c.append(int(campos[2]))
                rosas_c.append(int(campos[3]))
                m50_c.append(int(campos[4]))
                m60_c.append(int(campos[5]))
                m70_c.append(int(campos[6]))
                rojo_c.append(int(campos[7]))
                rosado_c.append(int(campos[8]))
                blanco_c.append(int(campos[9]))
                amarillo_c.append(int(campos[10]))
                cal_a_c.append(int(campos[11]))
                cal_b_c.append(int(campos[12]))
    except FileNotFoundError:
        # No hay archivo aún; empezamos vacíos
        pass


def guardar_cosechas():
    with open(ARCH_C, 'w', encoding='utf-8') as arch:
        for i in range(len(fechas_c)):
            campos = [fechas_c[i], viveros_c[i], str(bonches_c[i]), str(rosas_c[i]),
                      str(m50_c[i]), str(m60_c[i]), str(m70_c[i]),
                      str(rojo_c[i]), str(rosado_c[i]), str(blanco_c[i]), str(amarillo_c[i]),
                      str(cal_a_c[i]), str(cal_b_c[i])]
            arch.write('|'.join(campos) + '\n')


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
        with open(ARCH_I, 'r', encoding='utf-8') as arch:
            for linea in arch:
                linea = linea.strip()
                if linea == '':
                    continue
                campos = linea.split('|')
                # fecha|vivero|tipo|detalle|impacto|obs
                fechas_i.append(campos[0])
                viveros_i.append(campos[1])
                tipos_i.append(campos[2])
                detalles_i.append(campos[3])
                impactos_i.append(campos[4])
                obs_i.append(campos[5] if len(campos) > 5 else '')
    except FileNotFoundError:
        pass


def guardar_incidencias():
    with open(ARCH_I, 'w', encoding='utf-8') as arch:
        for i in range(len(fechas_i)):
            campos = [fechas_i[i], viveros_i[i], tipos_i[i], detalles_i[i], impactos_i[i], obs_i[i]]
            arch.write('|'.join(campos) + '\n')


# ── FILTRADO Y ORDENAMIENTO  ────────────────────

def pedir_vivero_registro():
    print("\n  Vivero:")
    print("    1 - " + VIV1)
    print("    2 - " + VIV2)
    op = leer_opcion("  Opción: ", ["1","2"]) 
    return VIV1 if op == "1" else VIV2


def pedir_vivero_consulta():
    print("\n  Vivero:")
    print("    1 - " + VIV1)
    print("    2 - " + VIV2)
    print("    3 - Ambos viveros")
    op = leer_opcion("  Opción: ", ["1","2","3"]) 
    if op == "1":
        return VIV1
    if op == "2":
        return VIV2
    return VIV1 + ',' + VIV2


def pedir_periodo():
    # Retorna (etiqueta, mes, año, op).
    print("\n  Período:")
    print("    1 - Todo el historial")
    print("    2 - Por año")
    print("    3 - Por mes y año")
    op = leer_opcion("  Opción: ", ["1","2","3"]) 
    if op == "1":
        return ("Todo", 0, 0, op)
    if op == "2":
        año = leer_entero_positivo("  Año: ")
        return (str(año), 0, año, op)
    mes = leer_entero_positivo("  Mes (1-12): ")
    año = leer_entero_positivo("  Año: ")
    return (f"{mes:02d}/{año}", mes, año, op)


def fecha_menor(fa, fb):
    # compara fechas dd/mm/aaaa
    da, ma, aa = map(int, fa.split('/'))
    db, mb, ab = map(int, fb.split('/'))
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
        ok = True
        if vivero != VIV1 + ',' + VIV2:
            if vivero != viveros_c[i]:
                ok = False
        if op == "2" and año != 0:
            if int(fechas_c[i].split('/')[-1]) != año:
                ok = False
        if op == "3":
            if int(fechas_c[i].split('/')[-1]) != año or int(fechas_c[i].split('/')[1]) != mes:
                ok = False
        if ok:
            indices.append(i)
        i += 1
    return indices


def filtrar_incidencias(vivero, op, mes, año):
    # Búsqueda lineal: devuelve índices que cumplen el filtro. (T3)
    indices = []
    i = 0   
    while i < len(fechas_i):
        ok = True
        if vivero != VIV1 + ',' + VIV2:
            if vivero != viveros_i[i]:
                ok = False
        if op == "2" and año != 0:
            if int(fechas_i[i].split('/')[-1]) != año:
                ok = False
        if op == "3":
            if int(fechas_i[i].split('/')[-1]) != año or int(fechas_i[i].split('/')[1]) != mes:
                ok = False
        if ok:
            indices.append(i)
        i += 1
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
            a_idx = indices[j]
            b_idx = indices[j+1]
            if fecha_menor(arreglo_fechas[b_idx], arreglo_fechas[a_idx]):
                indices[j], indices[j+1] = indices[j+1], indices[j]
            j += 1
        i += 1
    return indices


# OPCIÓN 1: REGISTRAR COSECHA

def registrar_cosecha():
    print("\n=== OPCIÓN 1 - REGISTRAR COSECHA ===\n")
    fecha   = leer_fecha()
    vivero  = pedir_vivero_registro()
    bonches = leer_entero_positivo("  Total de bonches cosechados: ")
    rosas   = leer_entero_no_negativo("  Rosas totales: ")
    # lee medidas
    m50 = leer_entero_no_negativo("    50cm: ")
    m60 = leer_entero_no_negativo("    60cm: ")
    m70 = leer_entero_no_negativo("    70-90cm: ")
    cal_a = leer_entero_no_negativo("  Cal. A: ")
    cal_b = leer_entero_no_negativo("  Cal. B: ")
    obs = input("  Observación (Enter para omitir): ").strip()

    print("\n  --- RESUMEN ---")
    print("  Fecha   : " + fecha + "   Vivero: " + vivero)
    print("  Bonches : " + str(bonches) + "   Rosas: " + str(rosas))
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
        rojo_c.append(0)
        rosado_c.append(0)
        blanco_c.append(0)
        amarillo_c.append(0)
        cal_a_c.append(cal_a)
        cal_b_c.append(cal_b)
        guardar_cosechas()
        print("  Registro guardado.")
    else:
        print("  Registro cancelado.")


# OPCIÓN 2: HISTORIAL DE COSECHAS

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
    print(SEP)
    print("  " + "Fecha".ljust(12) + "Viv".ljust(4) + "Bon".rjust(6) + "Rosas".rjust(8) + "  50cm".rjust(7) + "60cm".rjust(7) + "70-80-90cm".rjust(12) + "Rojo".rjust(7) + "Rosado".rjust(7) + "Blanco".rjust(7) + "Amarillo".rjust(9) + "A".rjust(6) + "B".rjust(6))
    print(SEP)

    t_bon = t_ros = t_50 = t_60 = t_70 = t_rj = t_rs = t_bl = t_am = t_a = t_b = 0
    for i in indices:
        v = "V1" if viveros_c[i] == VIV1 else "V2"
        print("  " + fechas_c[i].ljust(12) + v.ljust(4) + str(bonches_c[i]).rjust(6) + str(rosas_c[i]).rjust(8) + str(m50_c[i]).rjust(7) + str(m60_c[i]).rjust(7) + str(m70_c[i]).rjust(12) + str(rojo_c[i]).rjust(7) + str(rosado_c[i]).rjust(7) + str(blanco_c[i]).rjust(7) + str(amarillo_c[i]).rjust(9) + str(cal_a_c[i]).rjust(6) + str(cal_b_c[i]).rjust(6))
        t_bon += bonches_c[i]
        t_ros += rosas_c[i]
        t_50 += m50_c[i]
        t_60 += m60_c[i]
        t_70 += m70_c[i]
        t_rj += rojo_c[i]
        t_rs += rosado_c[i]
        t_bl += blanco_c[i]
        t_am += amarillo_c[i]
        t_a += cal_a_c[i]
        t_b += cal_b_c[i]

    print(SEP)
    print("  " + "TOTALES".ljust(16) + str(t_bon).rjust(6) + str(t_ros).rjust(8) + str(t_50).rjust(7) + str(t_60).rjust(7) + str(t_70).rjust(12) + str(t_rj).rjust(7) + str(t_rs).rjust(7) + str(t_bl).rjust(7) + str(t_am).rjust(9) + str(t_a).rjust(6) + str(t_b).rjust(6))
    print(SEP)
    print("  Registros: " + str(len(indices)))
    print("  V1 = " + VIV1 + "   |   V2 = " + VIV2)

    # Búsqueda lineal por fecha exacta
    while True:
        busq = input("\n  Buscar fecha exacta (dd/mm/aaaa) o Enter para volver: ").strip()
        if busq == "":
            break
        encontrado = False
        for idx in indices:
            if fechas_c[idx] == busq:
                print("  Encontrado: " + fechas_c[idx])
                encontrado = True
                break
        if not encontrado:
            print("  No se encontró ningún registro con esa fecha.")


# OPCIÓN 3: REGISTRAR INCIDENCIA

def registrar_incidencia():
    print("\n=== OPCIÓN 3 - REGISTRAR INCIDENCIA ===\n")
    fecha  = leer_fecha()
    vivero = pedir_vivero_registro()
    print("  Tipo de incidencia:")
    print("    1 - Plagas")
    print("    2 - Enfermedades")
    print("    3 - Clima")
    op = leer_opcion("  Opción: ", ["1","2","3"]) 
    tipo = {"1":"Plagas","2":"Enfermedades","3":"Clima"}[op]
    detalle = leer_no_vacio("  Detalle: ")
    print("  Impacto:")
    print("    1 - Bajo")
    print("    2 - Medio")
    print("    3 - Alto")
    op_i = leer_opcion("  Opción impacto: ", ["1","2","3"]) 
    imp_nom = ["Bajo", "Medio", "Alto"]
    impacto = imp_nom[int(op_i) - 1]
    obs = input("  Observación (Enter para omitir): ").strip()

    print("\n  --- RESUMEN ---")
    print("  Fecha  : " + fecha + "   Vivero: " + vivero)
    print("  Tipo   : " + tipo + "   Impacto: " + impacto)
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
        print("  Registro guardado.")
    else:
        print("  Registro cancelado.")


# OPCIÓN 4: VER INCIDENCIAS

def ver_incidencias():
    print("\n=== OPCIÓN 4 - VER INCIDENCIAS ===")
    vivero = pedir_vivero_consulta()
    etiqueta, mes, año, op = pedir_periodo()
    indices = filtrar_incidencias(vivero, op, mes, año)

    if len(indices) == 0:
        print("  Sin registros para el filtro seleccionado.")
        input("\n  Presione Enter para volver al menú...")
        return

    print("\n  Vivero : " + vivero)
    print("  Período: " + etiqueta)
    SEP = "  " + "-" * 72
    print(SEP)
    print("  Fecha       Tipo         Detalle                          Impacto   Obs")
    print(SEP)
    for i in indices:
        print("  " + fechas_i[i].ljust(12) + "  " + tipos_i[i].ljust(12) + "  " + detalles_i[i].ljust(30) + "  " + impactos_i[i].ljust(8) + "  " + obs_i[i])
    print(SEP)
    print("  Total: " + str(len(indices)) + " incidencias.")
    print("  V1 = " + VIV1 + "   |   V2 = " + VIV2)

    # Búsqueda lineal por fecha exacta 
    while True:
        busq = input("\n  Buscar fecha exacta (dd/mm/aaaa) o Enter para volver: ").strip()
        if busq == "":
            break
        encontrado = False
        for idx in indices:
            if fechas_i[idx] == busq:
                print("  Encontrado: " + fechas_i[idx] + " - " + tipos_i[idx])
                encontrado = True
                break
        if not encontrado:
            print("  No se encontró ningún registro con esa fecha.")


# Menú principal y arranque

def menu_principal():
    cargar_cosechas()
    cargar_incidencias()
    while True:
        print("\n==== ECOFLOR - Menú Principal ====")
        print("  1 - Registrar cosecha")
        print("  2 - Ver historial de cosechas")
        print("  3 - Registrar incidencia")
        print("  4 - Ver incidencias")
        print("  5 - Salir")
        opt = leer_opcion("  Opción: ", ["1","2","3","4","5"]) 
        if opt == "1":
            registrar_cosecha()
        elif opt == "2":
            ver_historial()
        elif opt == "3":
            registrar_incidencia()
        elif opt == "4":
            ver_incidencias()
        else:
            print("Saliendo...")
            break


if __name__ == '__main__':
    menu_principal()
