animales = ["gato", "perro","loro","oso"]
numeros = [0,1,2,3]

#recocciendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    
#reociiendo la lista numeros:
for numero in numeros:
    resultado = numeros * 10
    print(resultado)
    
    
#iterando dos lista del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f'Recorriendo lista1: {numero}')
    print(f'recorriendo lista 2: {animal}')


#iterando segun parametros
for num in range(5,10):
    print(num)    
 
 
#forma no optima de recorrer una lista    
for num in range(len(numeros)):
    print(num)  

#forma correcta de recorrer una lista por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
    
#utilizando el for/else
for numero in numeros:
    print(f'ejecutando el ltimo vucle: acual: {numero}')
else:
    print("el bucle termino")
    
#todo lo anterior funciona exactamente igual para tuplas


#enumerar conjuntos
animales = {"gato", "perro","loro","oso"}
numeros = {0,1,2,3}


#forma correcta de recorrer una lista por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')


