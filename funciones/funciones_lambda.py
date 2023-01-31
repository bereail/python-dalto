numeros = [1,2,3,4,5,6,7,8]

#creando un funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

#usando  filter con una funcion comun que sdiga si e spar o no
def es_par(num):
    if(num%2==0):
        return True
    
#usando filter con uan funcion comun
#numeros_pares = filter(es_par, numeros)   

#creando lo mismo que antes pero con lamda
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))