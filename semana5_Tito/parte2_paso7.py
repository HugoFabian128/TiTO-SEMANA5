# Paso 9: Guardar el dataset resultante (dataset_tito_semana5.csv)
import pandas as pd
import re

def normalizar_texto(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^a-záéíóúüñ0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

df = pd.read_csv("dataset_tito_v1.csv", encoding="utf-8")

columna = None
for col in ["texto", "pregunta", "preguntas", "Text"]:
    if col in df.columns:
        columna = col
        break
if columna is None:
    columna = df.columns[0]

df["texto_normalizado"] = df[columna].apply(normalizar_texto)
df["tokens"] = df["texto_normalizado"].apply(lambda texto: " | ".join(texto.split()))

# Guarda el archivo dataset_tito_semana5.csv indicado en la pizarra
df.to_csv("dataset_tito_semana5.csv", index=False, encoding="utf-8-sig")
print("¡Archivo 'dataset_tito_semana5.csv' guardado con éxito!")