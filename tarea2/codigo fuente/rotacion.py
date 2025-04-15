import pandas as pd

# Contenedor en metros
contenedor_ancho = 1.20
contenedor_largo = 2.50

# Lista de piezas
piezas = [
    {"pieza": 1, "ancho": 0.50, "largo": 1.00},
    {"pieza": 2, "ancho": 0.80, "largo": 0.60},
    {"pieza": 3, "ancho": 0.30, "largo": 1.50},
    {"pieza": 4, "ancho": 0.70, "largo": 0.90},
    {"pieza": 5, "ancho": 0.40, "largo": 0.70},
    {"pieza": 6, "ancho": 0.60, "largo": 0.50},
    {"pieza": 7, "ancho": 0.90, "largo": 0.40},
    {"pieza": 8, "ancho": 0.20, "largo": 2.00},
]

ubicaciones = []
x_actual = 0
y_actual = 0
altura_fila_actual = 0

def cabe(ancho, largo, x, y):
    return x + ancho <= contenedor_ancho and y + largo <= contenedor_largo

for p in piezas:
    ancho = p["ancho"]
    largo = p["largo"]
    rotada = False

    if cabe(ancho, largo, x_actual, y_actual):
        pass
    elif cabe(largo, ancho, x_actual, y_actual):
        ancho, largo = largo, ancho
        rotada = True
    else:
        x_actual = 0
        y_actual += altura_fila_actual
        altura_fila_actual = 0
        if cabe(ancho, largo, x_actual, y_actual):
            pass
        elif cabe(largo, ancho, x_actual, y_actual):
            ancho, largo = largo, ancho
            rotada = True
        else:
            ubicaciones.append({
                "pieza": p["pieza"], "x": None, "y": None,
                "ancho": p["ancho"], "largo": p["largo"],
                "rotada": False
            })
            continue

    ubicaciones.append({
        "pieza": p["pieza"],
        "x": x_actual,
        "y": y_actual,
        "ancho": ancho,
        "largo": largo,
        "rotada": rotada
    })
    altura_fila_actual = max(altura_fila_actual, largo)
    x_actual += ancho

# Guardar a Excel
df = pd.DataFrame(ubicaciones)
df.to_excel("acomodo_con_rotacion.xlsx", index=False)
print("Archivo generado: acomodo_con_rotacion.xlsx")
