with open('archivos\\texto_bere.txt','w', encoding="UTF-8") as archivo:
   #sobreescribiendo el archivo
   #archivo.write("kakakakakak")
   
   #agregando 2 lineas
   archivo.writelines(["hola maestro\n","como baaaaa\n"])
   
   #agregando otras dos lineas
   archivo.writelines(["hola maestro\n","como baaaaa\n"])