#cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("archivo_problemas\\datos.csv")

#convertir a string los datos de un columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de datos del primer elemento de la columna edad
print(type(df['edad'][0]))


#reemplazando el apellido solohaga por maestro
df['apellido'].replace("solohaga","maestro",inplace=True)
print(df['apellido'])


#eliminando las filas con datos faltantes
print(df)
df = df.dropna()
print(df)

#eliminando las columnas
df = df.dropna(axis=1)

#eliminando filas repetidas
df = df.drop_duplicates()

#creando un df con el dataframe resultante(limpio)
df.to_csv("archivo_problemas\\datos_limpios.csv")
