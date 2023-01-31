diccionario = {
    "nombre": 'berenice',
    "apellidos": 'solohaga',
    "subs": 100000
}



#permite ver los keys del diccionario
claves = diccionario.keys()


#deuvelve el valor de la keys ingresada
valor_de_nombre = diccionario.get("nombre")

#elimina todos los elemtnos del diccionario
diccionario.clear()


#elimino elemento de un dicciopnario
diccionario.pop("nombre", "apellido")

#obteniento un elemnto dict_items iterable
diccionario_iterable = diccionario.items()


print(claves)