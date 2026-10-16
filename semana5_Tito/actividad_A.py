import re

texto_prueba = "¡Hola! El chatbot Tito responde 24/7 en https://tito.edu.mx. ¿Dudas? Escríbenos a contacto@tito.edu.mx."

print("--- TEXTO ORIGINAL ---")
print(texto_prueba)

# 1. Eliminar solo enlaces y correos
sin_urls = re.sub(r"https?://\S+|www\.\S+|\S+@\S+", "", texto_prueba)
print("\n--- SIN URLS NI CORREOS ---")
print(sin_urls)

# 2. Conservar solo letras y espacios (elimina números y puntuación)
solo_letras = re.sub(r"[^a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]", "", texto_prueba)
print("\n--- SOLO LETRAS ---")
print(solo_letras)

# 3. Conservar letras, números y espacios
letras_y_numeros = re.sub(r"[^a-zA-ZáéíóúüñÁÉÍÓÚÜÑ0-9\s]", "", texto_prueba)
print("\n--- LETRAS Y NÚMEROS ---")
print(letras_y_numeros)