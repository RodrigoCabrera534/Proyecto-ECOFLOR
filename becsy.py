# ============================================================
# PARTE 4 - BECSY: GESTIÓN DE DATOS Y ARCHIVOS
# Curso: Fundamentos de Programación - CIIN1205P
# ============================================================

ARCHIVO_COSECHAS    = "cosechas.txt"
ARCHIVO_INCIDENCIAS = "incidencias.txt"

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

fechas_i   = []
viveros_i  = []
tipos_i    = []
detalles_i = []
impactos_i = []
obs_i      = []


def cargar_cosechas():
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
        archivo = open(ARCHIVO_COSECHAS, "r", encoding="utf-8")
        linea = archivo.readline()
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
            linea = archivo.readline()
        archivo.close()
        print("  " + ARCHIVO_COSECHAS + " cargado: " + str(len(fechas_c)) + " registros.")
    except FileNotFoundError:
        print("  " + ARCHIVO_COSECHAS + " no existe aún (0 registros).")


def guardar_cosechas():
    archivo = open(ARCHIVO_COSECHAS, "w", encoding="utf-8")
    i = 0
    while i < len(fechas_c):
        linea = (fechas_c[i] + ";" + viveros_c[i] + ";" +
                str(bonches_c[i]) + ";" + str(rosas_c[i]) + ";" +
                str(m50_c[i]) + ";" + str(m60_c[i]) + ";" + str(m70_c[i]) + ";" +
                str(rojo_c[i]) + ";" + str(rosado_c[i]) + ";" +
                str(blanco_c[i]) + ";" + str(amarillo_c[i]) + ";" +
                str(cal_a_c[i]) + ";" + str(cal_b_c[i]) + ";" +
                obs_c[i] + "\n")
        archivo.write(linea)
        i = i + 1
    archivo.close()


def cargar_incidencias():
    global fechas_i, viveros_i, tipos_i, detalles_i, impactos_i, obs_i

    fechas_i   = []
    viveros_i  = []
    tipos_i    = []
    detalles_i = []
    impactos_i = []
    obs_i      = []

    try:
        archivo = open(ARCHIVO_INCIDENCIAS, "r", encoding="utf-8")
        linea = archivo.readline()
        while linea != "":
            p = linea.strip().split(";")
            if len(p) == 6:
                fechas_i.append(p[0])
                viveros_i.append(p[1])
                tipos_i.append(p[2])
                detalles_i.append(p[3])
                impactos_i.append(p[4])
                obs_i.append(p[5])
            linea = archivo.readline()
        archivo.close()
        print("  " + ARCHIVO_INCIDENCIAS + " cargado: " + str(len(fechas_i)) + " incidencias.")
    except FileNotFoundError:
        print("  " + ARCHIVO_INCIDENCIAS + " no existe aún (0 incidencias).")


def guardar_incidencias():
    archivo = open(ARCHIVO_INCIDENCIAS, "w", encoding="utf-8")
    i = 0
    while i < len(fechas_i):
        linea = (fechas_i[i] + ";" + viveros_i[i] + ";" + tipos_i[i] + ";" +
                detalles_i[i] + ";" + impactos_i[i] + ";" + obs_i[i] + "\n")
        archivo.write(linea)
        i = i + 1
    archivo.close()


def generar_datos_prueba():
    archivo_tiene_datos = False
    try:
        archivo = open(ARCHIVO_COSECHAS, "r", encoding="utf-8")
        primera_linea = archivo.readline()
        archivo.close()
        if primera_linea.strip() != "":
            archivo_tiene_datos = True
    except FileNotFoundError:
        archivo_tiene_datos = False

    if archivo_tiene_datos:
        return

    datos_c = [
        "01/01/2026;Vivero A;20;480;8;7;5;10;5;3;2;19;1;inicio año",
        "03/01/2026;Vivero B;22;528;9;8;5;11;6;3;2;21;1;",
        "05/01/2026;Vivero A;18;432;6;8;4;9;4;3;2;17;1;",
        "07/01/2026;Vivero B;25;600;10;10;5;12;8;3;2;23;2;",
        "10/01/2026;Vivero A;30;720;10;12;8;14;9;4;3;28;2;",
        "12/01/2026;Vivero B;20;480;7;8;5;10;5;3;2;19;1;",
        "15/01/2026;Vivero A;24;576;8;10;6;12;7;3;2;22;2;",
        "17/01/2026;Vivero B;28;672;10;11;7;14;8;4;2;26;2;",
        "20/01/2026;Vivero A;22;528;8;9;5;11;6;3;2;20;2;",
        "22/01/2026;Vivero B;26;624;10;10;6;13;7;4;2;24;2;",
        "25/01/2026;Vivero A;20;480;7;8;5;10;5;3;2;19;1;",
        "27/01/2026;Vivero B;24;576;9;10;5;12;7;3;2;22;2;",
        "01/02/2026;Vivero A;18;432;6;8;4;9;4;3;2;17;1;",
        "03/02/2026;Vivero B;22;528;8;9;5;11;6;3;2;20;2;",
        "06/02/2026;Vivero A;25;600;9;10;6;12;8;3;2;23;2;",
        "08/02/2026;Vivero B;20;480;7;8;5;10;5;3;2;19;1;",
        "10/02/2026;Vivero A;30;720;12;11;7;15;9;4;2;28;2;buen clima",
        "12/02/2026;Vivero B;28;672;10;11;7;14;8;4;2;26;2;",
        "15/02/2026;Vivero A;22;528;8;9;5;11;6;3;2;20;2;",
        "17/02/2026;Vivero B;24;576;9;10;5;12;7;3;2;22;2;",
        "20/02/2026;Vivero A;20;480;7;8;5;10;5;3;2;19;1;",
        "22/02/2026;Vivero B;26;624;10;10;6;13;7;4;2;24;2;",
        "01/03/2026;Vivero A;22;528;8;9;5;11;6;3;2;20;2;",
        "03/03/2026;Vivero B;24;576;9;10;5;12;7;3;2;22;2;",
        "05/03/2026;Vivero A;18;432;6;8;4;9;4;3;2;17;1;",
        "08/03/2026;Vivero B;28;672;10;11;7;14;8;4;2;26;2;",
        "10/03/2026;Vivero A;25;600;9;10;6;12;8;3;2;23;2;",
        "12/03/2026;Vivero B;20;480;7;8;5;10;5;3;2;19;1;",
        "15/03/2026;Vivero A;30;720;12;11;7;15;9;4;2;28;2;",
        "17/03/2026;Vivero B;22;528;8;9;5;11;6;3;2;20;2;",
        "20/03/2026;Vivero A;24;576;9;10;5;12;7;3;2;22;2;",
        "22/03/2026;Vivero B;26;624;10;10;6;13;7;4;2;24;2;",
        "01/04/2026;Vivero A;20;480;7;8;5;10;5;3;2;19;1;",
        "03/04/2026;Vivero B;22;528;8;9;5;11;6;3;2;20;2;",
        "06/04/2026;Vivero A;25;600;9;10;6;12;8;3;2;23;2;",
        "08/04/2026;Vivero B;28;672;10;11;7;14;8;4;2;26;2;",
        "10/04/2026;Vivero A;18;432;6;8;4;9;4;3;2;17;1;",
        "12/04/2026;Vivero B;30;720;12;11;7;15;9;4;2;28;2;",
        "15/04/2026;Vivero A;22;528;8;9;5;11;6;3;2;20;2;",
        "17/04/2026;Vivero B;24;576;9;10;5;12;7;3;2;22;2;",
        "01/05/2026;Vivero A;20;480;8;7;5;10;5;3;2;19;1;lluvia leve",
        "05/05/2026;Vivero B;25;600;10;10;5;12;8;3;2;23;2;",
        "08/05/2026;Vivero A;18;432;6;8;4;9;4;3;2;17;1;",
        "10/05/2026;Vivero B;22;528;8;9;5;11;6;3;2;20;2;",
        "12/05/2026;Vivero A;18;432;6;8;4;9;4;3;2;17;1;",
        "15/05/2026;Vivero B;30;720;12;11;7;15;9;4;2;28;2;",
        "18/05/2026;Vivero B;22;528;8;9;5;11;6;3;2;20;2;trips",
        "20/05/2026;Vivero A;25;600;9;10;6;12;8;3;2;23;2;",
        "22/05/2026;Vivero B;28;672;10;11;7;14;8;4;2;26;2;",
        "25/05/2026;Vivero A;30;720;10;12;8;14;9;4;3;28;2;tarde soleada",
        "27/05/2026;Vivero B;24;576;9;10;5;12;7;3;2;22;2;",
        "29/05/2026;Vivero A;22;528;8;9;5;11;6;3;2;20;2;",
    ]

    archivo = open(ARCHIVO_COSECHAS, "w", encoding="utf-8")
    k = 0
    while k < len(datos_c):
        archivo.write(datos_c[k] + "\n")
        k = k + 1
    archivo.close()

    datos_i = [
        "05/01/2026;Vivero B;Plaga o enfermedad;Acaros en tallos;Medio;revisar",
        "10/02/2026;Vivero A;Daño clima/infraestructura;Granizo leve;Bajo;",
        "17/02/2026;Vivero B;Actividad no realizada;Fumigacion no realizada;Alto;reprogramar",
        "01/03/2026;Vivero A;Plaga o enfermedad;Pulgon en hojas;Medio;",
        "15/03/2026;Vivero B;Otra;Falta de personal;Bajo;",
        "06/04/2026;Vivero A;Daño clima/infraestructura;Viento fuerte;Medio;",
        "12/04/2026;Vivero B;Plaga o enfermedad;Mosca blanca;Alto;urgente",
        "18/05/2026;Vivero B;Plaga o enfermedad;Trips en Vivero B;Alto;revisar fumigacion",
    ]

    archivo = open(ARCHIVO_INCIDENCIAS, "w", encoding="utf-8")
    k = 0
    while k < len(datos_i):
        archivo.write(datos_i[k] + "\n")
        k = k + 1
    archivo.close()