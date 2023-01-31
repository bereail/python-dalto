#creando una funcion que suma numeros
def sumas_dos():
    #pidiendo numeros
    while True:
        a = input("num 1: ")
        b = input("num 2: ")
    #intentano convetirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
    #si lanza un excepcion, pedirle que reingrese los datos
        except Exception as e:
            print("ingrese un numero validp")
            print(f"error: {e}")
    #si todo salio bien terminamos el bucle
        else:
            break
        #esto se ejecuta siempre
        finally:
            print("manejo de excepcion finalizado")           
    return resultado

print(sumas_dos())