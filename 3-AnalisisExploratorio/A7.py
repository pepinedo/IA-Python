import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("./datos_ejercicios_sesion3.csv")

df_num = df.select_dtypes(include="number")
corr = df_num.corr(numeric_only=True)
print(corr)

#Me llaman la atención:
#  ternure_days y app_version con un -0.893... de correlación
#  churned con app_version con un 0.237... de correlacion

# Una tiene correlación negativa y la otra es simplemente la mayor correlación encontrada, la cual es muy baja y bajo mi punto de vista irrelevante. De todos modos ninguna lleva a ser significativa. 