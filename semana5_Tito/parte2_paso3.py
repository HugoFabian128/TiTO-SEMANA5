# Paso 5: Función de normalización con expresiones regulares
import re

def normalizar_texto(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^a-záéíóúüñ0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

frase = " ¿DÓNDE Está la Biblioteca? "
print("Texto normalizado:", normalizar_texto(frase))