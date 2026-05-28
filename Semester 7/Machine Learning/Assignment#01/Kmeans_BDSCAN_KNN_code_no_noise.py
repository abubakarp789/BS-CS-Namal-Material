import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

# 1. Load the Dataset
filename = 'Kmeans_DBScan_KNN_convex_no_noise.csv'

try:
    df = pd.read_csv(filename)
    print("Dataset loaded successfully.")
    print(df.head())
except FileNotFoundError:
    print(f"Error: {filename} not found. Please ensure the file is in the same directory.")
    exit()

# 2. Preprocessing
X = df[['x', 'y']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- Task 1: Load and Analyze Dataset ---
print("\n--- Task 1: Dataset Visualization ---")
plt.figure(figsize=(6, 5))
sns.scatterplot(data=df, x='x', y='y', hue='true_label', palette='bright', legend='full')
plt.title('Task 1: Ground Truth (Actual Labels)')
plt.savefig('Task1_GroundTruth.png')
print("Saved Task1_GroundTruth.png")
# plt.show()

# --- Task 2: K-Means Clustering ---
print("\n--- Task 2: K-Means Clustering (k=4) ---")
k_means_k = 4
kmeans = KMeans(n_clusters=k_means_k, random_state=42)
df['kmeans_labels'] = kmeans.fit_predict(X_scaled)

# Get centroids (need to inverse transform to plot on original scale if we plotted original data, 
# but here we usually plot on scaled or just overlay. For simplicity, we plot on scaled data or handle scaling carefully.
# Let's plot on the original scale for consistency with the scatterplot which uses 'x' and 'y' (unscaled).
# However, KMeans was fitted on X_scaled. 
# To plot centroids on original plot, we inverse transform them.
centroids_scaled = kmeans.cluster_centers_
centroids = scaler.inverse_transform(centroids_scaled)

plt.figure(figsize=(6, 5))
sns.scatterplot(data=df, x='x', y='y', hue='kmeans_labels', palette='viridis', legend='full')
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X', label='Centroids')
plt.title(f'Task 2: K-Means Clustering (k={k_means_k})')
plt.legend()
plt.savefig('Task2_KMeans.png')
print("Saved Task2_KMeans.png")
# plt.show()

# --- Task 3: DBSCAN Clustering ---
print("\n--- Task 3: DBSCAN Clustering ---")
# Try 2 different eps values
eps_values = [0.2, 0.5]
min_samples = 5

plt.figure(figsize=(12, 5))

for i, eps in enumerate(eps_values):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    col_name = f'dbscan_labels_eps_{eps}'
    df[col_name] = dbscan.fit_predict(X_scaled)
    
    n_clusters_db = len(set(df[col_name])) - (1 if -1 in df[col_name] else 0)
    n_noise_db = list(df[col_name]).count(-1)
    print(f"DBSCAN (eps={eps}): Clusters={n_clusters_db}, Noise Points={n_noise_db}")

    plt.subplot(1, 2, i+1)
    sns.scatterplot(data=df, x='x', y='y', hue=col_name, palette='deep', legend='full')
    plt.title(f'DBSCAN (eps={eps}, min_samples={min_samples})\nClusters: {n_clusters_db}, Noise: {n_noise_db}')

plt.tight_layout()
plt.savefig('Task3_DBSCAN.png')
print("Saved Task3_DBSCAN.png")
# plt.show()

# --- Task 4: KNN Classification ---
print("\n--- Task 4: KNN Classification ---")
y = df['true_label']
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

k_values = [3, 5, 9]
plt.figure(figsize=(15, 5))

for i, k in enumerate(k_values):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    print(f"\nKNN (k={k}):")
    print(f"Accuracy: {acc:.4f}")
    print("Confusion Matrix:")
    print(cm)
    
    # Visualize KNN boundaries or predictions on the whole dataset
    # For this assignment, plotting the predictions on the whole dataset is a good way to visualize regions
    df[f'knn_labels_k{k}'] = knn.predict(X_scaled)
    
    plt.subplot(1, 3, i+1)
    sns.scatterplot(data=df, x='x', y='y', hue=f'knn_labels_k{k}', palette='bright', legend='full')
    plt.title(f'KNN (k={k})\nAccuracy: {acc:.2f}')

plt.tight_layout()
plt.savefig('Task4_KNN.png')
print("Saved Task4_KNN.png")
# plt.show()

print("\n--- Execution Completed ---")