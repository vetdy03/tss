import pandas as pd
import numpy as np

# Generación de datos de prueba
np.random.seed(42)
n_samples = 500

data = {
    'num_creditos_vigentes': np.random.randint(1, 5, n_samples),
    'porcentaje_pago': np.random.uniform(50, 100, n_samples),
    'saldo_mora': np.random.uniform(0, 5000, n_samples),
    'dias_mora': np.random.randint(0, 120, n_samples),
    'antiguedad_credito': np.random.randint(1, 10, n_samples),
    'plazo_credito': np.random.randint(6, 60, n_samples),
    'num_microseguros': np.random.randint(0, 3, n_samples),
    'tasa_interes': np.random.uniform(5, 25, n_samples),
    'estado_ahorro': np.random.choice(["Activo", "Inactivo"], n_samples),
    'saldo_ahorro': np.random.uniform(0, 10000, n_samples),
    'edad': np.random.randint(18, 65, n_samples),
    'estado_civil': np.random.choice(["Soltero", "Casado", "Divorciado"], n_samples),
    'estrato': np.random.randint(1, 6, n_samples),
    'segmento': np.random.choice(["Alto", "Medio", "Bajo"], n_samples),
    'desercion': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])  # Desbalance de clases
}

df = pd.DataFrame(data)

# Guardar los datos en un archivo Excel
df.to_excel("datos_credito.xlsx", index=False)

print("📂 Archivo 'datos_credito.xlsx' generado exitosamente.")
