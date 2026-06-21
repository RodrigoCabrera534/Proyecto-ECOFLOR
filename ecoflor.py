# ============================================================
# ECOFLOR - Módulo principal: ecoflor.py
# Curso: Fundamentos de Programación - CIIN1205P
# UPN Cajamarca - 2026
# Equipo:
#   Cabrera Sanchez, Rodrigo Alejandro
#   Lezcano Moreno, Mariana Jasmín
#   Sánchez Hernández, Hilter Alexis
#   Sandoval Villanueva, Becsy Yomar
#   Yopla Huamán, Ana Elizabeth
# ============================================================

import datos
import validaciones as val
import busqueda as bus

SEP = "-" * 68
RX = 24   # rosas por bonche (factor de multiplicación)


def etiqueta_vivero(nombre):
    if nombre == datos.VIV1:
        return "V1"
    if nombre == datos.VIV2:
        return "V2"
    return "??"


def acumular(claves, valores, clave, incremento=1):
    """
    Búsqueda lineal sobre dos listas paralelas (clave/valor).
    Si 'clave' ya existe, suma 'incremento' a su valor; si no,
    agrega un nuevo par al final. Reemplaza el uso de diccionarios
    (fuera de sílabo) en conteos por mes/tipo/etc.
    """
    i = 0
    while i < len(claves):
        if claves[i] == clave:
            valores[i] += incremento
            return
        i += 1
    claves.append(clave)
    valores.append(incremento)


def maximo_par(claves, valores):
    """Búsqueda lineal: retorna (clave, valor) del valor más alto."""
    if len(claves) == 0:
        return "", 0
    mejor_clave = claves[0]
    mejor_valor = valores[0]
    i = 1
    while i < len(claves):
        if valores[i] > mejor_valor:
            mejor_valor = valores[i]
            mejor_clave = claves[i]
        i += 1
    return mejor_clave, mejor_valor


def pedir_seccion(fn_pedir):
    """
    Envuelve un bloque de entrada con la opción de rehacer o volver al menú.
    Retorna (resultado, False) si OK, (None, True) si quiere volver al menú.
    """
    while True:
        resultado = fn_pedir()
        print("  1 - Continuar   2 - Rehacer este campo   0 - Volver al menú")
        op = val.leer_opcion("  Opción: ", ["1", "2", "0"])
        if op == "1":
            return resultado, False
        if op == "0":
            return None, True


# ══════════════════════════════════════════════════════════════
# OPCIÓN 1 — REGISTRAR COSECHA
# Flujo: Fecha → Vivero → Total bonches → ¿Hay rosas sueltas? →
#        Clase A y B (suman bonches) →
#        Medidas del total de bonches (4 grupos) →
#        Colores del total de bonches (4 colores) →
#        Si hay sueltas: medidas (4) + colores (4) →
#        Observación → Guardar
# ══════════════════════════════════════════════════════════════

def registrar_cosecha():
    print("\n" + "=" * 50)
    print("  REGISTRAR COSECHA")
    print("=" * 50)
    print("  (En cualquier paso: 0 = volver al menú)")
    # 1. Fecha
    fecha, cancel = pedir_seccion(val.leer_fecha)
    if cancel: return
    # 2. Vivero
    vivero, cancel = pedir_seccion(bus.elegir_vivero_registro)
    if cancel: return
    # 3. Total de bonches
    def _bonches():
        return val.leer_entero_rango(
            f"  Total de bonches cosechados (0-{val.MAX_BONCHES}): ",
            val.MIN_BONCHES, val.MAX_BONCHES)
    bonches, cancel = pedir_seccion(_bonches)
    if cancel: return
    # 4. ¿Hay rosas sueltas?
    def _hay_sueltas():
        print("\n  ¿Hay rosas sueltas (flores individuales sin bonche)?")
        print("  1 - Sí   2 - No")
        return val.leer_opcion("  Opción: ", ["1", "2"])
    hay_sueltas, cancel = pedir_seccion(_hay_sueltas)
    if cancel: return
    # 5. Clase A y B (suman bonches)
    def _calidad():
        return val.leer_calidad(bonches)
    calidad, cancel = pedir_seccion(_calidad)
    if cancel: return
    cal_a, cal_b = calidad
    # 6. Medidas del total de bonches (A no tiene <50, B sí; mezclamos según cal_b)
    #    Para simplificar el ingreso: pedimos medidas del total incluyendo <50 si cal_b>0
    incluir_men50 = cal_b > 0
    print(f"\n  MEDIDAS — {bonches} bonches en total")
    def _medidas_bon():
        return val.leer_distribucion_medida(bonches, incluir_menor50=incluir_men50)
    medidas_bon, cancel = pedir_seccion(_medidas_bon)
    if cancel: return
    bon_men50, bon50, bon60, bon7090 = medidas_bon
    # Distribuimos men50 todo a clase B (clase A nunca tiene <50)
    b_men50 = bon_men50
    # Proporciones A/B para 50,60,7090 (aproximación entera)
    if bonches > 0:
        a50   = min(bon50, round(bon50 * cal_a / bonches))
        resto = cal_a - a50
        a60   = min(bon60, resto)
        a7090 = resto - a60
    else:
        a50 = a60 = a7090 = 0
    b50   = bon50   - a50
    b60   = bon60   - a60
    b7090 = bon7090 - a7090
    # 7. Colores del total de bonches
    print(f"\n  COLORES — {bonches} bonches en total")
    def _colores_bon():
        return val.leer_distribucion_color(bonches)
    colores_bon, cancel = pedir_seccion(_colores_bon)
    if cancel: return
    bon_rojo, bon_blanco, bon_rosado, bon_amarillo = colores_bon
    # Distribuir colores proporcionalmente entre A y B
    if bonches > 0:
        a_rojo   = min(bon_rojo, round(bon_rojo * cal_a / bonches))
        resto    = cal_a - a_rojo
        a_blanco = min(bon_blanco, resto); resto -= a_blanco
        a_rosado = min(bon_rosado, resto); resto -= a_rosado
        a_amarillo = resto
    else:
        a_rojo = a_blanco = a_rosado = a_amarillo = 0
    b_rojo    = bon_rojo    - a_rojo
    b_blanco  = bon_blanco  - a_blanco
    b_rosado  = bon_rosado  - a_rosado
    b_amarillo= bon_amarillo- a_amarillo
    # 8. Rosas sueltas (solo si hay)
    rosas_sueltas = 0
    s_men50 = s50 = s60 = s7090 = 0
    s_rojo = s_blanco = s_rosado = s_amarillo = 0
    if hay_sueltas == "1":
        def _cant_sueltas():
            return val.leer_entero_rango(
                f"  Cantidad de rosas sueltas (0-{val.MAX_ROSAS_SUELTAS}): ",
                0, val.MAX_ROSAS_SUELTAS)
        rosas_sueltas, cancel = pedir_seccion(_cant_sueltas)
        if cancel: return
        if rosas_sueltas > 0:
            print(f"\n  MEDIDAS — {rosas_sueltas} rosas sueltas")
            def _med_s():
                return val.leer_distribucion_medida(rosas_sueltas, incluir_menor50=True)
            medida_s, cancel = pedir_seccion(_med_s)
            if cancel: return
            s_men50, s50, s60, s7090 = medida_s
            print(f"\n  COLORES — {rosas_sueltas} rosas sueltas")
            def _col_s():
                return val.leer_distribucion_color(rosas_sueltas)
            color_s, cancel = pedir_seccion(_col_s)
            if cancel: return
            s_rojo, s_blanco, s_rosado, s_amarillo = color_s
    # 9. Observación
    def _obs():
        return val.leer_texto("  Observación (Enter para omitir): ", obligatorio=False)
    obs, cancel = pedir_seccion(_obs)
    if cancel: return

    # ── Resumen ──
    print("\n  " + SEP)
    print("  RESUMEN DE COSECHA")
    print("  " + SEP)
    print(f"  Fecha  : {fecha}     Vivero: {vivero}")
    print(f"  Bonches: {bonches}   Clase A: {cal_a}   Clase B: {cal_b}   Sueltas: {rosas_sueltas}")
    print(f"  Medidas (bonches) → <50:{bon_men50}  50cm:{bon50}  60cm:{bon60}  70-90cm:{bon7090}")
    print(f"  Colores (bonches) → Rojo:{bon_rojo}  Blanco:{bon_blanco}  Rosado:{bon_rosado}  Amarillo:{bon_amarillo}")
    if rosas_sueltas > 0:
        print(f"  Medidas (sueltas) → <50:{s_men50}  50cm:{s50}  60cm:{s60}  70-90cm:{s7090}")
        print(f"  Colores (sueltas) → Rojo:{s_rojo}  Blanco:{s_blanco}  Rosado:{s_rosado}  Amarillo:{s_amarillo}")
    print("  " + SEP)

    op = val.leer_opcion("  ¿Guardar? (1-Sí  2-No  0-Menú): ", ["1", "2", "0"])
    if op != "1":
        print("  Registro cancelado.")
        return

    fila = [fecha, vivero, bonches, cal_a, cal_b, rosas_sueltas,
            a50, a60, a7090, a_rojo, a_blanco, a_rosado, a_amarillo,
            b_men50, b50, b60, b7090, b_rojo, b_blanco, b_rosado, b_amarillo,
            s_men50, s50, s60, s7090, s_rojo, s_blanco, s_rosado, s_amarillo, obs]
    i = 0
    while i < len(datos._LISTAS_COSECHAS):
        datos._LISTAS_COSECHAS[i].append(fila[i])
        i += 1
    datos.guardar_cosechas()


# ══════════════════════════════════════════════════════════════
# OPCIÓN 2 — VER HISTORIAL DE COSECHAS
# ══════════════════════════════════════════════════════════════

def _rx(n):
    """Formatea bonches con su equivalente en rosas entre paréntesis."""
    return f"{n} ({n*RX})"


def ver_historial():
    print("\n" + "=" * 50)
    print("  HISTORIAL DE COSECHAS")
    print("=" * 50)

    vivero = bus.elegir_vivero_consulta()
    etiqueta, mes, anio, op = bus.elegir_periodo()
    indices = bus.filtrar_cosechas(vivero, op, mes, anio)
    indices = bus.ordenar_burbuja(indices, datos.fechas_c)

    if len(indices) == 0:
        print("  Sin registros para el filtro seleccionado.")
        input("  [Enter para volver al menú]")
        return

    nombre_viv = "Ambos viveros" if vivero == "AMBOS" else vivero
    print(f"\n  Vivero: {nombre_viv}   Período: {etiqueta}")

    # ── TABLA HISTORIAL — UNA sola tabla, formato bonches(unidades) ──
    # Las medidas y colores son del total de bonches (A+B).
    # Las rosas sueltas SOLO existen en Clase B, así que se suman directo
    # como unidades dentro del total de producción (no van en tabla aparte).
    def br(b):
        """bonches(rosas): ej. 50(1200)"""
        return f"{b}({b * RX})"

    def br_total(bon, suelt):
        """Total de producción en unidades: bonches->rosas + sueltas registradas."""
        return f"{bon}({bon * RX + suelt})"

    # Anchos fijos para que quepan valores como 90(2160)
    W = 10   # ancho columna bonches/clase
    WS = 8   # ancho columna sueltas
    WM = 8   # ancho columna medida/color

    S = "-" * (16 + W*3 + WS + WM*8 + 30)
    print("\n  RESUMEN POR COSECHA  [formato: bonches(unidades)]")
    print("  " + S)
    # Cabecera línea 1
    print(f"  {'Fecha':<12} {'V':<2}"
          f"  {'Total':>{W}}  {'Clase A':>{W}}  {'Clase B':>{W}}  {'Sueltas':>{WS}}"
          f"  {'<50cm':>{WM}} {'50cm':>{WM}} {'60cm':>{WM}} {'70-90cm':>{WM}}"
          f"  {'Rojo':>{WM}} {'Blanco':>{WM}} {'Rosado':>{WM}} {'Amarillo':>{WM}}")
    print("  " + S)

    t_bon = t_a = t_b = t_suelt = 0
    t_men50 = t_50 = t_60 = t_7090 = 0
    t_rojo = t_blanco = t_rosado = t_amarillo = 0
    # Acumuladores de rosas sueltas por medida/color (siempre Clase B)
    ts_men50 = ts_50 = ts_60 = ts_7090 = 0
    ts_rojo = ts_blanco = ts_rosado = ts_amarillo = 0

    i = 0
    while i < len(indices):
        idx   = indices[i]
        viv   = etiqueta_vivero(datos.viveros_c[idx])
        bon   = datos.bonches_c[idx]
        ca    = datos.cal_a_c[idx]
        cb    = datos.cal_b_c[idx]
        suelt = datos.rosas_sueltas_c[idx]

        # Medidas totales de bonches (A+B), en cantidad de bonches
        men50 = datos.b_men50_c[idx]                          # solo B tiene <50
        m50   = datos.a50_c[idx]  + datos.b50_c[idx]
        m60   = datos.a60_c[idx]  + datos.b60_c[idx]
        m7090 = datos.a7090_c[idx]+ datos.b7090_c[idx]

        # Colores totales de bonches (A+B), en cantidad de bonches
        rojo   = datos.a_rojo_c[idx]    + datos.b_rojo_c[idx]
        blanco = datos.a_blanco_c[idx]  + datos.b_blanco_c[idx]
        rosado = datos.a_rosado_c[idx]  + datos.b_rosado_c[idx]
        amar   = datos.a_amarillo_c[idx]+ datos.b_amarillo_c[idx]

        # Rosas sueltas de esta cosecha: siempre Clase B, con su propia
        # medida y color (no llegaron a completar un bonche, pero sí
        # cuentan como unidades dentro de cada categoría)
        s_men50_r = datos.s_men50_c[idx]
        s_50_r    = datos.s50_c[idx]
        s_60_r    = datos.s60_c[idx]
        s_7090_r  = datos.s7090_c[idx]
        s_rojo_r    = datos.s_rojo_c[idx]
        s_blanco_r  = datos.s_blanco_c[idx]
        s_rosado_r  = datos.s_rosado_c[idx]
        s_amarillo_r= datos.s_amarillo_c[idx]

        print(f"  {datos.fechas_c[idx]:<12} {viv:<2}"
              f"  {br_total(bon, suelt):>{W}}  {br(ca):>{W}}  {br_total(cb, suelt):>{W}}  {suelt:>{WS}}"
              f"  {br_total(men50, s_men50_r):>{WM}} {br_total(m50, s_50_r):>{WM}}"
              f" {br_total(m60, s_60_r):>{WM}} {br_total(m7090, s_7090_r):>{WM}}"
              f"  {br_total(rojo, s_rojo_r):>{WM}} {br_total(blanco, s_blanco_r):>{WM}}"
              f" {br_total(rosado, s_rosado_r):>{WM}} {br_total(amar, s_amarillo_r):>{WM}}")

        t_bon  += bon;   t_a    += ca;    t_b    += cb;   t_suelt += suelt
        t_men50+= men50; t_50   += m50;   t_60   += m60;  t_7090  += m7090
        t_rojo += rojo;  t_blanco+= blanco; t_rosado+= rosado; t_amarillo+= amar
        ts_men50+= s_men50_r; ts_50+= s_50_r; ts_60+= s_60_r; ts_7090+= s_7090_r
        ts_rojo += s_rojo_r;  ts_blanco+= s_blanco_r
        ts_rosado+= s_rosado_r; ts_amarillo+= s_amarillo_r
        i += 1

    print("  " + S)
    print(f"  {'TOTAL':<14}"
          f"  {br_total(t_bon, t_suelt):>{W}}  {br(t_a):>{W}}  {br_total(t_b, t_suelt):>{W}}  {t_suelt:>{WS}}"
          f"  {br_total(t_men50, ts_men50):>{WM}} {br_total(t_50, ts_50):>{WM}}"
          f" {br_total(t_60, ts_60):>{WM}} {br_total(t_7090, ts_7090):>{WM}}"
          f"  {br_total(t_rojo, ts_rojo):>{WM}} {br_total(t_blanco, ts_blanco):>{WM}}"
          f" {br_total(t_rosado, ts_rosado):>{WM}} {br_total(t_amarillo, ts_amarillo):>{WM}}")
    print(f"  Registros: {len(indices)}")
    print(f"  Producción total en unidades (bonches→rosas + sueltas): {t_bon*RX + t_suelt}")

    while True:
        busq = input("\n  Buscar por fecha (dd/mm/aaaa) o Enter para volver: ").strip()
        if busq == "":
            break
        resultado = bus.buscar_por_fecha(busq, indices, datos.fechas_c)
        if resultado is None:
            print("  ✗ Formato de fecha inválido.")
            continue
        if len(resultado) == 0:
            print("  Sin resultados para esa fecha.")
            continue
        for idx in resultado:
            viv = etiqueta_vivero(datos.viveros_c[idx])
            print(f"\n  → {datos.fechas_c[idx]} | {viv} | "
                  f"Bon={_rx(datos.bonches_c[idx])}")
            print(f"    Clase A: {_rx(datos.cal_a_c[idx])} | "
                  f"50cm:{datos.a50_c[idx]} 60cm:{datos.a60_c[idx]} "
                  f"70-90cm:{datos.a7090_c[idx]} | "
                  f"Rojo:{datos.a_rojo_c[idx]} Blanco:{datos.a_blanco_c[idx]} "
                  f"Rosado:{datos.a_rosado_c[idx]} Amarillo:{datos.a_amarillo_c[idx]}")
            print(f"    Clase B: {_rx(datos.cal_b_c[idx])} | "
                  f"<50:{datos.b_men50_c[idx]} 50cm:{datos.b50_c[idx]} "
                  f"60cm:{datos.b60_c[idx]} 70-90cm:{datos.b7090_c[idx]} | "
                  f"Rojo:{datos.b_rojo_c[idx]} Blanco:{datos.b_blanco_c[idx]} "
                  f"Rosado:{datos.b_rosado_c[idx]} Amarillo:{datos.b_amarillo_c[idx]}")
            print(f"    Sueltas: {datos.rosas_sueltas_c[idx]}")
            if datos.obs_c[idx]:
                print(f"    Obs: {datos.obs_c[idx]}")


# ══════════════════════════════════════════════════════════════
# OPCIÓN 3 — REGISTRAR INCIDENCIA
# ══════════════════════════════════════════════════════════════

def registrar_incidencia():
    print("\n" + "=" * 50)
    print("  REGISTRAR INCIDENCIA")
    print("=" * 50)
    print("  (En cualquier paso: 0 = volver al menú)")

    fecha, cancel = pedir_seccion(val.leer_fecha)
    if cancel: return

    vivero, cancel = pedir_seccion(bus.elegir_vivero_registro)
    if cancel: return

    def _pedir_tipo():
        print("\n  Tipo de incidencia:")
        print("  1 - Plaga o enfermedad")
        print("  2 - Daño clima / infraestructura")
        print("  3 - Actividad no realizada")
        print("  4 - Otra")
        op_tipo = val.leer_opcion("  Opción: ", ["1", "2", "3", "4"])
        tipos_map = {"1": "Plaga o enfermedad", "2": "Daño clima/infraestructura",
                     "3": "Actividad no realizada", "4": "Otra"}
        tipo = tipos_map[op_tipo]
        if op_tipo == "4":
            especif = val.leer_texto("  Especifique: ", obligatorio=True)
            tipo = "Otra: " + especif
        return tipo
    tipo, cancel = pedir_seccion(_pedir_tipo)
    if cancel: return

    def _pedir_detalle():
        return val.leer_texto(
            f"  Detalle (mín {val.MIN_DETALLE} caracteres): ",
            obligatorio=True, min_chars=val.MIN_DETALLE)
    detalle, cancel = pedir_seccion(_pedir_detalle)
    if cancel: return

    def _pedir_impacto():
        print("\n  Impacto:")
        print("  1 - Bajo")
        print("  2 - Medio")
        print("  3 - Alto")
        op = val.leer_opcion("  Opción: ", ["1", "2", "3"])
        return ["Bajo", "Medio", "Alto"][int(op) - 1]
    impacto, cancel = pedir_seccion(_pedir_impacto)
    if cancel: return

    def _obs_i():
        return val.leer_texto("  Observación (Enter para omitir): ", obligatorio=False)
    obs, cancel = pedir_seccion(_obs_i)
    if cancel: return

    print("\n  " + SEP)
    print("  RESUMEN DE INCIDENCIA")
    print("  " + SEP)
    print(f"  Fecha   : {fecha}     Vivero : {vivero}")
    print(f"  Tipo    : {tipo}")
    print(f"  Detalle : {detalle}")
    print(f"  Impacto : {impacto}")
    if obs:
        print(f"  Obs     : {obs}")
    print("  " + SEP)

    op = val.leer_opcion("  ¿Guardar? (1-Sí  2-No  0-Menú): ", ["1", "2", "0"])
    if op != "1":
        print("  Registro cancelado.")
        return

    datos.fechas_i.append(fecha)
    datos.viveros_i.append(vivero)
    datos.tipos_i.append(tipo)
    datos.detalles_i.append(detalle)
    datos.impactos_i.append(impacto)
    datos.obs_i.append(obs)
    datos.guardar_incidencias()


# ══════════════════════════════════════════════════════════════
# OPCIÓN 4 — VER INCIDENCIAS
# ══════════════════════════════════════════════════════════════

def ver_incidencias():
    print("\n" + "=" * 50)
    print("  VER INCIDENCIAS")
    print("=" * 50)

    vivero = bus.elegir_vivero_consulta()
    etiqueta, mes, anio, op = bus.elegir_periodo()
    indices = bus.filtrar_incidencias(vivero, op, mes, anio)
    indices = bus.ordenar_burbuja(indices, datos.fechas_i)

    if len(indices) == 0:
        print("  Sin registros para el filtro seleccionado.")
        input("  [Enter para volver al menú]")
        return

    nombre_viv = "Ambos viveros" if vivero == "AMBOS" else vivero
    print(f"\n  Vivero: {nombre_viv}   Período: {etiqueta}")

    def _trunc(texto, ancho):
        """Recorta texto a 'ancho' caracteres, agregando '…' si no entra completo."""
        if len(texto) > ancho:
            return texto[:ancho - 1] + "…"
        return texto

    W_TIPO = 28
    W_DET  = 66

    SI = "-" * (12 + 2 + 7 + W_TIPO + W_DET + 10)
    print("\n  " + SI)
    print(f"  {'Fecha':<12} {'V':<2} {'Impacto':<7} {'Tipo':<{W_TIPO}} "
          f"{'Detalle':<{W_DET}}")
    print("  " + SI)

    i = 0
    while i < len(indices):
        idx = indices[i]
        viv = etiqueta_vivero(datos.viveros_i[idx])
        tipo    = _trunc(datos.tipos_i[idx], W_TIPO)
        detalle = _trunc(datos.detalles_i[idx], W_DET)
        print(f"  {datos.fechas_i[idx]:<12} {viv:<2} {datos.impactos_i[idx]:<7} "
              f"{tipo:<{W_TIPO}} {detalle:<{W_DET}}")
        i += 1

    print("  " + SI)
    print(f"  Total: {len(indices)} incidencias.")

    while True:
        busq = input("\n  Buscar por fecha (dd/mm/aaaa) o Enter para volver: ").strip()
        if busq == "":
            break
        resultado = bus.buscar_por_fecha(busq, indices, datos.fechas_i)
        if resultado is None:
            print("  ✗ Formato de fecha inválido.")
            continue
        if len(resultado) == 0:
            print("  Sin resultados para esa fecha.")
            continue
        for idx in resultado:
            viv = etiqueta_vivero(datos.viveros_i[idx])
            print(f"  → {datos.fechas_i[idx]} | {viv} | "
                  f"{datos.tipos_i[idx]} | {datos.impactos_i[idx]}")
            print(f"    {datos.detalles_i[idx]}")


# ══════════════════════════════════════════════════════════════
# OPCIÓN 5 — ANÁLISIS INTEGRAL
# Muestra datos NUEVOS (no repite lo que ya aparece en el historial):
# total de flores individuales producidas, proporción de rosas
# sueltas, mes pico de producción, calidad relativa por vivero,
# y el resumen de incidencias.
# ══════════════════════════════════════════════════════════════

def analisis_integral():
    print("\n" + "=" * 50)
    print("  ANÁLISIS INTEGRAL")
    print("=" * 50)

    if len(datos.bonches_c) == 0 and len(datos.tipos_i) == 0:
        print("  No hay datos para analizar.")
        input("  [Enter para volver]")
        return

    vivero = bus.elegir_vivero_consulta()
    etiqueta, mes, anio, op = bus.elegir_periodo()
    indices_c = bus.filtrar_cosechas(vivero, op, mes, anio)
    indices_i = bus.filtrar_incidencias(vivero, op, mes, anio)

    nombre_viv = "Ambos viveros" if vivero == "AMBOS" else vivero
    print(f"\n  Vivero: {nombre_viv}   Período: {etiqueta}")
    if len(indices_c) == 0 and len(indices_i) == 0:
        print("  No hay datos para el filtro seleccionado.")
        input("  [Enter para volver]")
        return
    if len(indices_c) > 0:
        t_bon = t_a = t_b = t_suelt = 0
        total_v1 = total_v2 = 0
        v1_a = v1_b = v2_a = v2_b = 0
        meses_c = []; totales_mes_c = []
        i = 0
        while i < len(indices_c):
            idx = indices_c[i]
            t_bon += datos.bonches_c[idx]
            t_a += datos.cal_a_c[idx]
            t_b += datos.cal_b_c[idx]
            t_suelt += datos.rosas_sueltas_c[idx]
            mc = datos.fechas_c[idx][3:10]
            acumular(meses_c, totales_mes_c, mc, datos.bonches_c[idx])
            if datos.viveros_c[idx] == datos.VIV1:
                total_v1 += datos.bonches_c[idx]
                v1_a += datos.cal_a_c[idx]; v1_b += datos.cal_b_c[idx]
            else:
                total_v2 += datos.bonches_c[idx]
                v2_a += datos.cal_a_c[idx]; v2_b += datos.cal_b_c[idx]
            i += 1
        # Flores individuales totales: bonches × 24 (en todas las clases) + sueltas
        total_flores = t_bon * RX + t_suelt
        pct_sueltas = round((t_suelt * 100) / total_flores, 2) if total_flores > 0 else 0
        prom = round(t_bon / len(indices_c), 2)
        lider = "V1" if total_v1 >= total_v2 else "V2"
        ratio_v1 = round(v1_a / v1_b, 1) if v1_b > 0 else 0
        ratio_v2 = round(v2_a / v2_b, 1) if v2_b > 0 else 0
        mejor_calidad = "V1" if ratio_v1 >= ratio_v2 else "V2"
        mes_pico, cant_pico = maximo_par(meses_c, totales_mes_c)
        print()
        print("  " + "=" * 46)
        print("       PRODUCCIÓN TOTAL DE FLORES")
        print("  " + "=" * 46)
        print(f"  Bonches cosechados        : {t_bon}  (→ {t_bon*RX} rosas)")
        print(f"  Rosas sueltas cosechadas  : {t_suelt}")
        print(f"  TOTAL flores individuales : {total_flores}")
        print(f"  Proporción de sueltas     : {pct_sueltas}% del total de flores")
        print()
        print(f"  Promedio de bonches por cosecha : {prom}")
        print(f"  Mes con mayor producción        : {mes_pico} ({cant_pico} bonches)")
        print(f"  Vivero con más bonches          : {lider} "
              f"(V1={total_v1}  V2={total_v2})")
        print()
        print("  CALIDAD RELATIVA POR VIVERO (bonches A por cada bonche B)")
        print(f"    Vivero 1: {ratio_v1} a 1")
        print(f"    Vivero 2: {ratio_v2} a 1")
        print(f"    → {mejor_calidad} tiene mejor proporción de calidad")
    if len(indices_i) > 0:
        tipos_vistos = []; conteos_tipo = []
        meses_i = []; totales_mes_i = []
        cont_alto = cont_medio = cont_bajo = 0
        i = 0
        while i < len(indices_i):
            idx = indices_i[i]
            t = datos.tipos_i[idx]
            m = datos.impactos_i[idx]
            mc = datos.fechas_i[idx][3:10]
            acumular(tipos_vistos, conteos_tipo, t, 1)
            acumular(meses_i, totales_mes_i, mc, 1)
            if m == "Alto":
                cont_alto += 1
            elif m == "Medio":
                cont_medio += 1
            else:
                cont_bajo += 1
            i += 1
        mes_max, cant_max = maximo_par(meses_i, totales_mes_i)
        print()
        print("  " + "=" * 46)
        print("       RESUMEN DE INCIDENCIAS")
        print("  " + "=" * 46)
        print(f"  Total incidencias    : {len(indices_i)}")
        print(f"  Mes con más casos    : {mes_max} ({cant_max})")
        print()
        print("  Por tipo:")
        j = 0
        while j < len(tipos_vistos):
            print(f"    {tipos_vistos[j]:<32}: {conteos_tipo[j]}")
            j += 1
        print()
        print("  Por nivel de impacto:")
        if cont_alto > 0:
            print(f"    {'Alto':<10}: {cont_alto}")
        if cont_medio > 0:
            print(f"    {'Medio':<10}: {cont_medio}")
        if cont_bajo > 0:
            print(f"    {'Bajo':<10}: {cont_bajo}")
    print()
    input("  [Enter para volver al menú]")


# ══════════════════════════════════════════════════════════════
# MENÚ PRINCIPAL
# ══════════════════════════════════════════════════════════════

def menu_principal():
    datos.cargar_cosechas()
    datos.cargar_incidencias()

    while True:
        print("\n" + "=" * 50)
        print("     ECOFLOR - Gestión de Cosechas e Incidencias")
        print("=" * 50)
        print("  1. Registrar cosecha")
        print("  2. Ver historial de cosechas")
        print("  3. Registrar incidencia")
        print("  4. Ver incidencias")
        print("  5. Análisis integral")
        print("  6. Salir")
        print("=" * 50)

        op = val.leer_opcion("  Opción: ", ["1", "2", "3", "4", "5", "6"])

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
        else:
            print("\n  Saliendo de ECOFLOR. ¡Hasta pronto!")
            break


if __name__ == "__main__":
    try:
        menu_principal()
    except (KeyboardInterrupt, EOFError):
        print("\n\n  Programa interrumpido. ¡Hasta pronto!")
