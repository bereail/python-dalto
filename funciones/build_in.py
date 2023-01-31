numeros = [4,7,2,42,15]

#encontrando el numero mayor d euna lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales -> el segundo valor es la cantidad de decimales que queres dejar
numero = round(12.123456, 2)
print(numero)

#retorna False -> 0, vario, False, ninguno
#distinto a 0, True, cadena, datos no vacios
resultado = bool(0)
print(resultado)


#retorna True, si todos los valores son verdaderos -> 
#es decir, si no hay elementos vacios
resultado_all = all([1,"true",[123,465]])
print(resultado_all)


#suma todos los valores que tiene un iterable
suma = sum(numeros)
print(suma)