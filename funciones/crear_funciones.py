#creando una funcion simple
#def saludar():
#    print("hola bere")

#ejecutando la funcion simple
#saludar()


#creando funcion con parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "kpa"
    elif (sexo == "hombre"):
        adjetivo = "kpo"
    else:
        adjetivo = 'baby'
        
    print(f'Hola {nombre}, mi {adjetivo} como andas?')
    
saludar("bere","Mujer")

#crear un funcion que retorne valores
#def crear_contraseña_random(num):
#    chars = 'abcdefg'
#    num_entero = str(num)
#    num = int(num_entero[0])
#    c1 = num - 2
#    c2 = num
#    c3 = num - 5
#    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
#    return contraseña
    
#password = crear_contraseña_random(4)
#print(password)


#utilizando parametro args -> se debe utulizar al final
def suma(nombre, *numeros):
    return f"{nombre}, la suma de todos tus numeros es: {sum(numeros)}"

resultado = suma("bere",4,5,6,7)
print(resultado)

#forma no optima de sumar valores
def sum_total(numeros):
    return sum(*numeros)

resultado2 = sum_total([5,9,10,15,20])

print(resultado2)

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = sum_total([5,3,9,10,15])

