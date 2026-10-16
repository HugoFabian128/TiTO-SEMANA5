import re

def normalizar_texto(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^a-záéíóúüñ0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

frase = "¿Dónde está la biblioteca?"
limpio = normalizar_texto(frase)
tokens = limpio.split()

print("Original:", frase)
print("Limpio:", limpio)
print("Tokens limpios:", tokens)