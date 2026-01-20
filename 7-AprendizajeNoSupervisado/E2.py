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

ds = pd.read_csv("./energy_consumption_patterns.csv")

# --- Paso 1. Preparación ---
print("--- Paso 1 ---")

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
Ks = range(2, 9)
inertias = []
silhouettes = []

for k in Ks:
    km = KMeans(n_clusters=k, n_init="auto", random_state=RANDOM_STATE)
    labels_k = km.fit_predict(Z)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(Z, labels_k))

plt.figure()
plt.plot(list(Ks), inertias)
plt.xlabel("k")
plt.ylabel("Inercia")
plt.title("Método del codo (inercia)")

plt.figure()
plt.plot(list(Ks), silhouettes)
plt.xlabel("k")
plt.ylabel("Silhouette")
plt.title("Silhouette score (métrica interna)")
plt.show()

pd.DataFrame({"k": list(Ks), "inertia": inertias, "silhouette": silhouettes})

# --- Paso 2 ---
# La inercia disminuye al aumentar K porque hacer nuevos grupos deja de dar suficiente información
# El silhoutte score mide simultáneamente la cantidad de grupos que puede haber con la información que se puede obtener de ellas

# --- Paso 3 ---
# Elegiría una K intermedia. Una K pequeña haría que no pudiera obtener toda la información posible y una K grande haría que hubiera muchos grupos parecidos entre si, cayendo en redundancia. 

# --- Paso 4 ---
print("--- Paso 4 ---")
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

# Los nombres que le daría a los clusters serían los siguientes: 
# Cluster1: negativo
# Cluster2: neutro
# Cluster3: positivo
# son con respecto a la escala X, osea, PC1