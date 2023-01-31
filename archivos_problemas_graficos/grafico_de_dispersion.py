import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")

#creando el grafico
sns.scatterplot(x="fuente",y="ingresos",data=df)

#mostrando el grafico
plt.show()