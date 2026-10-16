import re

# Paso 3 y 5: Función para limpiar/normalizar
def normalizar_texto(texto):
    texto = str(texto).lower() # Pasa a minúsculas
    texto = re.sub(r"[^a-záéíóúüñ0-9\s]", " ", texto) # Quita signos de puntuación
    texto = re.sub(r"\s+", " ", texto).strip() # Quita espacios sobrantes
    return texto

# Paso 6: Prueba con una frase
frase = "¿Dónde está la biblioteca?"
limpio = normalizar_texto(frase)
tokens = limpio.split() # Separa la frase en una lista de palabras

print("Original:", frase)
print("Limpio:", limpio)
print("Tokens:", tokens)