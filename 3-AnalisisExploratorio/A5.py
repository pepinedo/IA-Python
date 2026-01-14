import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./datos_ejercicios_sesion3.csv")

print("Variables que tiene nulos:\n", df.isna().sum())

print("Proporción de nulos:\n", (df.isna().sum() / len(df)) * 100)

#La proporción de nulos es del 10%, por lo que parece estructural
