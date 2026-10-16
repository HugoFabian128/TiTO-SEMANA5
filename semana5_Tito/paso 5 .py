import re

def normalizar_texto(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^a-záéíóúüñ0-9\s]", " ", texto) # Mantiene letras, acentos, ñ y números
    texto = re.sub(r"\s+", " ", texto).strip()        # Limpia espacios extra
    return texto

frase = " ¿DÓNDE Está la Biblioteca? "
print("Frase con ruido:", frase)
print("Frase normalizada:", normalizar_texto(frase))