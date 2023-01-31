#las clases comienzan en mayuscula
class MiExcepcion():
    def __init__(self, err):
        print(f"cometiste el sigueinte error: {err}") 

#lanzando mi propia excepcion
raise MiExcepcion


#manejandola
try:        
    raise MiExcepcion("hola")
except:
    print("commo vas a cometes ese error")
    

    