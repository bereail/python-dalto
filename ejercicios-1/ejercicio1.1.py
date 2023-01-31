frase = input("decime algo: ")


#permuite separa las palabra
palabras_separadas = frase.split(" ")

cantidad_de_palabras = len(palabras_separadas)

print(f'Dijiste {cantidad_de_palabras} y tardarias {cantidad_de_palabras/2} segundos en decirlo')

