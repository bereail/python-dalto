diccionario = {
    "nombre" : "bere",
    "apellido" : "solohaga",
    "edad" : 30
    }

for key in diccionario.items():
    print(key)
 
#recorriendo diccionario para obetner las claves
for key in diccionario:
    key
    print(f'la clave es: {key}')  
 
#recorriendo diccionario con items para obtener la clave y el valor    
for datos in diccionario.items():
    keys = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es: {value}')