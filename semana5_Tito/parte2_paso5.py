# Paso 7: Aplicar normalización al dataset de Tito
import pandas as pd
import re

def normalizar_texto(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^a-záéíóúüñ0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

df = pd.read_csv("dataset_tito_v1.csv", encoding="utf-8")

# Detectar automáticamente el nombre de la columna
columna = None
for col in ["texto", "pregunta", "preguntas", "Text"]:
    if col in df.columns:
        columna = col
        break
if columna is None:
    columna = df.columns[0]

df["texto_normalizado"] = df[columna].apply(normalizar_texto)
print(df[[columna, "texto_normalizado"]].head(10))