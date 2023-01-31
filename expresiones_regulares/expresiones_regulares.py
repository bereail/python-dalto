import re

texto = '''hola maestro, esta es la cadena uno
esta es la  2 segunda linea de texto,
esta e sla tercvera 3'''
 
resultado = re.search("hola",texto)

#busca todos los "holas" -> haciendo una busqueda simple
resultado = re.findall("hola", texto)

#\d - busca digitos numericos del 0 -9
resultado = re.findall(r"\d",texto)

#\D - busca todo menos digitos numericos del 0 -9
resultado = re.findall(r"\D",texto)


#\w busca caracteres alfanumerico (a-z , A-Z, 0-9, _)
resultado = re.findall(r"\w", texto)

#\w busca todo menos caracteres alfanumerico (a-z , A-Z, 0-9, _)
resultado = re.findall(r"\W", texto)


#\s busca espacios en blanco -> espacios comunes, tabs, saltos de linea
resultado = re.findall(r"\s",texto)

#\s busca todo menosespacios en blanco -> espacios comunes, tabs, saltos de linea
resultado = re.findall(r"\S", texto)

#.-> busca todos menos los saltos de linea
resultado = re.findall(r"\.", texto)

#\n -> busca saltos en lines
resultado = re.findall(r"\n", texto)

#\ -> cancelamso caracteres especiales
resultado = re.findall(r"\.", texto)

#armando una cadena q bsuque un numero seguido d unpunto y un espacio en linea
resultado = re.findall(r"\d\.\s", texto)

#buscando hola al principo de la line
resultado = re.findall(r"^hola",texto, flags=re.IGNORECASE) #-> ignora mayus y min
resultado = re.findall(r"^hola",texto,flags=re.M)#->resultado multilinea

#$ -> busca el final d euna linea
resultado = re.findall(f"$hola", texto, flags=re.M)

#(n) -> bsuca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}',texto) #->encontrar una cadena con 3 diguitos juntos

#{n,m} -> almenos n como maximo m
resultado = re.findall(r'{ab}{2,4}',texto)

# simbolo ! or aca no me sale -> busca una cosa o la otra
resultado = re.findall(r'!{2,4}',texto)

print(resultado) 