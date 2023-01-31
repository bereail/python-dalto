#si el modulo estuviera en una carpeta en la misma ruta
# import funciones_buenas.saludar as saludin 

#si el modulo esta en un carpeta anterior
import sys  

sys.path.append(['c:\\Users\\berea\\Desktop\\bere\\python-daltp\\modulos', 'C:\\Python311\\python311.zip', 'C:\\Python311\\Lib', 'C:\\Python311\\DLLs', 'C:\\Python311', 'C:\\Python311\\Lib\\site-packages\\funciones_buenas'])

#import saludar as modulo_saludo 

#print(modulo_saludo.saludar("bere"))

#print(saludin.saludar("bere"))

#print(sys.builtin_module_names)