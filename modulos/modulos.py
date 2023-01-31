#as nos permite modificar un nombre de un modulo a otro
#import modulo_saludar as m_saludar

#importanto todo
from modulo_saludar import *

#importanto funciones desde el modulo
from modulo_saludar import saludar, saludar_raro


#creamos las varibale con los saludos
saludo = saludar("bere")
saludar_raro = saludar_raro("bebi")

#mostrando los resultados
print(saludo)
print(saludar_raro)

#accedemso al nombre dle modulo llamdo
print(__name__)