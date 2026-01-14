import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./datos_ejercicios_sesion3.csv")

variable = "annual_income"
df[variable].hist(bins=30)
plt.xlabel(variable)
plt.ylabel(variable)
plt.title(f"Histograma: {variable}")
plt.show()

variable2 = "avg_session_min"
df[variable2].hist(bins=30)
plt.xlabel(variable2)
plt.ylabel(variable2)
plt.title(f"Histograma: {variable2}")
plt.show()

