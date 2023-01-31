#creando una funcion de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'


frase_resultante = frase("bere","solo","kpa")
print(frase_resultante)

#forzando argumento -> utlkizando keyword
frase_resultante = frase(adjetivo="kpa",apellido="solo",nombre="bere")
print(frase_resultante)