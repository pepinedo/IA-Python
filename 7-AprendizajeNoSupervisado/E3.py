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

ds = pd.read_csv("./non_convex_shapes.csv")

print(ds.dtypes)

plt.figure()
plt.scatter(ds["x1"], ds["x2"], s=12)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("????")
plt.show();