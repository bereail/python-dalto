import re

#la cadena en la que se busca los patrones
text = "la fecha es 12/06/01 y el telefono es -1-555-55555"

#el patron a buscar
pattern = r"\d{2}/\d{2}/\{4}"

#el texto con el que se reemplazara le patron
replacement = "fecha oculta"

#reemplazar todas las apariciones dle patron en la cadema de textp
new_txt = re.sub(pattern, replacement, text)

#imprimir resultado
print("texto modificado", new_txt)