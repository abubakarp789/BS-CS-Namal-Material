"""
Main Script for PCA Analysis

This script performs complete PCA analysis on the 3D dataset.
It loads the data, computes statistics, performs PCA, creates visualizations,
and displays all required outputs for the assignment.
"""

import numpy as np
from pca_core import (
    load_data,
    compute_statistics,
    center_data,
    compute_covariance_matrix,
    compute_correlation_matrix,
    compute_eigen_decomposition,
    compute_variance_explained,
    project_to_1d,
    project_to_2d,
    reconstruct_from_1d,
    reconstruct_from_2d,
    compute_reconstruction_error
)
from visualization import (
    plot_3d_data,
    plot_2d_projection,
    plot_1d_projection
)


def main():
    """
    Main function to perform complete PCA analysis.
    """
    print("=" * 80)
    print("PCA ANALYSIS ON 3D DATASET")
    print("=" * 80)
    print()
    
    # ========================================================================
    # 1. Load the dataset
    # ========================================================================
    print("1. Loading dataset...")
    data = load_data('pca_3d_dataset.csv')
    print(f"   Dataset loaded successfully: {data.shape[0]} samples, {data.shape[1]} features")
    print()
    
    # ========================================================================
    # 2. Compute and display basic statistics
    # ========================================================================
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
    
    # ========================================================================
    # 3. Compute and display covariance matrix
    # ========================================================================
    print("3. Covariance Matrix")
    print("-" * 80)
    
    # Center the data first (required for covariance computation)
    centered_data, _ = center_data(data)
    cov_matrix = compute_covariance_matrix(centered_data)
    
    print("   3x3 Covariance Matrix:")
    print(cov_matrix)
    print()
    
    # ========================================================================
    # 4. Compute and display correlation matrix
    # ========================================================================
    print("4. Correlation Matrix")
    print("-" * 80)
    corr_matrix = compute_correlation_matrix(data)
    
    print("   3x3 Correlation Matrix:")
    print(corr_matrix)
    print()
    
    # ========================================================================
    # 5. Create 3D scatter plot of original data
    # ========================================================================
    print("5. Creating 3D scatter plot of original data...")
    plot_3d_data(data, title="Original 3D Dataset", save_path="plot_3d_original.png")
    print("   3D plot displayed and saved.")
    print()
    
    # ========================================================================
    # 6. Compute eigenvalues and eigenvectors
    # ========================================================================
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
    
    # ========================================================================
    # 7. Compute and display variance explained
    # ========================================================================
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
    
    # ========================================================================
    # 8. Project to 1D and 2D
    # ========================================================================
    print("8. Projecting data to lower dimensions...")
    
    # Extract principal components
    pc1 = eigenvectors[:, 0]
    pc2 = eigenvectors[:, 1]
    
    # Project to 1D (onto PC1)
    projected_1d = project_to_1d(centered_data, pc1)
    print(f"   1D projection shape: {projected_1d.shape}")
    
    # Project to 2D (onto PC1 and PC2)
    projected_2d = project_to_2d(centered_data, pc1, pc2)
    print(f"   2D projection shape: {projected_2d.shape}")
    print()
    
    # ========================================================================
    # 9. Create 2D projection plot
    # ========================================================================
    print("9. Creating 2D projection plot...")
    plot_2d_projection(projected_2d, variance_explained, 
                       title="2D PCA Projection (PC1 vs PC2)", 
                       save_path="plot_2d_projection.png")
    print("   2D projection plot displayed and saved.")
    print()
    
    # ========================================================================
    # 10. Create 1D projection plot
    # ========================================================================
    print("10. Creating 1D projection plot...")
    plot_1d_projection(projected_1d, variance_explained[0], 
                       title="1D PCA Projection (PC1)",
                       save_path="plot_1d_projection.png")
    print("    1D projection plot displayed and saved.")
    print()
    
    # ========================================================================
    # 11. Compute reconstruction errors
    # ========================================================================
    print("11. Reconstruction Analysis")
    print("-" * 80)
    
    # Reconstruct from 1D projection
    reconstructed_1d = reconstruct_from_1d(projected_1d, pc1, means)
    error_1d = compute_reconstruction_error(data, reconstructed_1d)
    print(f"    Reconstruction Error (1D): {error_1d:.6f}")
    
    # Reconstruct from 2D projection
    reconstructed_2d = reconstruct_from_2d(projected_2d, pc1, pc2, means)
    error_2d = compute_reconstruction_error(data, reconstructed_2d)
    print(f"    Reconstruction Error (2D): {error_2d:.6f}")
    print()
    
    print("    Note: Lower error means better reconstruction.")
    print("    2D reconstruction should have lower error than 1D (more components = less information loss).")
    print()
    
    # ========================================================================
    # Summary
    # ========================================================================
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
    print("  - plot_3d_original.png (3D scatter plot of original data)")
    print("  - plot_2d_projection.png (2D PCA projection)")
    print("  - plot_1d_projection.png (1D PCA projection)")
    print()


if __name__ == "__main__":
    main()
