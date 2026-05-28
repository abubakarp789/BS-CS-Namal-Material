"""
PCA Core Implementation

This module contains the core functions for Principal Component Analysis (PCA).
"""

import numpy as np
import pandas as pd


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
        raise ValueError(
            f"Invalid data shape: expected (n, 3), got {data.shape}"
        )
    
    return data


def compute_statistics(data: np.ndarray) -> dict:
    """
    Compute mean and standard deviation for each feature.
    
    Parameters:
        data: numpy array of shape (n, 3)
        
    Returns:
        stats: dictionary with keys 'means', 'stds'
    """
    # Compute mean for each feature (axis=0 computes along rows, giving mean per column)
    means = np.mean(data, axis=0)
    
    # Compute standard deviation with ddof=1 (sample standard deviation)
    # ddof=1 uses n-1 in the denominator for unbiased sample std
    stds = np.std(data, axis=0, ddof=1)
    
    return {
        'means': means,
        'stds': stds
    }


def center_data(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Center the data by subtracting the mean of each feature.
    
    Parameters:
        data: numpy array of shape (n, 3)
        
    Returns:
        centered_data: zero-mean data of shape (n, 3)
        means: array of shape (3,) containing the mean of each feature
    """
    # Compute mean of each feature (axis=0 computes along rows, giving mean per column)
    means = np.mean(data, axis=0)
    
    # Subtract mean from data (creates a new array, doesn't modify original)
    # Broadcasting automatically subtracts each column's mean from all rows in that column
    centered_data = data - means
    
    # Return both centered data and means (means needed for reconstruction later)
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
    # X^T @ X gives us the sum of outer products of each sample
    # Dividing by n gives us the covariance matrix
    cov_matrix = (1 / n) * (centered_data.T @ centered_data)
    
    # Ensure the matrix is symmetric (handle numerical precision issues)
    # This is mathematically guaranteed but floating point arithmetic may introduce small asymmetries
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
    # Use NumPy's corrcoef function which computes the Pearson correlation coefficient
    # rowvar=False means each column is a variable (feature)
    # This returns a symmetric matrix with 1s on the diagonal
    corr_matrix = np.corrcoef(data, rowvar=False)
    
    return corr_matrix


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
    # Returns eigenvalues and eigenvectors (as columns)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # Sort eigenvalues in descending order
    # argsort returns indices that would sort the array
    # [::-1] reverses the order to get descending
    sorted_indices = np.argsort(eigenvalues)[::-1]
    
    # Reorder eigenvalues using the sorted indices
    eigenvalues = eigenvalues[sorted_indices]
    
    # Reorder eigenvectors to match sorted eigenvalues
    # Each column of eigenvectors corresponds to an eigenvalue
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
    # In PCA, the total variance equals the sum of eigenvalues
    total_variance = np.sum(eigenvalues)
    
    # Compute proportion of variance explained by each eigenvalue
    # Each eigenvalue represents the variance captured by its corresponding principal component
    # Dividing by total variance gives us the proportion (between 0 and 1)
    variance_explained = eigenvalues / total_variance
    
    # Compute cumulative variance explained
    # This shows how much total variance is captured by the first k components
    # cumsum computes the cumulative sum: [a, a+b, a+b+c]
    cumulative_variance = np.cumsum(variance_explained)
    
    return variance_explained, cumulative_variance


def project_to_1d(centered_data: np.ndarray, pc1: np.ndarray) -> np.ndarray:
    """
    Project data onto the first principal component.
    
    Parameters:
        centered_data: zero-mean data of shape (n, 3)
        pc1: first principal component (eigenvector) of shape (3,)
        
    Returns:
        projected_data: array of shape (n,) with projections onto PC1
    """
    # Project centered data onto first principal component using matrix-vector multiplication
    # X @ v1 computes the dot product of each row of X with v1
    # This gives us the coordinate of each data point along the PC1 direction
    # Result shape: (n,) - one projection value per sample
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
    # Stack the two principal components as columns to form a (3, 2) matrix
    # column_stack takes 1D arrays and stacks them as columns
    pc_matrix = np.column_stack([pc1, pc2])
    
    # Project centered data onto first two principal components using matrix multiplication
    # X @ [v1, v2] computes the projection onto the 2D subspace spanned by PC1 and PC2
    # Each row of the result contains [coordinate along PC1, coordinate along PC2]
    # Result shape: (n, 2) - two projection values per sample
    projected_data = centered_data @ pc_matrix
    
    return projected_data


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
    # Ensure projected_1d is a column vector for proper matrix multiplication
    # If it's shape (n,), reshape to (n, 1)
    if projected_1d.ndim == 1:
        projected_1d = projected_1d.reshape(-1, 1)
    
    # Reconstruct using formula: X_recon = Z @ v1^T + means
    # Z is (n, 1), v1^T is (1, 3), so Z @ v1^T is (n, 3)
    # This projects the 1D coordinates back into the original 3D space
    # along the direction of the first principal component
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
    # Stack the two principal components as columns to form a (3, 2) matrix
    pc_matrix = np.column_stack([pc1, pc2])
    
    # Reconstruct using formula: X_recon = Z @ [v1, v2]^T + means
    # Z is (n, 2), [v1, v2]^T is (2, 3), so Z @ [v1, v2]^T is (n, 3)
    # This projects the 2D coordinates back into the original 3D space
    # along the plane spanned by the first two principal components
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
    
    # Compute the mean of all squared differences
    # This gives us the Mean Squared Error (MSE)
    mse = np.mean(squared_diff)
    
    return mse
