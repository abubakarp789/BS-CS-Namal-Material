"""
===============================================================================
PRINCIPAL COMPONENT ANALYSIS (PCA) - COMPLETE IMPLEMENTATION
Assignment 04 - Machine Learning
===============================================================================

This file contains the complete implementation of PCA from scratch, including:
1. Data loading and validation
2. Statistical analysis (mean, std, covariance, correlation)
3. Data centering
4. Eigenvalue decomposition
5. Variance explained calculation
6. Projection to lower dimensions (1D, 2D)
7. Reconstruction from projections
8. Visualization (3D, 2D, 1D plots)
9. Main analysis pipeline

Author: Abu Bakar
Date: January 2026
===============================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# =============================================================================
# PART 1: DATA LOADING AND VALIDATION
# =============================================================================

def load_data(filepath: str) -> np.ndarray:
    """
    Load the 3D dataset from CSV file.
    
    Parameters:
        filepath: Path to the CSV file
        
    Returns:
        data: numpy array of shape (n, 3) containing x1, x2, x3
        
    Raises:
        FileNotFoundError: If CSV file doesn't exist
        ValueError: If data format is invalid
    """
    try:
        # Read CSV file using pandas
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at path: {filepath}")
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {str(e)}")
    
    # Validate that exactly 3 columns exist (x1, x2, x3)
    expected_columns = ['x1', 'x2', 'x3']
    if list(df.columns) != expected_columns:
        raise ValueError(
            f"Invalid CSV format: expected 3 columns (x1, x2, x3), "
            f"found {len(df.columns)} columns: {list(df.columns)}"
        )
    
    # Check for missing values
    if df.isnull().any().any():
        n_missing = df.isnull().sum().sum()
        raise ValueError(f"Dataset contains {n_missing} missing values")
    
    # Convert to numpy array
    data = df.to_numpy()
    
    # Validate data shape
    if data.shape[1] != 3:
        raise ValueError(f"Invalid data shape: expected (n, 3), got {data.shape}")
    
    return data


# =============================================================================
# PART 2: STATISTICAL ANALYSIS
# =============================================================================

def compute_statistics(data: np.ndarray) -> dict:
    """
    Compute mean and standard deviation for each feature.
    
    Parameters:
        data: numpy array of shape (n, 3)
        
    Returns:
        stats: dictionary with keys 'means', 'stds'
    """
    # Compute mean for each feature (axis=0 computes along rows)
    means = np.mean(data, axis=0)
    
    # Compute standard deviation with ddof=1 (sample standard deviation)
    stds = np.std(data, axis=0, ddof=1)
    
    return {'means': means, 'stds': stds}


def center_data(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Center the data by subtracting the mean of each feature.
    
    Parameters:
        data: numpy array of shape (n, 3)
        
    Returns:
        centered_data: zero-mean data of shape (n, 3)
        means: array of shape (3,) containing the mean of each feature
    """
    # Compute mean of each feature
    means = np.mean(data, axis=0)
    
    # Subtract mean from data (creates new array, doesn't modify original)
    centered_data = data - means
    
    return centered_data, means


def compute_covariance_matrix(centered_data: np.ndarray) -> np.ndarray:
    """
    Compute the 3x3 covariance matrix.
    
    Parameters:
        centered_data: zero-mean data of shape (n, 3)
        
    Returns:
        cov_matrix: 3x3 covariance matrix
    """
    # Get number of samples
    n = centered_data.shape[0]
    
    # Compute covariance using formula: Σ = (1/n) * X^T @ X
    cov_matrix = (1 / n) * (centered_data.T @ centered_data)
    
    # Ensure the matrix is symmetric (handle numerical precision)
    cov_matrix = (cov_matrix + cov_matrix.T) / 2
    
    return cov_matrix


def compute_correlation_matrix(data: np.ndarray) -> np.ndarray:
    """
    Compute the 3x3 correlation matrix.
    
    Parameters:
        data: numpy array of shape (n, 3)
        
    Returns:
        corr_matrix: 3x3 correlation matrix with ones on diagonal
    """
    # Use NumPy's corrcoef function (rowvar=False means columns are variables)
    corr_matrix = np.corrcoef(data, rowvar=False)
    
    return corr_matrix



# =============================================================================
# PART 3: EIGENVALUE DECOMPOSITION
# =============================================================================

def compute_eigen_decomposition(cov_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute eigenvalues and eigenvectors of the covariance matrix.
    
    Parameters:
        cov_matrix: 3x3 covariance matrix
        
    Returns:
        eigenvalues: array of shape (3,) sorted in descending order
        eigenvectors: array of shape (3, 3) where column i is eigenvector for eigenvalue i
    """
    # Use NumPy's eigenvalue decomposition function
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # Sort eigenvalues in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    
    # Reorder eigenvalues and eigenvectors
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]
    
    return eigenvalues, eigenvectors


def compute_variance_explained(eigenvalues: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute variance explained by each principal component.
    
    Parameters:
        eigenvalues: array of shape (3,) in descending order
        
    Returns:
        variance_explained: array of shape (3,) with proportion for each PC
        cumulative_variance: array of shape (3,) with cumulative proportions
    """
    # Compute total variance as sum of all eigenvalues
    total_variance = np.sum(eigenvalues)
    
    # Compute proportion of variance explained by each eigenvalue
    variance_explained = eigenvalues / total_variance
    
    # Compute cumulative variance explained
    cumulative_variance = np.cumsum(variance_explained)
    
    return variance_explained, cumulative_variance



# =============================================================================
# PART 4: PROJECTION TO LOWER DIMENSIONS
# =============================================================================

def project_to_1d(centered_data: np.ndarray, pc1: np.ndarray) -> np.ndarray:
    """
    Project data onto the first principal component.
    
    Parameters:
        centered_data: zero-mean data of shape (n, 3)
        pc1: first principal component (eigenvector) of shape (3,)
        
    Returns:
        projected_data: array of shape (n,) with projections onto PC1
    """
    # Project centered data onto first principal component
    # X @ v1 computes the dot product of each row with v1
    projected_data = centered_data @ pc1
    
    return projected_data


def project_to_2d(centered_data: np.ndarray, pc1: np.ndarray, pc2: np.ndarray) -> np.ndarray:
    """
    Project data onto the first two principal components.
    
    Parameters:
        centered_data: zero-mean data of shape (n, 3)
        pc1: first principal component of shape (3,)
        pc2: second principal component of shape (3,)
        
    Returns:
        projected_data: array of shape (n, 2) with projections onto PC1 and PC2
    """
    # Stack the two principal components as columns
    pc_matrix = np.column_stack([pc1, pc2])
    
    # Project centered data onto first two principal components
    projected_data = centered_data @ pc_matrix
    
    return projected_data



# =============================================================================
# PART 5: RECONSTRUCTION FROM PROJECTIONS
# =============================================================================

def reconstruct_from_1d(projected_1d: np.ndarray, pc1: np.ndarray, means: np.ndarray) -> np.ndarray:
    """
    Reconstruct 3D data from 1D projection.
    
    Parameters:
        projected_1d: 1D projections of shape (n,) or (n, 1)
        pc1: first principal component of shape (3,)
        means: original means of shape (3,)
        
    Returns:
        reconstructed: array of shape (n, 3)
    """
    # Ensure projected_1d is a column vector
    if projected_1d.ndim == 1:
        projected_1d = projected_1d.reshape(-1, 1)
    
    # Reconstruct using formula: X_recon = Z @ v1^T + means
    reconstructed = projected_1d @ pc1.reshape(1, -1) + means
    
    return reconstructed


def reconstruct_from_2d(projected_2d: np.ndarray, pc1: np.ndarray, pc2: np.ndarray, means: np.ndarray) -> np.ndarray:
    """
    Reconstruct 3D data from 2D projection.
    
    Parameters:
        projected_2d: 2D projections of shape (n, 2)
        pc1: first principal component of shape (3,)
        pc2: second principal component of shape (3,)
        means: original means of shape (3,)
        
    Returns:
        reconstructed: array of shape (n, 3)
    """
    # Stack the two principal components as columns
    pc_matrix = np.column_stack([pc1, pc2])
    
    # Reconstruct using formula: X_recon = Z @ [v1, v2]^T + means
    reconstructed = projected_2d @ pc_matrix.T + means
    
    return reconstructed


def compute_reconstruction_error(original: np.ndarray, reconstructed: np.ndarray) -> float:
    """
    Compute mean squared error between original and reconstructed data.
    
    Parameters:
        original: original data of shape (n, 3)
        reconstructed: reconstructed data of shape (n, 3)
        
    Returns:
        mse: mean squared error (scalar)
    """
    # Compute the squared differences element-wise
    squared_diff = (original - reconstructed) ** 2
    
    # Compute the mean of all squared differences (MSE)
    mse = np.mean(squared_diff)
    
    return mse



# =============================================================================
# PART 6: VISUALIZATION FUNCTIONS
# =============================================================================

def plot_3d_data(data: np.ndarray, title: str = "3D Data Visualization", save_path: str = None) -> None:
    """
    Create a 3D scatter plot of the original data.
    
    Parameters:
        data: numpy array of shape (n, 3) with columns [x1, x2, x3]
        title: plot title
        save_path: optional path to save the figure
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create scatter plot
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], 
               c='blue', marker='o', s=50, alpha=0.6, edgecolors='k')
    
    # Label axes
    ax.set_xlabel('x1', fontsize=12, labelpad=10)
    ax.set_ylabel('x2', fontsize=12, labelpad=10)
    ax.set_zlabel('x3', fontsize=12, labelpad=10)
    ax.set_title(title, fontsize=14, pad=20)
    ax.grid(True, alpha=0.3)
    
    # Save if path provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"   Plot saved to: {save_path}")
    
    plt.tight_layout()
    plt.show()


def plot_2d_projection(projected_2d: np.ndarray, variance_explained: np.ndarray, 
                       title: str = "2D PCA Projection", save_path: str = None) -> None:
    """
    Create a 2D scatter plot of data projected onto PC1 and PC2.
    
    Parameters:
        projected_2d: array of shape (n, 2)
        variance_explained: array with variance explained by each PC
        title: plot title
        save_path: optional path to save the figure
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create scatter plot
    ax.scatter(projected_2d[:, 0], projected_2d[:, 1], 
               c='green', marker='o', s=50, alpha=0.6, edgecolors='k')
    
    # Label axes with variance explained
    pc1_var = variance_explained[0] * 100
    pc2_var = variance_explained[1] * 100
    ax.set_xlabel(f'PC1 ({pc1_var:.2f}% variance explained)', fontsize=12)
    ax.set_ylabel(f'PC2 ({pc2_var:.2f}% variance explained)', fontsize=12)
    ax.set_title(title, fontsize=14, pad=20)
    ax.grid(True, alpha=0.3)
    
    # Add axis lines at zero
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    ax.set_aspect('equal', adjustable='datalim')
    
    # Save if path provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"   Plot saved to: {save_path}")
    
    plt.tight_layout()
    plt.show()



def plot_1d_projection(projected_1d: np.ndarray, variance_explained: float, 
                       title: str = "1D PCA Projection", save_path: str = None) -> None:
    """
    Create a 1D scatter plot of data projected onto PC1.
    
    Parameters:
        projected_1d: array of shape (n,) or (n, 1)
        variance_explained: variance explained by PC1
        title: plot title
        save_path: optional path to save the figure
    """
    # Ensure projected_1d is 1D array
    if projected_1d.ndim == 2:
        projected_1d = projected_1d.flatten()
    
    fig, ax = plt.subplots(figsize=(12, 4))
    
    # Create 1D scatter plot with random jitter for visualization
    n_points = len(projected_1d)
    y_jitter = np.random.uniform(-0.1, 0.1, n_points)
    
    ax.scatter(projected_1d, y_jitter, 
               c='red', marker='o', s=50, alpha=0.6, edgecolors='k')
    
    # Label x-axis with variance explained
    pc1_var = variance_explained * 100
    ax.set_xlabel(f'PC1 ({pc1_var:.2f}% variance explained)', fontsize=12)
    ax.set_ylabel('Random Jitter', fontsize=12)
    ax.set_title(title, fontsize=14, pad=20)
    ax.grid(True, alpha=0.3, axis='x')
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    ax.set_yticks([])
    ax.set_ylim(-0.3, 0.3)
    
    # Save if path provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"   Plot saved to: {save_path}")
    
    plt.tight_layout()
    plt.show()



# =============================================================================
# PART 7: MAIN ANALYSIS PIPELINE
# =============================================================================

def main():
    """
    Main function to perform complete PCA analysis.
    """
    print("=" * 80)
    print("PCA ANALYSIS ON 3D DATASET")
    print("=" * 80)
    print()
    
    # 1. Load the dataset
    print("1. Loading dataset...")
    data = load_data('pca_3d_dataset.csv')
    print(f"   Dataset loaded successfully: {data.shape[0]} samples, {data.shape[1]} features")
    print()
    
    # 2. Compute and display basic statistics
    print("2. Basic Statistics")
    print("-" * 80)
    stats = compute_statistics(data)
    means = stats['means']
    stds = stats['stds']
    
    print("   Mean for each feature:")
    for i, mean in enumerate(means, 1):
        print(f"      x{i}: {mean:.6f}")
    print()
    
    print("   Standard Deviation for each feature:")
    for i, std in enumerate(stds, 1):
        print(f"      x{i}: {std:.6f}")
    print()
    
    # 3. Compute and display covariance matrix
    print("3. Covariance Matrix")
    print("-" * 80)
    centered_data, _ = center_data(data)
    cov_matrix = compute_covariance_matrix(centered_data)
    print("   3x3 Covariance Matrix:")
    print(cov_matrix)
    print()
    
    # 4. Compute and display correlation matrix
    print("4. Correlation Matrix")
    print("-" * 80)
    corr_matrix = compute_correlation_matrix(data)
    print("   3x3 Correlation Matrix:")
    print(corr_matrix)
    print()
    
    # 5. Create 3D scatter plot
    print("5. Creating 3D scatter plot of original data...")
    plot_3d_data(data, title="Original 3D Dataset", save_path="plot_3d_original.png")
    print("   3D plot displayed and saved.")
    print()
    
    # 6. Compute eigenvalues and eigenvectors
    print("6. Eigenvalue Decomposition")
    print("-" * 80)
    eigenvalues, eigenvectors = compute_eigen_decomposition(cov_matrix)
    
    print("   Eigenvalues (sorted in descending order):")
    for i, eigenval in enumerate(eigenvalues, 1):
        print(f"      λ{i}: {eigenval:.6f}")
    print()
    
    print("   Eigenvectors (Principal Components):")
    for i in range(3):
        print(f"      v{i+1}: [{eigenvectors[0, i]:8.6f}, {eigenvectors[1, i]:8.6f}, {eigenvectors[2, i]:8.6f}]")
    print()
    
    # 7. Compute and display variance explained
    print("7. Variance Explained")
    print("-" * 80)
    variance_explained, cumulative_variance = compute_variance_explained(eigenvalues)
    
    print("   Variance Explained by each Principal Component:")
    for i, var_exp in enumerate(variance_explained, 1):
        print(f"      PC{i}: {var_exp * 100:.2f}%")
    print()
    
    print("   Cumulative Variance Explained:")
    for i, cum_var in enumerate(cumulative_variance, 1):
        print(f"      PC1-PC{i}: {cum_var * 100:.2f}%")
    print()
    
    # 8. Project to 1D and 2D
    print("8. Projecting data to lower dimensions...")
    pc1 = eigenvectors[:, 0]
    pc2 = eigenvectors[:, 1]
    
    projected_1d = project_to_1d(centered_data, pc1)
    print(f"   1D projection shape: {projected_1d.shape}")
    
    projected_2d = project_to_2d(centered_data, pc1, pc2)
    print(f"   2D projection shape: {projected_2d.shape}")
    print()
    
    # 9. Create 2D projection plot
    print("9. Creating 2D projection plot...")
    plot_2d_projection(projected_2d, variance_explained, 
                       title="2D PCA Projection (PC1 vs PC2)", 
                       save_path="plot_2d_projection.png")
    print("   2D projection plot displayed and saved.")
    print()
    
    # 10. Create 1D projection plot
    print("10. Creating 1D projection plot...")
    plot_1d_projection(projected_1d, variance_explained[0], 
                       title="1D PCA Projection (PC1)",
                       save_path="plot_1d_projection.png")
    print("    1D projection plot displayed and saved.")
    print()
    
    # 11. Compute reconstruction errors
    print("11. Reconstruction Analysis")
    print("-" * 80)
    
    reconstructed_1d = reconstruct_from_1d(projected_1d, pc1, means)
    error_1d = compute_reconstruction_error(data, reconstructed_1d)
    print(f"    Reconstruction Error (1D): {error_1d:.6f}")
    
    reconstructed_2d = reconstruct_from_2d(projected_2d, pc1, pc2, means)
    error_2d = compute_reconstruction_error(data, reconstructed_2d)
    print(f"    Reconstruction Error (2D): {error_2d:.6f}")
    print()
    
    print("    Note: Lower error means better reconstruction.")
    print("    2D reconstruction should have lower error than 1D.")
    print()
    
    # Summary
    print("=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print()
    print("Summary:")
    print(f"  - Dataset: {data.shape[0]} samples with {data.shape[1]} features")
    print(f"  - PC1 explains {variance_explained[0] * 100:.2f}% of variance")
    print(f"  - PC1 + PC2 explain {cumulative_variance[1] * 100:.2f}% of variance")
    print(f"  - All 3 PCs explain {cumulative_variance[2] * 100:.2f}% of variance")
    print(f"  - 1D reconstruction error: {error_1d:.6f}")
    print(f"  - 2D reconstruction error: {error_2d:.6f}")
    print()
    print("Saved Files:")
    print("  - plot_3d_original.png (3D scatter plot)")
    print("  - plot_2d_projection.png (2D PCA projection)")
    print("  - plot_1d_projection.png (1D PCA projection)")
    print()


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    main()
