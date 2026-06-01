ARCHIVO_COSECHAS = "cosechas.txt"
ARCHIVO_INCIDENCIAS = "incidencias.txt"

# Listas de cosechas
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
obs_c = []

# Listas de incidencias
fechas_i = []
viveros_i = []
tipos_i = []
detalles_i = []
impactos_i = []
obs_i = []

def cargar_cosechas():
    try:
        archivo = open(ARCHIVO_COSECHAS, "r")

        for linea in archivo:
            datos = linea.strip().split(";")

            fechas_c.append(datos[0])
            viveros_c.append(datos[1])
            bonches_c.append(int(datos[2]))
            rosas_c.append(int(datos[3]))
            m50_c.append(int(datos[4]))
            m60_c.append(int(datos[5]))
            m70_c.append(int(datos[6]))
            rojo_c.append(int(datos[7]))
            rosado_c.append(int(datos[8]))
            blanco_c.append(int(datos[9]))
            amarillo_c.append(int(datos[10]))
            cal_a_c.append(int(datos[11]))
            cal_b_c.append(int(datos[12]))
            obs_c.append(datos[13])

        archivo.close()

    except:
        print("No existe archivo de cosechas.")

def guardar_cosechas():
    archivo = open(ARCHIVO_COSECHAS, "w")

    for i in range(len(fechas_c)):
        linea = (
            fechas_c[i] + ";" +
            viveros_c[i] + ";" +
            str(bonches_c[i]) + ";" +
            str(rosas_c[i]) + ";" +
            str(m50_c[i]) + ";" +
            str(m60_c[i]) + ";" +
            str(m70_c[i]) + ";" +
            str(rojo_c[i]) + ";" +
            str(rosado_c[i]) + ";" +
            str(blanco_c[i]) + ";" +
            str(amarillo_c[i]) + ";" +
            str(cal_a_c[i]) + ";" +
            str(cal_b_c[i]) + ";" +
            obs_c[i] + "\n"
        )

        archivo.write(linea)

    archivo.close()

def cargar_incidencias():
    try:
        archivo = open(ARCHIVO_INCIDENCIAS, "r")

        for linea in archivo:
            datos = linea.strip().split(";")

            fechas_i.append(datos[0])
            viveros_i.append(datos[1])
            tipos_i.append(datos[2])
            detalles_i.append(datos[3])
            impactos_i.append(datos[4])
            obs_i.append(datos[5])

        archivo.close()

    except:
        print("No existe archivo de incidencias.")

def guardar_incidencias():
    archivo = open(ARCHIVO_INCIDENCIAS, "w")

    for i in range(len(fechas_i)):
        linea = (
            fechas_i[i] + ";" +
            viveros_i[i] + ";" +
            tipos_i[i] + ";" +
            detalles_i[i] + ";" +
            impactos_i[i] + ";" +
            obs_i[i] + "\n"
        )

        archivo.write(linea)

    archivo.close()  

def generar_datos_prueba():

    if len(fechas_c) == 0:

        for i in range(52):
            fechas_c.append("01/01/2026")
            viveros_c.append("Vivero A")
            bonches_c.append(100)
            rosas_c.append(3000)
            m50_c.append(30)
            m60_c.append(40)
            m70_c.append(30)
            rojo_c.append(1000)
            rosado_c.append(700)
            blanco_c.append(800)
            amarillo_c.append(500)
            cal_a_c.append(90)
            cal_b_c.append(10)
            obs_c.append("Registro prueba")

    if len(fechas_i) == 0:

        for i in range(8):
            fechas_i.append("01/01/2026")
            viveros_i.append("Vivero A")
            tipos_i.append("Plagas")
            detalles_i.append("Pulgones")
            impactos_i.append("Alto")
            obs_i.append("Sin observación")  