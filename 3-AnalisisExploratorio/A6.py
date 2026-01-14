import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("./datos_ejercicios_sesion3.csv")

var1 = "app_version"
var2 = "avg_session_min"

plt.scatter(df[var1], df[var2], alpha=0.6)
plt.xlabel(var1)
plt.ylabel(var2)
plt.title(f"Scatter: {var1} vs {var2}")
plt.show()

#Tendencia: no lineal
#Nivel del ruido: bajo
#Presencia de outliers relevantes: no
#¿Merece exploración posterior? dudas