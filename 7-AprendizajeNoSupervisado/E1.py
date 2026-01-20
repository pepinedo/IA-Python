# Setup básico
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances

# (Reproducibilidad)
RANDOM_STATE = 42

ds = pd.read_csv("./customers_behavior.csv")

# --- Paso 1. Observación ---

print("--- Paso 1 ---")

mins = ds.min(numeric_only=True)
maxs = ds.max(numeric_only=True)
rngs = (maxs - mins).sort_values(ascending=False)
print(pd.DataFrame({"min": mins, "max": maxs, "range": (maxs-mins)}).sort_values("range", ascending=False))

# La variable con mayor rango es -> annual_income_eur con 116445 de rango
# La variable con menor rango es -> loyalty_score con 0.94456 de rango

# --- Paso 2. K-Means SIN escalado ---
print("--- Paso 2 ---")

# Primero pasar a numpy
X = ds.to_numpy();
# Preparar la pipeline del K-Miles
pipeline = Pipeline([
    ("kmeans", KMeans(n_clusters=3, n_init="auto", random_state=RANDOM_STATE))
])
# Las etiquetas de las tabals
labels = pipeline.fit_predict(X)
print(labels[:20], np.unique(labels, return_counts=True))
# Pasar por el PCA
pca = PCA(n_components=2, random_state=RANDOM_STATE)
P = pca.fit_transform(X)

# Representarlo gráficamente
km = KMeans(n_clusters=3, n_init="auto", random_state=RANDOM_STATE)
labels_pca = km.fit_predict(P)

plt.figure()
plt.scatter(P[:, 0], P[:, 1], c=labels_pca, s=12)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("K-Miles")
plt.show();

# Sin escalado, los clusters parecen organizados principalmente según la variable PC1 y esto ocurre porque la variable PC1 está sin escalar, siento esta la dominante. 

# Los centroides se diferencian sobre todo en la dimensión PC1. Las demás dimensiones aportan poco porque, al estar PC1 sin escalar y ser absurdamente más grande, domina.

# --- Paso 3. K-Means CON escalado
print("--- Paso 3 ---")

# Primero pasar a numpy
X = ds.to_numpy();
# Preparar la pipeline del K-Miles
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("kmeans", KMeans(n_clusters=3, n_init="auto", random_state=RANDOM_STATE))
])
# Las etiquetas de las tabals
labels = pipeline.fit_predict(X)
print(labels[:20], np.unique(labels, return_counts=True))
# Pasar por el PCA
pca = PCA(n_components=2, random_state=RANDOM_STATE)
Z = StandardScaler().fit_transform(X)
P = pca.fit_transform(Z)

# Representarlo gráficamente
km = KMeans(n_clusters=3, n_init="auto", random_state=RANDOM_STATE)
labels_pca = km.fit_predict(P)

plt.figure()
plt.scatter(P[:, 0], P[:, 1], c=labels_pca, s=12)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("K-Miles")
plt.show();

# La estructura cambia de forma relevante, si.
# Esto es debido a que, al escalar als variables y hacerlas equivalentes, ahora ninguna es más poderosa que otra y no provoca sesgo. 

# --- Paso 4. K-Means 2 veces con datos diferentes
print("--- Paso 3 ---")

# Primero pasar a numpy
X = ds.to_numpy();
# Preparar la pipeline del K-Miles
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("kmeans", KMeans(n_clusters=3, n_init="auto", random_state=12))
])
# Las etiquetas de las tabals
labels = pipeline.fit_predict(X)
print(labels[:20], np.unique(labels, return_counts=True))
# Pasar por el PCA
pca = PCA(n_components=2, random_state=12)
Z = StandardScaler().fit_transform(X)
P = pca.fit_transform(Z)

# Representarlo gráficamente
km = KMeans(n_clusters=3, n_init="auto", random_state=12)
labels_pca = km.fit_predict(P)

plt.figure()
plt.scatter(P[:, 0], P[:, 1], c=labels_pca, s=12)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("K-Miles")
plt.show();

# Primero pasar a numpy
X = ds.to_numpy();
# Preparar la pipeline del K-Miles
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("kmeans", KMeans(n_clusters=3, n_init="auto", random_state=234))
])
# Las etiquetas de las tabals
labels = pipeline.fit_predict(X)
print(labels[:20], np.unique(labels, return_counts=True))
# Pasar por el PCA
pca = PCA(n_components=2, random_state=124)
Z = StandardScaler().fit_transform(X)
P = pca.fit_transform(Z)

# Representarlo gráficamente
km = KMeans(n_clusters=3, n_init="auto", random_state=124)
labels_pca = km.fit_predict(P)

plt.figure()
plt.scatter(P[:, 0], P[:, 1], c=labels_pca, s=12)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("K-Miles")
plt.show();

# Los clusters cambian. Esto indica que es resultado es sensible a la inicialización. El algoritmo no ha cambiado pero el espacio si. 