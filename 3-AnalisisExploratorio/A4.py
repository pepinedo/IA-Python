import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./datos_ejercicios_sesion3.csv")

var = "country"
print("-- Número de categorías: ", df[var].value_counts().count())
print("-- Frecuencia absoluta:\n", df[var].value_counts())
print("-- Frecuencia relativa:\n", df[var].value_counts(normalize=True) * 100)