import pandas as pd

df = pd.read_csv("./datos_ejercicios_sesion3.csv")


print("Tamaño de dataset: ", df.shape)

print("Nombres de las columnas: ", df.columns)

print("Tipos de datos inferidos: ", df.dtypes)

print("Valores ausentes: ", df.isna().sum().sort_values(ascending=False))
