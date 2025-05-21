import random
import pandas as pd

# Configuración inicial
partidos = ["MAS", "CC", "Creemos", "FPV", "PDC"]
departamentos = ["La Paz", "Cochabamba", "Santa Cruz", "Oruro", "Potosí", "Chuquisaca", "Tarija", "Beni", "Pando"]

# Simular votos por partido en cada departamento
def simular_votos():
    resultados = []
    for dpto in departamentos:
        votos_totales = random.randint(50000, 200000)
        porcentajes = [random.uniform(5, 40) for _ in partidos]
        suma = sum(porcentajes)
        porcentajes = [p * 100 / suma for p in porcentajes]
        votos = [int(votos_totales * p / 100) for p in porcentajes]
        resultados.append(dict(Departamento=dpto, **dict(zip(partidos, votos))))
    return pd.DataFrame(resultados)

# Sumar resultados totales por partido
def computar_totales(df):
    totales = df[partidos].sum().sort_values(ascending=False)
    return totales

# Verificar si hay ganador en primera vuelta
def verificar_primera_vuelta(totales):
    total_votos = totales.sum()
    porcentajes = totales / total_votos * 100
    primero, segundo = porcentajes.index[0], porcentajes.index[1]
    if porcentajes[primero] >= 50:
        return f"Gana {primero} con mayoría absoluta ({porcentajes[primero]:.2f}%)", None
    elif porcentajes[primero] >= 40 and (porcentajes[primero] - porcentajes[segundo]) >= 10:
        return f"Gana {primero} con mayoría relativa ({porcentajes[primero]:.2f}%) y 10%+ sobre {secondo}", None
    else:
        return None, (primero, segundo)

# Simular segunda vuelta
def segunda_vuelta(df, primero, segundo):
    resultados_segunda = []
    for dpto in departamentos:
        votos_totales = random.randint(50000, 200000)
        porcentaje_primero = random.uniform(45, 55)
        porcentaje_segundo = 100 - porcentaje_primero
        votos_primero = int(votos_totales * porcentaje_primero / 100)
        votos_segundo = votos_totales - votos_primero
        resultados_segunda.append({
            "Departamento": dpto,
            primero: votos_primero,
            segundo: votos_segundo
        })
    df2 = pd.DataFrame(resultados_segunda)
    totales2 = df2[[primero, segundo]].sum()
    ganador = totales2.idxmax()
    porcentaje = totales2[ganador] / totales2.sum() * 100
    return f"Gana {ganador} en segunda vuelta con {porcentaje:.2f}%"

# Ejecutar simulación completa
df_votos = simular_votos()
totales = computar_totales(df_votos)
resultado, segunda = verificar_primera_vuelta(totales)

if resultado:
    resultado_final = resultado
else:
    resultado_final = segunda_vuelta(df_votos, *segunda)

df_votos, totales, resultado_final

# Guardar resultados en Excel
from openpyxl import Workbook

# Crear un archivo Excel con dos hojas: resultados por departamento y totales
ruta_excel = "/mnt/data/resultados_elecciones.xlsx"

with pd.ExcelWriter(ruta_excel, engine='openpyxl') as writer:
    df_votos.to_excel(writer, sheet_name="Votos por Departamento", index=False)
    totales_df = totales.reset_index()
    totales_df.columns = ['Partido', 'Total Votos']
    totales_df.to_excel(writer, sheet_name="Totales Generales", index=False)

ruta_excel
