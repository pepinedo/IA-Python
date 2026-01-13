import numpy as np

rng = np.random.default_rng(42)
base = 1.8
noise = rng.normal(0, 0.3, size=168)
consumo = base + noise
consumo = np.clip(consumo, 0, None).astype(np.float64)

# Introducción de outliers
idx_outliers = rng.choice(np.arange(consumo.size), size=6, replace=False)
consumo[idx_outliers] += rng.uniform(5, 12, size=6)

#Datos originales
print("Media: ", consumo.mean(axis=0))
print("Mediana: ", np.median(consumo))

#Outliers sustituidos por np.nan
consumo_nan = consumo.copy()
mask = consumo > 4
consumo_nan[mask] = np.nan

print("Media: ", consumo_nan.mean(axis=0))
print("Mediana: ", np.median(consumo_nan))

#Outliers sustituidos por 0
consumo_0 = consumo.copy()
mask = consumo > 4
consumo_0[mask] = 0

print("Media: ", consumo_0.mean(axis=0))
print("Mediana: ", np.median(consumo_0))