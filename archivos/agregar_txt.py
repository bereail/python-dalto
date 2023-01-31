with open('archivos\\texto_bere.txt','a', encoding="UTF-8") as archivo:
   #forzando un bucle para agrega varias lineas
   archivo.write("\n")
   for i in range(5):
       #agregando lineas
       archivo.write(f"linea {i+1} agregada\n")