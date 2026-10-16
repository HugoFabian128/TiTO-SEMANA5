import pandas as pd
import re

def normalizar_texto(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^a-záéíóúüñ0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

# 1. Cargar el CSV
df = pd.read_csv("dataset_tito_v1.csv", encoding="utf-8")

# Mostrar en pantalla las columnas encontradas
print("Columnas en tu archivo CSV:", list(df.columns))

# 2. Buscar la columna correcta entre las opciones más habituales
posibles_columnas = ["texto", "pregunta", "preguntas", "Text", "Question", "intent"]
columna_origen = None

for col in posibles_columnas:
    if col in df.columns:
        columna_origen = col
        break

# Si no encuentra ninguna de las conocidas, toma la primera columna del CSV
if columna_origen is None:
    columna_origen = df.columns[0]

print(f"Usando la columna: '{columna_origen}'")

# 3. Aplicar normalización
df["texto_normalizado"] = df[columna_origen].apply(normalizar_texto)

print("\n--- PRIMEROS 10 REGISTROS ---")
print(df[[columna_origen, "texto_normalizado"]].head(10))