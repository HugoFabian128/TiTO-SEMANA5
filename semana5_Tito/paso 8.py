import pandas as pd
import re

# 1. Función de normalización
def normalizar_texto(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^a-záéíóúüñ0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

# 2. Cargar el dataset original
df = pd.read_csv("dataset_tito_v1.csv", encoding="utf-8")

# 3. Detectar automáticamente el nombre de la columna
posibles_columnas = ["texto", "pregunta", "preguntas", "Text", "Question", "intent"]
columna_origen = None

for col in posibles_columnas:
    if col in df.columns:
        columna_origen = col
        break

# Si no coincide con ninguna de la lista, toma la primera columna disponible del CSV
if columna_origen is None:
    columna_origen = df.columns[0]

print(f"Columna detectada para procesar: '{columna_origen}'")

# 4. Crear columna de texto normalizado y columna de tokens
df["texto_normalizado"] = df[columna_origen].apply(normalizar_texto)
df["tokens"] = df["texto_normalizado"].apply(lambda texto: " | ".join(texto.split()))

# 5. Mostrar en pantalla los primeros 5 resultados (para la captura del entregable)
print("\n--- MUESTRA DEL RESULTADO FINAL ---")
print(df[[columna_origen, "texto_normalizado", "tokens"]].head(5))

# 6. Guardar en un nuevo archivo CSV
df.to_csv("dataset_tito_semana5_parte1.csv", index=False, encoding="utf-8-sig")

print("\n ¡Archivo 'dataset_tito_semana5_parte1.csv' guardado exitosamente!")