# ECOFLOR – Sistema de Gestión de Cosechas e Incidencias

**Curso:** CIIN1205P – Fundamentos de Programación
**Universidad:** Universidad Privada del Norte – Cajamarca
**Docente:** Pereda Cabanillas, Edwuard Jhonatan
**Equipo:**
- Cabrera Sanchez, Rodrigo Alejandro
- Lezcano Moreno, Mariana Jasmín
- Sánchez Hernández, Hilter Alexis
- Sandoval Villanueva, Becsy Yomar
- Yopla Huamán, Ana Elizabeth

---

## Requisitos

- Python 3.8 o superior
- No requiere librerías externas (solo `datetime` de la librería estándar)

---

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `ecoflor.py` | Menú principal y las 5 opciones del sistema |
| `validaciones.py` | Funciones de entrada y validación de datos |
| `datos.py` | Listas paralelas y lectura/escritura de archivos |
| `busqueda.py` | Filtrado, búsqueda lineal y ordenamiento burbuja |
| `cosechas.txt` | Registros de cosechas (56 registros simulados) |
| `incidencias.txt` | Registros de incidencias (52 registros simulados) |

Colocar los seis archivos en la misma carpeta y ejecutar:

```
python ecoflor.py
```

---

## Menú

| Opción | Descripción |
|---|---|
| 1 | Registrar cosecha |
| 2 | Ver historial de cosechas |
| 3 | Registrar incidencia |
| 4 | Ver incidencias |
| 5 | Análisis integral |
| 6 | Salir |

En cualquier paso del registro: opción `0` vuelve al menú sin guardar.

---

## Modelo de datos — cosechas

Una cosecha se registra por vivero (no "ambos"). El total de bonches se divide en
**Clase A** (vendible, ~95%) y **Clase B** (con defecto, ~5%); además puede haber
**rosas sueltas** (flores individuales que no formaron bonche, siempre clase B).

Cada uno de estos tres grupos (Clase A, Clase B, Sueltas) se registra con su
propia distribución de **medida de tallo** y **color**:

- **Clase A** (bonches vendibles): medida en 3 grupos — 50 cm / 60 cm / 70-80-90 cm
  (nunca tiene tallos menores a 50 cm).
- **Clase B** (bonches con defecto) y **Sueltas**: medida en 4 grupos — menor de
  50 cm / 50 cm / 60 cm / 70-80-90 cm.
- Los tres grupos usan los mismos 4 colores: rojo / blanco / rosado / amarillo.

Cada registro tiene 30 campos separados por `;`:

```
fecha ; vivero ; bonches ; cal_a ; cal_b ; rosas_sueltas ;
a50 ; a60 ; a7090 ; a_rojo ; a_blanco ; a_rosado ; a_amarillo ;
b_men50 ; b50 ; b60 ; b7090 ; b_rojo ; b_blanco ; b_rosado ; b_amarillo ;
s_men50 ; s50 ; s60 ; s7090 ; s_rojo ; s_blanco ; s_rosado ; s_amarillo ;
obs
```

| Campo | Descripción |
|---|---|
| `bonches` | Total de bonches cosechados (0–150) |
| `cal_a` / `cal_b` | Bonches Clase A / Clase B (suman = bonches) |
| `rosas_sueltas` | Total de rosas sueltas cosechadas (0 si no hay) |
| `a50/a60/a7090` | Medida de Clase A (suman = cal_a) |
| `a_rojo/a_blanco/a_rosado/a_amarillo` | Color de Clase A (suman = cal_a) |
| `b_men50/b50/b60/b7090` | Medida de Clase B (suman = cal_b) |
| `b_rojo/.../b_amarillo` | Color de Clase B (suman = cal_b) |
| `s_men50/s50/s60/s7090` | Medida de rosas sueltas (suman = rosas_sueltas) |
| `s_rojo/.../s_amarillo` | Color de rosas sueltas (suman = rosas_sueltas) |
| `obs` | Observación libre (opcional) |

**Distribuciones de referencia** usadas para generar los datos de ejemplo:
Clase A/B ≈ 95% / 5% del total de bonches (dentro de Clase B, lo que no llega a
formar un bonche completo se registra como rosas sueltas). Sobre el total de
producción: ≈ 40% rojo-60cm, 35% blanco-70/80/90cm, 22% rosado-50cm y 3%
amarillo-menor de 50cm. El grupo "menor de 50cm" solo aplica a Clase B y
Sueltas (Clase A nunca tiene tallos menores a 50cm) y **no debe quedar en 0**:
representa ese 3% del total y concentra la mayoría de Clase B.

---

## Modelo de datos — incidencias

Cada registro tiene 6 campos separados por `;`:

```
fecha ; vivero ; tipo ; detalle ; impacto ; obs
```

| Campo | Valores posibles |
|---|---|
| `tipo` | `Plaga o enfermedad` / `Daño clima/infraestructura` / `Actividad no realizada` / `Otra: <descripción>` |
| `impacto` | `Bajo` / `Medio` / `Alto` |
| `obs` | Observación opcional |

---
## Control de versiones

Repositorio Git con historial de commits por avance del proyecto.

**Repositorio:** https://github.com/RodrigoCabrera534/Proyecto-ECOFLOR
