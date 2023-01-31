#creando las listas
frutas = ['banana','manzana','pera','granada']
letras = "hola berenice"
numeros = [1,3,5,0,8]

#exceptuando datos en la iteracion
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f'me voy a comer una {fruta}')
    
#evitar que el bucle siga ejecutandose (cuando se encuentra un break el else no se ejecuta)
for fruta in frutas:
    print(f'me voty a comer una: {fruta}')
    if fruta == 'banana':
        break
else:
    print("terminado")    
    
#recorrer cadebna de texto
for letra in letras:
    print(letra)
    
#for en un sola liena de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)