
def leer_fecha():
    while True:
        fecha = input("Ingrese fecha (dd/mm/aaaa): ").strip()

        partes = fecha.split("/")

        if len(partes) != 3:
            print("Formato incorrecto.")
            continue

        dia, mes, anio = partes

        if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
            print("La fecha debe contener solo números.")
            continue

        dia = int(dia)
        mes = int(mes)
        anio = int(anio)

        if not (1 <= dia <= 31):
            print("Día inválido.")
            continue

        if not (1 <= mes <= 12):
            print("Mes inválido.")
            continue

        if not (2000 <= anio <= 2100):
            print("Año inválido.")
            continue

        return fecha


def leer_entero_positivo(mensaje):
    while True:
        valor = input(mensaje).strip()

        if not valor.isdigit():
            print("Ingrese solo números.")
            continue

        valor = int(valor)

        if valor < 1:
            print("Debe ser mayor o igual a 1.")
            continue

        return valor


def leer_entero_no_negativo(mensaje):
    while True:
        valor = input(mensaje).strip()

        if not valor.isdigit():
            print("Ingrese solo números.")
            continue

        valor = int(valor)

        if valor < 0:
            print("No puede ser negativo.")
            continue

        return valor


def leer_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()

        if opcion in opciones_validas:
            return opcion

        print("Opción inválida.")


def leer_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("El campo no puede estar vacío.")


def leer_bloque_suma(campos, total):
    while True:
        valores = []
        suma = 0

        for campo in campos:
            valor = leer_entero_no_negativo(f"{campo}: ")
            valores.append(valor)
            suma += valor

        if suma == total:
            return valores

        print(f"La suma debe ser exactamente {total}.")


def fecha_es_menor(fecha_a, fecha_b):
    dia_a, mes_a, anio_a = map(int, fecha_a.split("/"))
    dia_b, mes_b, anio_b = map(int, fecha_b.split("/"))

    return (anio_a, mes_a, dia_a) < (anio_b, mes_b, dia_b)


def ordenar_burbuja(indices, arreglo_fechas):
    n = len(indices)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if fecha_es_menor(
                arreglo_fechas[indices[j + 1]],
                arreglo_fechas[indices[j]]
            ):
                indices[j], indices[j + 1] = indices[j + 1], indices[j]

    return indices
