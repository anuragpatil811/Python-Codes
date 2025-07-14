#!C:\Users\DELL\Downloads\my code\myenv\Scripts\python.exe
import numpy as np
import matplotlib.pyplot as plt

def k_means_clustering(data, k, max_iters=100, tolerance=1e-4):
    """
    K-means clustering algorithm.

    Parameters:
        data (numpy.ndarray): Dataset, each row is a data point.
        k (int): Number of clusters.
        max_iters (int): Maximum number of iterations.
        tolerance (float): Tolerance for centroid movement.

    Returns:
        centroids (numpy.ndarray): Final centroids.
        labels (numpy.ndarray): Cluster assignments for each data point.
    """
    # Initialize centroids randomly from data points
    np.random.seed(42)  # For reproducibility
    initial_indices = np.random.choice(data.shape[0], k, replace=False)
    centroids = data[initial_indices]

    for iteration in range(max_iters):
        
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)

        
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        if np.linalg.norm(new_centroids - centroids) < tolerance:
            print(f"Converged after {iteration + 1} iterations.")
            break

        centroids = new_centroids

    return centroids, labels
np.random.seed(42)
data = np.vstack([
    np.random.normal([2, 2], 0.5, (50, 2)),
    np.random.normal([8, 8], 0.5, (50, 2)),
    np.random.normal([5, 14], 0.5, (50, 2))
])

# Run k-means clustering
k = 3
centroids, labels = k_means_clustering(data, k)

# Plot the results
plt.figure(figsize=(8, 6))
for i in range(k):
    plt.scatter(data[labels == i, 0], data[labels == i, 1], label=f"Cluster {i + 1}")
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x', s=200, label='Centroids')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
