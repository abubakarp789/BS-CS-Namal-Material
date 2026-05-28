"""
Visualization Module

This module contains functions for creating visualizations of PCA results.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_3d_data(data: np.ndarray, title: str = "3D Data Visualization", save_path: str = None) -> None:
    """
    Create a 3D scatter plot of the original data.
    
    Parameters:
        data: numpy array of shape (n, 3) with columns [x1, x2, x3]
        title: plot title
        save_path: optional path to save the figure (e.g., 'plot_3d.png')
    """
    # Create a new figure
    fig = plt.figure(figsize=(10, 8))
    
    # Add a 3D subplot
    ax = fig.add_subplot(111, projection='3d')
    
    # Create scatter plot with the three features
    # data[:, 0] is x1, data[:, 1] is x2, data[:, 2] is x3
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], 
               c='blue', marker='o', s=50, alpha=0.6, edgecolors='k')
    
    # Label axes appropriately
    ax.set_xlabel('x1', fontsize=12, labelpad=10)
    ax.set_ylabel('x2', fontsize=12, labelpad=10)
    ax.set_zlabel('x3', fontsize=12, labelpad=10)
    
    # Add title
    ax.set_title(title, fontsize=14, pad=20)
    
    # Make plot interactive (allows rotation)
    # This is automatic with matplotlib's 3D plots
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3)
    
    # Save the plot if path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"   Plot saved to: {save_path}")
    
    # Show the plot
    plt.tight_layout()
    plt.show()


def plot_2d_projection(projected_2d: np.ndarray, variance_explained: np.ndarray, 
                       title: str = "2D PCA Projection", save_path: str = None) -> None:
    """
    Create a 2D scatter plot of data projected onto PC1 and PC2.
    
    Parameters:
        projected_2d: array of shape (n, 2) with projections onto PC1 and PC2
        variance_explained: array with variance explained by each PC (as proportions)
        title: plot title
        save_path: optional path to save the figure (e.g., 'plot_2d.png')
    """
    # Create a new figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create scatter plot with PC1 on x-axis and PC2 on y-axis
    ax.scatter(projected_2d[:, 0], projected_2d[:, 1], 
               c='green', marker='o', s=50, alpha=0.6, edgecolors='k')
    
    # Label axes with variance explained percentages
    # Convert proportions to percentages
    pc1_var = variance_explained[0] * 100
    pc2_var = variance_explained[1] * 100
    
    ax.set_xlabel(f'PC1 ({pc1_var:.2f}% variance explained)', fontsize=12)
    ax.set_ylabel(f'PC2 ({pc2_var:.2f}% variance explained)', fontsize=12)
    
    # Add title
    ax.set_title(title, fontsize=14, pad=20)
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3)
    
    # Add axis lines at zero
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    
    # Equal aspect ratio for better visualization
    ax.set_aspect('equal', adjustable='datalim')
    
    # Save the plot if path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"   Plot saved to: {save_path}")
    
    # Show the plot
    plt.tight_layout()
    plt.show()


def plot_1d_projection(projected_1d: np.ndarray, variance_explained: float, 
                       title: str = "1D PCA Projection", save_path: str = None) -> None:
    """
    Create a 1D scatter plot of data projected onto PC1.
    
    Parameters:
        projected_1d: array of shape (n,) or (n, 1) with projections onto PC1
        variance_explained: variance explained by PC1 (as proportion)
        title: plot title
        save_path: optional path to save the figure (e.g., 'plot_1d.png')
    """
    # Ensure projected_1d is 1D array
    if projected_1d.ndim == 2:
        projected_1d = projected_1d.flatten()
    
    # Create a new figure
    fig, ax = plt.subplots(figsize=(12, 4))
    
    # Create 1D scatter plot with random jitter on y-axis for better visualization
    # Use small random jitter to spread points vertically so they don't all overlap
    n_points = len(projected_1d)
    y_jitter = np.random.uniform(-0.1, 0.1, n_points)
    
    ax.scatter(projected_1d, y_jitter, 
               c='red', marker='o', s=50, alpha=0.6, edgecolors='k')
    
    # Label x-axis with variance explained percentage
    pc1_var = variance_explained * 100
    ax.set_xlabel(f'PC1 ({pc1_var:.2f}% variance explained)', fontsize=12)
    ax.set_ylabel('Random Jitter', fontsize=12)
    
    # Add title
    ax.set_title(title, fontsize=14, pad=20)
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add vertical line at zero
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    
    # Remove y-axis ticks since jitter is arbitrary
    ax.set_yticks([])
    
    # Set y-axis limits to keep jitter visible but minimal
    ax.set_ylim(-0.3, 0.3)
    
    # Save the plot if path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"   Plot saved to: {save_path}")
    
    # Show the plot
    plt.tight_layout()
    plt.show()
