#2 listas con nombre y apellidos
nombres = ["bere","clara","lucia","martina"]
apellidos = ["solohaga","marnitez","fernandex","dominguez"]

#registrar esta informacion en un txt de forma optima

with open('archivo_problemas\\nombres_y_apellidos.txt','w') as arch:
    arch.writelines("los datos son: \n\n")
    [arch.writelines(f'nombre: {n}\n apelido: {a}\n---------------') for n,a in zip(nombres,apellidos)] 
