import pandas as pd

try:
    df = pd.read_csv("../dataset_tito_v1.csv", encoding="utf-8")
    print(" Dataset cargado con éxito.")
    print(f"Columnas detectadas: {list(df.columns)}")
    print(f"Total de registros: {len(df)}")
except Exception as e:
    print(f" Error al leer el archivo: {e}")