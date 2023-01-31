#creando funciones que nos devuelva numero primmos
#entre el 0 y el argumento que pasamos

#crear un funcion que verifica si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no puede dividirse por dos y por el mismo numero
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y terminamos el bucle
        if num%i==0: return False
    return True
    
#creando funcion que retorne un lista con todos los primos   
def primos_hasta(num):
    #creando la lista
    primos = []
    for i in range(3, num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        #devolvemos la lista
    return primos

#creamos el resultado llamando la funcon y lo mostramos
resultado = primos_hasta(13)
print(resultado)

#numeros primos funcion lambda
primos_hasta_lambda = lambda num: list(filter(lambda x: all(x % i !=0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))

print(primos_hasta_lambda(25))