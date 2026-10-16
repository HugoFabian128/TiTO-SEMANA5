import os
import shutil

# Ruta del dataset original (asumiendo que está en la raíz de semana5_tito)
origen = "../dataset_tito_v1.csv"
destino = "../dataset_tito_v1_backup.csv"

if os.path.exists(origen):
    shutil.copy(origen, destino)
    print(" Archivo dataset_tito_v1.csv localizado.")
    print(" Copia de respaldo creada como 'dataset_tito_v1_backup.csv'.")
else:
    print(" Archivo dataset_tito_v1.csv no encontrado en el directorio raíz.")