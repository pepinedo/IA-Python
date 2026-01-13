import numpy as np

rng = np.random.default_rng(42)
base = 1.8
noise = rng.normal(0, 0.3, size=168)
consumo = base + noise
consumo = np.clip(consumo, 0, None).astype(np.float64)

# Introducción de outliers
idx_outliers = rng.choice(np.arange(consumo.size), size=6, replace=False)
consumo[idx_outliers] += rng.uniform(5, 12, size=6)


print(consumo.shape)
print(consumo.dtype)
print(consumo.ndim)

print("Valor máximo: ", consumo.max())
print("Valor mínimo: ", consumo.min())
print("Media: ", consumo.mean(axis=0))
print("Mediana: ", np.median(consumo))

# El valor máximo es muy extremo, esto puede generar mucho ruido. Al generar el gráfico se pueden ver varios valores extremos que alterarán sustancialmente la media. 

import matplotlib.pyplot as plt

plt.figure()
plt.hist(consumo, bins=50)
plt.title("Histograma consumo (raw)")
plt.show()

