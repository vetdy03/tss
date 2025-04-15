# Re-importamos las librerías después del reinicio del entorno
import pandas as pd

# Definimos las dimensiones del contenedor
contenedor_ancho = 1.20
contenedor_largo = 2.50

# Lista de piezas con su ancho, largo y área (sin rotación inicialmente)
piezas = [
    {"pieza": 1, "ancho": 0.50, "largo": 1.00, "area": 0.50},
    {"pieza": 2, "ancho": 0.80, "largo": 0.60, "area": 0.48},
    {"pieza": 3, "ancho": 0.30, "largo": 1.50, "area": 0.45},
    {"pieza": 4, "ancho": 0.70, "largo": 0.90, "area": 0.63},
    {"pieza": 5, "ancho": 0.40, "largo": 0.70, "area": 0.28},
    {"pieza": 6, "ancho": 0.60, "largo": 0.50, "area": 0.30},
    {"pieza": 7, "ancho": 0.90, "largo": 0.40, "area": 0.36},
    {"pieza": 8, "ancho": 0.20, "largo": 2.00, "area": 0.40},
]

# Inicializamos variables para el acomodo sin rotación
ubicaciones = []
x_actual = 0
y_actual = 0
altura_fila_actual = 0

# Intentamos colocar las piezas una por una (sin rotación)
for p in piezas:
    ancho = p["ancho"]
    largo = p["largo"]

    if x_actual + ancho <= contenedor_ancho:
        ubicaciones.append({
            "pieza": p["pieza"],
            "x": x_actual,
            "y": y_actual,
            "ancho": ancho,
            "largo": largo,
            "rotada": False
        })
        altura_fila_actual = max(altura_fila_actual, largo)
        x_actual += ancho
    else:
        # Mover a nueva fila
        x_actual = 0
        y_actual += altura_fila_actual
        altura_fila_actual = largo

        # Verificamos si cabe en la nueva fila
        if y_actual + largo <= contenedor_largo:
            ubicaciones.append({
                "pieza": p["pieza"],
                "x": x_actual,
                "y": y_actual,
                "ancho": ancho,
                "largo": largo,
                "rotada": False
            })
            x_actual += ancho
        else:
            # No cabe en el contenedor
            ubicaciones.append({
                "pieza": p["pieza"],
                "x": None,
                "y": None,
                "ancho": ancho,
                "largo": largo,
                "rotada": False
            })

# Creamos DataFrame con los resultados
df_ubicaciones = pd.DataFrame(ubicaciones)
df_ubicaciones


# Guardar en archivo Excel
output_path = "/mnt/data/acomodo_sin_rotacion.xlsx"
df_ubicaciones.to_excel(output_path, index=False)
output_path = "acomodo_sin_rotacion.xlsx"

