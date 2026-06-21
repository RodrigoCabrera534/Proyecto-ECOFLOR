# ============================================================
# ECOFLOR - Módulo: validaciones.py
# Curso: Fundamentos de Programación - CIIN1205P
# UPN Cajamarca - 2026
# ============================================================

from datetime import datetime

MAX_BONCHES = 150
MAX_ROSAS_SUELTAS = 150
MIN_BONCHES = 0
MAX_CHARS   = 150
MIN_CHARS   = 5
MIN_DETALLE = 10
ANIO_MIN    = 2000
ANIO_MAX    = 2100


def leer_fecha():
    """Solicita fecha dd/mm/aaaa. Rechaza fechas imposibles."""
    while True:
        entrada = input("  Fecha (dd/mm/aaaa): ").strip()
        try:
            fecha = datetime.strptime(entrada, "%d/%m/%Y")
            if fecha.year < ANIO_MIN or fecha.year > ANIO_MAX:
                print(f"  ✗ Año debe estar entre {ANIO_MIN} y {ANIO_MAX}.")
                continue
            return fecha.strftime("%d/%m/%Y")
        except ValueError:
            print("  ✗ Fecha inválida. Use dd/mm/aaaa con días y meses reales.")


def leer_entero_rango(mensaje, minimo, maximo):
    """Pide un entero en [minimo, maximo]."""
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor < minimo or valor > maximo:
                print(f"  ✗ Valor entre {minimo} y {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ✗ Solo números enteros.")


def leer_entero_no_negativo(mensaje):
    """Pide un entero >= 0."""
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor < 0:
                print("  ✗ No puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("  ✗ Solo números enteros.")


def leer_opcion(mensaje, opciones):
    """Pide una opción de la lista."""
    while True:
        entrada = input(mensaje).strip()
        if entrada in opciones:
            return entrada
        print("  ✗ Opción no válida. Elija: " + " / ".join(opciones))


def leer_texto(mensaje, obligatorio=True, min_chars=None):
    """Lee texto con validaciones de longitud, letras y sin ';'."""
    minimo = min_chars if min_chars is not None else MIN_CHARS
    while True:
        entrada = input(mensaje).strip()
        if not obligatorio and entrada == "":
            return ""
        if obligatorio and entrada == "":
            print("  ✗ Este campo es obligatorio.")
            continue
        if obligatorio and len(entrada) < minimo:
            print(f"  ✗ Mínimo {minimo} caracteres.")
            continue
        if len(entrada) > MAX_CHARS:
            print(f"  ✗ Máximo {MAX_CHARS} caracteres.")
            continue
        if not any(c.isalpha() for c in entrada):
            print("  ✗ Debe contener al menos una letra.")
            continue
        if ";" in entrada:
            print("  ✗ No use el carácter ';'.")
            continue
        return entrada


def leer_distribucion_medida(total, incluir_menor50=False):
    """
    Pide la distribución por largo de tallo. Siempre retorna 4 valores
    (menor50, 50cm, 60cm, 70-80-90cm); si incluir_menor50 es False,
    el grupo 'menor50' no se pregunta y queda en 0 (caso Clase A,
    que nunca tiene tallos menores a 50 cm).
    La suma de los 4 valores debe ser exactamente 'total'.
    """
    print(f"\n  Medidas de tallo (deben sumar {total}):")
    while True:
        menor50 = 0
        if incluir_menor50:
            menor50 = leer_entero_no_negativo("    Menores de 50 cm : ")
        m50   = leer_entero_no_negativo("    50 cm           : ")
        m60   = leer_entero_no_negativo("    60 cm           : ")
        m7090 = leer_entero_no_negativo("    70-80-90 cm     : ")
        suma = menor50 + m50 + m60 + m7090
        if suma == total:
            return menor50, m50, m60, m7090
        print(f"  ✗ Suma {suma} ≠ {total}. Reintente.")


def leer_distribucion_color(total):
    """
    Pide la distribución por color: rojo, blanco, rosado, amarillo.
    La suma de los 4 valores debe ser exactamente 'total'.
    """
    print(f"\n  Colores (deben sumar {total}):")
    while True:
        rojo     = leer_entero_no_negativo("    Rojo    : ")
        blanco   = leer_entero_no_negativo("    Blanco  : ")
        rosado   = leer_entero_no_negativo("    Rosado  : ")
        amarillo = leer_entero_no_negativo("    Amarillo: ")
        suma = rojo + blanco + rosado + amarillo
        if suma == total:
            return rojo, blanco, rosado, amarillo
        print(f"  ✗ Suma {suma} ≠ {total}. Reintente.")


def leer_calidad(bonches):
    """
    Pide bonches Clase A (vendibles, ~95%) y Clase B (con defecto, ~5%).
    A + B deben sumar el total de bonches cosechados.
    """
    print(f"\n  Calidad de bonches (total cosechado: {bonches}):")
    while True:
        cal_a = leer_entero_no_negativo("    Clase A — bonches : ")
        cal_b = leer_entero_no_negativo("    Clase B — bonches : ")
        if cal_a + cal_b == bonches:
            return cal_a, cal_b
        print(f"  ✗ {cal_a}+{cal_b}={cal_a+cal_b} ≠ {bonches}. Reintente.")
