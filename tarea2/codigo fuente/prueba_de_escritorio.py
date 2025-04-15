# Intentamos colocar piezas permitiendo rotación si es necesario
ubicaciones_con_rotacion = []
x_actual = 0
y_actual = 0
altura_fila_actual = 0

for p in piezas:
    ancho = p["ancho"]
    largo = p["largo"]
    rotada = False

    def cabe(ancho_, largo_, x_, y_):
        return (x_ + ancho_ <= contenedor_ancho) and (y_ + largo_ <= contenedor_largo)

    # Primero, intentamos sin rotación
    if cabe(ancho, largo, x_actual, y_actual):
        ubicaciones_con_rotacion.append({
            "pieza": p["pieza"],
            "x": x_actual,
            "y": y_actual,
            "ancho": ancho,
            "largo": largo,
            "rotada": rotada
        })
        altura_fila_actual = max(altura_fila_actual, largo)
        x_actual += ancho
        continue

    # Intentamos rotar
    if cabe(largo, ancho, x_actual, y_actual):
        rotada = True
        ancho, largo = largo, ancho
        ubicaciones_con_rotacion.append({
            "pieza": p["pieza"],
            "x": x_actual,
            "y": y_actual,
            "ancho": ancho,
            "largo": largo,
            "rotada": rotada
        })
        altura_fila_actual = max(altura_fila_actual, largo)
        x_actual += ancho
        continue

    # Nueva fila
    x_actual = 0
    y_actual += altura_fila_actual
    altura_fila_actual = largo

    if cabe(ancho, largo, x_actual, y_actual):
        ubicaciones_con_rotacion.append({
            "pieza": p["pieza"],
            "x": x_actual,
            "y": y_actual,
            "ancho": ancho,
            "largo": largo,
            "rotada": rotada
        })
        x_actual += ancho
    elif cabe(largo, ancho, x_actual, y_actual):
        rotada = True
        ancho, largo = largo, ancho
        ubicaciones_con_rotacion.append({
            "pieza": p["pieza"],
            "x": x_actual,
            "y": y_actual,
            "ancho": ancho,
            "largo": largo,
            "rotada": rotada
        })
        x_actual += ancho
    else:
        # No cabe ni rotada ni normal
        ubicaciones_con_rotacion.append({
            "pieza": p["pieza"],
            "x": None,
            "y": None,
            "ancho": p["ancho"],
            "largo": p["largo"],
            "rotada": False
        })

# Exportamos a Excel
df_rotacion = pd.DataFrame(ubicaciones_con_rotacion)
output_rotado = "acomodo_con_rotacion.xlsx"
df_rotacion.to_excel(output_rotado, index=False)

df_rotacion
