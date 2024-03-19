# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:37:07 2024

@author: linac
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Extract features and target
X = iris.data
Y = iris.target  # Target for coloring

#%% Fitting
# Instantiate KMeans with 3 clusters
kmeans = KMeans(n_clusters=3)

# Fit KMeans to the data
kmeans.fit(X)

# Get cluster labels
cluster_labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

#%% Plotting
# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))


# Plot 1: Iris samples colored by species
for i in range(len(np.unique(Y))):
    axs[0].scatter(X[Y == i, 0], X[Y == i, 1], label=f'Species {i}')
axs[0].set_title('Iris Samples by Species')
axs[0].set_xlabel('Sepal Length (cm)')
axs[0].set_ylabel('Sepal Width (cm)')
axs[0].legend()

# Plot 2: Clusters found by KMeans
for i in range(len(np.unique(cluster_labels))):
    axs[1].scatter(
        X[cluster_labels == i, 0], 
        X[cluster_labels == i, 1], 
        label=f'Cluster {i+1}',
        )
    axs[1].scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200, marker='X', label='Cluster Centers')

axs[1].set_title('Clusters Found by KMeans')
axs[1].set_xlabel('Sepal Length (cm)')
axs[1].set_ylabel('Sepal Width (cm)')
axs[1].legend()

plt.tight_layout()
plt.show()
