import numpy as np

rng = np.random.default_rng(42)
base = 1.8
noise = rng.normal(0, 0.3, size=168)
consumo = base + noise
consumo = np.clip(consumo, 0, None).astype(np.float64)

# Introducción de outliers
idx_outliers = rng.choice(np.arange(consumo.size), size=6, replace=False)
consumo[idx_outliers] += rng.uniform(5, 12, size=6)

import matplotlib.pyplot as plt

plt.figure()
plt.hist(consumo, bins=50)
plt.title("Histograma consumo (raw)")
plt.show()

plt.figure()
plt.plot(consumo)
plt.title("Serie temporal consumo (raw)")
plt.show()

# No, todos los valores no pertenecen al mismo comportamiento normal. Hay muchos valores muy extremos. Esto por la parte del Histograma. 
# Por la parte de la serie temporal de consumo hay varios picos muy pronunciados. 