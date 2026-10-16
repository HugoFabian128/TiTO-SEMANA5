from collections import Counter
import pandas as pd

# 1. Cargar el dataset procesado
df = pd.read_csv("dataset_tito_semana5.csv", encoding="utf-8")

# 2. Unir todas las frases normalizadas en una sola lista de tokens
todos_los_tokens = []
for texto in df["texto_normalizado"]:
    todos_los_tokens.extend(str(texto).split())

# 3. Contar la frecuencia de cada palabra
conteo = Counter(todos_los_tokens)

print("--- LAS 15 PALABRAS MÁS FRECUENTES ---")
for palabra, frecuencia in conteo.most_common(15):
    print(f"{palabra}: {frecuencia} veces")