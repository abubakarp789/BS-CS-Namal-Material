"""
Machine Learning Assignment 02: Loss Function Analysis
Comparing MSE, MAE, and Huber Loss on Clean and Noisy Datasets
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.optimize import minimize
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')

def mae_loss_function(params, X_vals, y_vals):
    """
    Calculate MAE (Mean Absolute Error) loss for given parameters.
    
    Args:
        params: [slope, intercept]
        X_vals: Feature values
        y_vals: Target values
    
    Returns:
        Total absolute error
    """
    m, c = params
    y_pred = m * X_vals + c
    return np.sum(np.abs(y_vals - y_pred))


def fit_mae_regression(X, y, initial_guess=[1, 1]):
    """
    Fit regression model by minimizing MAE.
    
    Args:
        X: Feature array
        y: Target array
        initial_guess: Initial parameter values [slope, intercept]
    
    Returns:
        Optimized slope and intercept
    """
    result = minimize(mae_loss_function, initial_guess, args=(X, y))
    return result.x


def analyze_dataset(file_path, dataset_name, output_prefix):
    """
    Complete analysis pipeline for a dataset.
    
    Args:
        file_path: Path to CSV file
        dataset_name: Name for display
        output_prefix: Prefix for output files
    """
    print("\n" + "="*70)
    print(f"ANALYSIS: {dataset_name}")
    print("="*70)
    
    # ====== TASK 1: DATA EXPLORATION ======
    print(f"\n--- Task 1: Data Exploration ---")
    df = pd.read_csv(file_path)
    X = df['experience_years'].values
    y = df['salary_k'].values
    X_reshaped = X.reshape(-1, 1)
    
    print(f"Dataset Shape: {df.shape}")
    print(f"Experience Range: {X.min():.1f} - {X.max():.1f} years")
    print(f"Salary Range: {y.min():.1f} - {y.max():.1f}k")
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    color = 'blue' if 'clean' in file_path.lower() else 'orange'
    plt.scatter(X, y, color=color, label='Data Points', alpha=0.6, s=50)
    plt.title(f"Salary vs Experience - {dataset_name}", fontsize=14, fontweight='bold')
    plt.xlabel("Experience (Years)", fontsize=12)
    plt.ylabel("Salary (k USD)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_scatter.png', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()
    
    # ====== TASK 2: MSE REGRESSION ======
    print(f"\n--- Task 2: MSE Regression (Ordinary Least Squares) ---")
    mse_model = LinearRegression()
    mse_model.fit(X_reshaped, y)
    y_pred_mse = mse_model.predict(X_reshaped)
    
    mse_score = mean_squared_error(y, y_pred_mse)
    mae_score_mse = mean_absolute_error(y, y_pred_mse)
    
    print(f"MSE Model: y = {mse_model.coef_[0]:.2f}x + {mse_model.intercept_:.2f}")
    print(f"  MSE: {mse_score:.2f}")
    print(f"  MAE: {mae_score_mse:.2f}")
    
    # Plot MSE Regression
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color=color, label='Data Points', alpha=0.6, s=50)
    plt.plot(X, y_pred_mse, color='red', linewidth=2.5, label='MSE Regression (OLS)')
    plt.title(f"MSE Regression - {dataset_name}", fontsize=14, fontweight='bold')
    plt.xlabel("Experience (Years)", fontsize=12)
    plt.ylabel("Salary (k USD)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_mse.png', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()
    
    # ====== TASK 3: MAE REGRESSION ======
    print(f"\n--- Task 3: MAE Regression (Least Absolute Deviations) ---")
    m_mae, c_mae = fit_mae_regression(X, y)
    y_pred_mae = m_mae * X + c_mae
    
    mse_score_mae = mean_squared_error(y, y_pred_mae)
    mae_score_mae = mean_absolute_error(y, y_pred_mae)
    
    print(f"MAE Model: y = {m_mae:.2f}x + {c_mae:.2f}")
    print(f"  MSE: {mse_score_mae:.2f}")
    print(f"  MAE: {mae_score_mae:.2f}")
    
    # Plot MAE Regression
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color=color, label='Data Points', alpha=0.6, s=50)
    plt.plot(X, y_pred_mae, color='green', linewidth=2.5, label='MAE Regression (LAD)')
    plt.title(f"MAE Regression - {dataset_name}", fontsize=14, fontweight='bold')
    plt.xlabel("Experience (Years)", fontsize=12)
    plt.ylabel("Salary (k USD)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_mae.png', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()
    
    # ====== TASK 4: HUBER REGRESSION ======
    print(f"\n--- Task 4: Huber Regression ---")
    huber_model = HuberRegressor(epsilon=1.35, max_iter=200)
    huber_model.fit(X_reshaped, y)
    y_pred_huber = huber_model.predict(X_reshaped)
    
    mse_score_huber = mean_squared_error(y, y_pred_huber)
    mae_score_huber = mean_absolute_error(y, y_pred_huber)
    
    print(f"Huber Model: y = {huber_model.coef_[0]:.2f}x + {huber_model.intercept_:.2f}")
    print(f"  MSE: {mse_score_huber:.2f}")
    print(f"  MAE: {mae_score_huber:.2f}")
    print(f"  Epsilon (δ): {huber_model.epsilon}")
    
    # Plot Comparison of All Methods
    plt.figure(figsize=(12, 7))
    plt.scatter(X, y, color='gray', label='Data Points', alpha=0.5, s=50, zorder=1)
    plt.plot(X, y_pred_mse, color='red', linestyle='--', linewidth=2.5, 
             label=f'MSE (OLS): y={mse_model.coef_[0]:.2f}x+{mse_model.intercept_:.2f}', zorder=2)
    plt.plot(X, y_pred_mae, color='green', linestyle='-.', linewidth=2.5, 
             label=f'MAE (LAD): y={m_mae:.2f}x+{c_mae:.2f}', zorder=3)
    plt.plot(X, y_pred_huber, color='purple', linestyle='-', linewidth=2.5, 
             label=f'Huber: y={huber_model.coef_[0]:.2f}x+{huber_model.intercept_:.2f}', zorder=4)
    plt.title(f"Comparison of Loss Functions - {dataset_name}", fontsize=14, fontweight='bold')
    plt.xlabel("Experience (Years)", fontsize=12)
    plt.ylabel("Salary (k USD)", fontsize=12)
    plt.legend(fontsize=9, loc='best')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()
    
    # ====== TASK 5: COMPARATIVE ANALYSIS ======
    print("\n" + "-"*70)
    print("COMPARATIVE ANALYSIS REPORT")
    print("-"*70)
    
    # Store results for return
    results = {
        'mse': {'slope': mse_model.coef_[0], 'intercept': mse_model.intercept_, 
                'mse_score': mse_score, 'mae_score': mae_score_mse},
        'mae': {'slope': m_mae, 'intercept': c_mae, 
                'mse_score': mse_score_mae, 'mae_score': mae_score_mae},
        'huber': {'slope': huber_model.coef_[0], 'intercept': huber_model.intercept_, 
                  'mse_score': mse_score_huber, 'mae_score': mae_score_huber}
    }
    
    # Calculate residuals for outlier analysis
    residuals_mse = np.abs(y - y_pred_mse)
    residuals_mae = np.abs(y - y_pred_mae)
    residuals_huber = np.abs(y - y_pred_huber)
    
    max_residual_mse = np.max(residuals_mse)
    max_residual_mae = np.max(residuals_mae)
    
    print(f"\n1. MODEL PARAMETERS:")
    print(f"   MSE:   Slope={mse_model.coef_[0]:.4f}, Intercept={mse_model.intercept_:.4f}")
    print(f"   MAE:   Slope={m_mae:.4f}, Intercept={c_mae:.4f}")
    print(f"   Huber: Slope={huber_model.coef_[0]:.4f}, Intercept={huber_model.intercept_:.4f}")
    
    print(f"\n2. PERFORMANCE METRICS:")
    print(f"   MSE Model   - MSE: {mse_score:.2f}, MAE: {mae_score_mse:.2f}")
    print(f"   MAE Model   - MSE: {mse_score_mae:.2f}, MAE: {mae_score_mae:.2f}")
    print(f"   Huber Model - MSE: {mse_score_huber:.2f}, MAE: {mae_score_huber:.2f}")
    
    print(f"\n3. OUTLIER SENSITIVITY:")
    print(f"   Maximum Residual (MSE): {max_residual_mse:.2f}")
    print(f"   Maximum Residual (MAE): {max_residual_mae:.2f}")
    print(f"   Difference: {abs(max_residual_mse - max_residual_mae):.2f}")
    
    # Determine if dataset has outliers
    slope_difference = abs(mse_model.coef_[0] - m_mae)
    has_outliers = slope_difference > 0.5  # Threshold for significant difference
    
    if has_outliers:
        print(f"\n4. EFFECTS OF OUTLIERS:")
        print(f"   ⚠ Outliers detected! Slope difference: {slope_difference:.2f}")
        print(f"   - MSE regression is heavily influenced by outliers (squared penalty)")
        print(f"   - The MSE line is pulled toward extreme values")
        print(f"   - MAE and Huber remain robust, following the main trend")
        
        print(f"\n5. STRENGTHS & WEAKNESSES:")
        print(f"   MSE (Ordinary Least Squares):")
        print(f"   ✗ Highly sensitive to outliers due to squared error term")
        print(f"   ✗ Can produce misleading results with noisy data")
        print(f"   ✓ Efficient computation and differentiable everywhere")
        
        print(f"\n   MAE (Least Absolute Deviations):")
        print(f"   ✓ Robust to outliers (linear penalty)")
        print(f"   ✓ Represents the median trend, ignoring anomalies")
        print(f"   ✗ Computationally expensive (requires iterative optimization)")
        print(f"   ✗ Not differentiable at zero")
        
        print(f"\n   Huber Loss:")
        print(f"   ✓ Balanced approach: MSE-like for small errors, MAE-like for large errors")
        print(f"   ✓ Robust to outliers while maintaining differentiability")
        print(f"   ✓ Best of both worlds")
        print(f"   ✗ Requires tuning epsilon parameter")
        
        print(f"\n6. RECOMMENDATION:")
        print(f"   🎯 For this dataset: MAE or Huber Regression")
        print(f"   Reason: The presence of outliers makes MSE unsuitable.")
        print(f"           MAE/Huber capture the true underlying relationship.")
    else:
        print(f"\n4. EFFECTS OF OUTLIERS:")
        print(f"   ✓ No significant outliers detected (slope difference: {slope_difference:.2f})")
        print(f"   - All three methods produce nearly identical regression lines")
        print(f"   - The data follows a clear linear trend with minimal noise")
        
        print(f"\n5. STRENGTHS & WEAKNESSES:")
        print(f"   MSE (Ordinary Least Squares):")
        print(f"   ✓ Optimal for normally distributed errors")
        print(f"   ✓ Computationally efficient (closed-form solution)")
        print(f"   ✓ Provides Maximum Likelihood Estimation for Gaussian noise")
        print(f"   ✓ Differentiable everywhere")
        
        print(f"\n   MAE (Least Absolute Deviations):")
        print(f"   ○ No advantage over MSE in clean data")
        print(f"   ✗ Computationally more expensive")
        print(f"   ○ Would be beneficial if outliers were present")
        
        print(f"\n   Huber Loss:")
        print(f"   ○ Behaves like MSE when errors are small (within epsilon)")
        print(f"   ○ No significant advantage over MSE in clean data")
        print(f"   ○ Would provide robustness if data quality degrades")
        
        print(f"\n6. RECOMMENDATION:")
        print(f"   🎯 For this dataset: MSE (Linear Regression)")
        print(f"   Reason: Clean data with no outliers makes MSE the optimal choice.")
        print(f"           It's the standard, most efficient solution.")
    
    print("\n" + "="*70 + "\n")
    
    return results


# ====== MAIN EXECUTION ======
if __name__ == "__main__":
    print("\n" + "="*70)
    print(" MACHINE LEARNING ASSIGNMENT 02: LOSS FUNCTION ANALYSIS")
    print(" Comparing MSE, MAE, and Huber Loss Functions")
    print("="*70)
    
    # Analyze Clean Dataset
    try:
        results_clean = analyze_dataset(
            "salary_experience_clean.csv", 
            "Clean Dataset",
            "clean"
        )
    except FileNotFoundError:
        print("\n⚠ Warning: 'salary_experience_clean.csv' not found!")
        print("Please ensure the file is in the same directory as this script.\n")
    
    # Analyze Dataset with Outliers
    try:
        results_outliers = analyze_dataset(
            "salary_experience_with_outliers.csv", 
            "Dataset with Outliers",
            "outliers"
        )
    except FileNotFoundError:
        print("\n⚠ Warning: 'salary_experience_with_outliers.csv' not found!")
        print("Please ensure the file is in the same directory as this script.\n")
    
    print("\n" + "="*70)
    print(" ANALYSIS COMPLETE!")
    print(" Check the generated PNG files for visualizations.")
    print("="*70)