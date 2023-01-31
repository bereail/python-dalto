lista = list(["bere",1,False])

#agrego varios elemntos a la lista
#lista.extend(12,2030)

#devuelve la cantida de elementos de una lista
cantidad_elemntos = len(lista)

#agrega un elemento a la lista
lista.append(65)

#elimina un elementos de la lista por su indice
lista.pop(2) #-1 para eliminar el ultimo

#removiendo un elemento de la lista por su valor
lista.remove("hola")

#eliminando todos los elemntos de la lista 
#lista.clear()

#ordenando la lista de forma ascendente
lista.sort()

#invirtiendo los elemtnso de una lista
lista.reverse()

#verificnaod si un elmento se encuentra en la lista
elemento_encontrado = lista.index(1)

print(elemento_encontrado)


#set para armar un conjunto
elemento_encontrado_en_conjunto = set(["dsd"])