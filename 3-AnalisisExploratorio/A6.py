import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("./datos_ejercicios_sesion3.csv")

var1 = "app_version"
var2 = "tenure_days"

x = np.array(df[var1])
y = np.array(df[var2])
plt.scatter(x, y, alpha=0.7)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Relación")
plt.show()

#Tendencia: lineal
#Nivel del ruido: no lo se
#Presencia de outliers relevantes: no lo se
#¿Merece exploración posterior? tiene una forma muy rara, de 2 cuadrados. 