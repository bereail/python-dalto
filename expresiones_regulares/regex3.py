import re

text = "reemplazando las vocales por asteriscos "

new_text = re.sub("[aeiou]", "", text)

print(new_text)