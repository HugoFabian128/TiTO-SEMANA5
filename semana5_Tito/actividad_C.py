import pandas as pd

# 1. Cargar el dataset procesado
df = pd.read_csv("dataset_tito_semana5.csv", encoding="utf-8")

# Detectar automáticamente cuál es la columna original de texto/pregunta
columna_origen = None
for col in ["texto", "pregunta", "preguntas", "Text", "Question"]:
    if col in df.columns:
        columna_origen = col
        break

# Si no encuentra ninguna de las conocidas, usa la primera columna que no sea de procesamiento
if columna_origen is None:
    columnas_disponibles = [c for c in df.columns if c not in ["texto_normalizado", "tokens"]]
    columna_origen = columnas_disponibles[0] if columnas_disponibles else df.columns[0]

print(f"Usando columna original: '{columna_origen}'\n")

# 2. Función para buscar preguntas por palabra clave
def buscar_por_palabra(palabra_clave):
    palabra_clave = palabra_clave.lower()
    print(f"--- BÚSQUEDA DE PREGUNTAS QUE CONTIENEN: '{palabra_clave}' ---")

    # Filtrar en la columna de tokens
    resultados = df[
        df["tokens"].str.contains(palabra_clave, case=False, na=False)
    ]

    if not resultados.empty:
        for idx, row in resultados.iterrows():
            print(f"- Original: {row[columna_origen]}")
            print(f"  Tokens:   {row['tokens']}\n")
    else:
        print("No se encontraron coincidencias.\n")

# 3. Pruebas de búsqueda
buscar_por_palabra("beca")
buscar_por_palabra("horario")