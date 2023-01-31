#creando un conjunto son set

conjunto = set(["dato1","dato2","dato3"])

#las tuplas puedne ir dentor de otros datos
#conjunto_con_tupla = set[]


#metienod un conjuunto dentor d eotro conjunti
conjunto_2 = frozenset(["dato4", "dato5"])
conjunto_1 = {conjunto_2, "dato 3"}
print(conjunto_1)

#teoria de conjuntos
conjunto_1 = {1,3,5,7}
conjunto_2 = {1,3,7}

#verificando si  es subconunto = True
resultado = conjunto_2.issubset(conjunto_1)
resultado = conjunto_2<= conjunto_1


#verficando si es un superconuunto
resultado = conjunto_2.issubset(conjunto_1)
resultado = conjunto_2 < conjunto_1


#verificar si hay algun numero en comun
resultado = conjunto_2.isdisjoint(conjunto_1)

print(resultado)