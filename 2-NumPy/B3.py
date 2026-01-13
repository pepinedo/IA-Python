import numpy as np

rng = np.random.default_rng(42)
base = 1.8
noise = rng.normal(0, 0.3, size=168)
consumo = base + noise
consumo = np.clip(consumo, 0, None).astype(np.float64)

# Introducción de outliers
idx_outliers = rng.choice(np.arange(consumo.size), size=6, replace=False)
consumo[idx_outliers] += rng.uniform(5, 12, size=6)

#Elijo ponerla en 4 ya que todos los valores normales son menores a éste numero
mask = consumo > 4

print("Cantidad de valores outliers: ", len(consumo[mask]))
print("Porcentaje de valores outliers", 100 / len(consumo) * len(consumo[mask]), "%")

