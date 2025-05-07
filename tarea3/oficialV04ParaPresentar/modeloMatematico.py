import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargar los datos desde el archivo Excel
df = pd.read_excel("datos_credito.xlsx")

# Preprocesamiento de datos
le = LabelEncoder()
for col in ['estado_ahorro', 'estado_civil', 'segmento']:
    df[col] = le.fit_transform(df[col])

scaler = StandardScaler()
X = df.drop(columns=['desercion'])
y = df['desercion']
X_scaled = scaler.fit_transform(X)

# Aplicar SMOTE para balancear clases
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

# División de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Entrenar el modelo (Random Forest)
model = RandomForestClassifier(class_weight="balanced", random_state=42, n_estimators=100)
model.fit(X_train, y_train)

# Evaluación del modelo
y_pred = model.predict(X_test)
print("🔍 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Matriz de confusión:\n", confusion_matrix(y_test, y_pred))
print("\n📑 Reporte de clasificación:\n", classification_report(y_test, y_pred))

# Visualización de la distribución de clases
plt.figure(figsize=(10, 5))
sns.countplot(x='desercion', data=df)
plt.title("Distribución de clientes que desertan (1) vs. los que permanecen (0)")
plt.show()
