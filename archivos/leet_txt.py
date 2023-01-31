#usnado openpara abrirn un arhivo
archivo = open("archivos\\texto_bere.txt",encoding="UTF-8")

#leer archivo completo
#archivo = archivo.read()

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo.readline()

print(linea)

#cerrar el archivo

archivo.close()

print(archivo)