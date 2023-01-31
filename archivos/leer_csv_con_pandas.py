#desde le cmd -> py -m pip install pandas
import pandas as pd
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo los datos de la primera columna
nombres = df["nombre"]

#ordenamo el dataframe por la edad
df_ordenado_ascendente = df.sort_values("edad")

#ordenando de forma descenten
df_ordenado_descendente = df.sort_values("edad",ascending=False)


#concatenando lso dos dataframe
df_concatenado = pd.concat([df,df2])

#asccediento a la primeras 3 fila con head()
primeras_filas = df.head(3)

#accediento alas ultimas 3 filas conm tail()
ultimas_filas = df.tail(3)


#accediento a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape


#obteniendo data estadistica dle dataframe:
df_info = df.describe()

#accediento a un elemento especifico del df con lo
#elemento_especifico_loc = df.loc(2,"edad")

#accediento aun elemento con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediento a todas las filas d una columna
apellidos_loc = df.loc[:,"apellido"]

#accediento a todos los apellidos ocn iloc
apellidos = df.iloc[:,1]

#accediento a la fila 3 con loc
fila_3 = df.loc[2, :]


#accediento a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)