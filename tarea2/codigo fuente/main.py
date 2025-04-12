import pandas as pd

# Dimensiones de la plancha
ANCHO_PLANCHA = 100
ALTO_PLANCHA = 100

# Piezas a cortar: (Nombre, Ancho, Alto)
piezas = [
    ("A", 30, 20),
    ("B", 50, 30),
    ("C", 20, 10),
    ("D", 40, 25),
    ("E", 10, 10),
    ("F", 15, 20),
    ("G", 45, 30)
]

# Ordenar piezas de mayor a menor área
piezas.sort(key=lambda x: x[1] * x[2], reverse=True)

# Coordenadas donde se colocarán las piezas
colocaciones = []

x_cursor = 0
y_cursor = 0
fila_max_alto = 0

for nombre, ancho, alto in piezas:
    if x_cursor + ancho <= ANCHO_PLANCHA and y_cursor + alto <= ALTO_PLANCHA:
        colocaciones.append((nombre, ancho, alto, x_cursor, y_cursor))
        x_cursor += ancho
        fila_max_alto = max(fila_max_alto, alto)
    else:
        # Intentamos una nueva fila
        x_cursor = 0
        y_cursor += fila_max_alto
        fila_max_alto = alto
        if y_cursor + alto <= ALTO_PLANCHA:
            colocaciones.append((nombre, ancho, alto, x_cursor, y_cursor))
            x_cursor += ancho
        else:
            print(f"Pieza {nombre} no cabe en la plancha y fue descartada.")

# Mostrar en consola
print("Resultado de colocación de piezas:\n")
for nombre, ancho, alto, x, y in colocaciones:
    print(f"Pieza {nombre}: {ancho}x{alto} en posición ({x}, {y})")

# Exportar a Excel
df = pd.DataFrame(colocaciones, columns=["Pieza", "Ancho", "Alto", "X", "Y"])
df.to_excel("output.xlsx", index=False)
print("\nArchivo 'output.xlsx' generado con éxito.")
