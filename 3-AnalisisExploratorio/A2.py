import pandas as pd

df = pd.read_csv("./datos_ejercicios_sesion3.csv")

print("Variables numéricas continuas: \n", df.select_dtypes(include=["float64"]))

print("Variables numéricas discretas: \n", df.select_dtypes(include=["int64"]))

print("Variables categóricas: \n", df.select_dtypes(include=["object"]))

print("Variables binarias: \n", df.select_dtypes(include=["bool"]))