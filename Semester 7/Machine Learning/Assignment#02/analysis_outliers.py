import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.optimize import minimize

# --- Configuration ---
FILE_PATH = "salary_experience_with_outliers.csv"
DATASET_NAME = "Dataset with Outliers"

# --- Task 1: Data Exploration ---
print(f"--- Task 1: Data Exploration ({DATASET_NAME}) ---")
# Load dataset
df = pd.read_csv(FILE_PATH)
X = df['experience_years'].values
y = df['salary_k'].values

# Reshape X for sklearn (needs 2D array)
X_reshaped = X.reshape(-1, 1)

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='orange', label='Data Points (with Outliers)', alpha=0.6)
plt.title(f"Salary vs Experience ({DATASET_NAME})")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (k)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
plt.savefig('scatter_plot_outliers.png')
plt.close()
print("Scatter plot created. Visual inspection shows extreme outliers that deviate significantly from the main trend.\n")


# --- Task 2: Implement MSE Regression (Ordinary Least Squares) ---
print(f"--- Task 2: MSE Regression ({DATASET_NAME}) ---")
# Fit Linear Regression (minimizes MSE)
mse_model = LinearRegression()
mse_model.fit(X_reshaped, y)
y_pred_mse = mse_model.predict(X_reshaped)

# Calculate metrics
mse_mse = mean_squared_error(y, y_pred_mse)
mae_mse = mean_absolute_error(y, y_pred_mse)

print(f"MSE Model Coefficients: Slope={mse_model.coef_[0]:.2f}, Intercept={mse_model.intercept_:.2f}")
print(f"MSE (Mean Squared Error): {mse_mse:.2f}")
print(f"MAE (Mean Absolute Error): {mae_mse:.2f}")

# Plot MSE Regression
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='orange', label='Data Points', alpha=0.6)
plt.plot(X, y_pred_mse, color='red', linewidth=2, label='MSE Regression (OLS)')
plt.title(f"MSE Regression on {DATASET_NAME}")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (k)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
plt.savefig('mse_regression_outliers.png')
plt.close()
print("\n")


# --- Task 3: Implement MAE Regression (Least Absolute Deviations) ---
print(f"--- Task 3: MAE Regression ({DATASET_NAME}) ---")

# Define MAE loss function for optimization
def mae_loss_func(params, X_vals, y_vals):
    m, c = params
    y_pred = m * X_vals + c
    return np.sum(np.abs(y_vals - y_pred))

# Optimize to find best m (slope) and c (intercept)
initial_guess = [1, 1]
result = minimize(mae_loss_func, initial_guess, args=(X, y))
m_mae, c_mae = result.x
y_pred_mae = m_mae * X + c_mae

# Calculate metrics for MAE model
mse_mae_model = mean_squared_error(y, y_pred_mae)
mae_mae_model = mean_absolute_error(y, y_pred_mae)

print(f"MAE Model Coefficients: Slope={m_mae:.2f}, Intercept={c_mae:.2f}")
print(f"MSE (Mean Squared Error): {mse_mae_model:.2f}")
print(f"MAE (Mean Absolute Error): {mae_mae_model:.2f}")

# Plot MAE Regression
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='orange', label='Data Points', alpha=0.6)
plt.plot(X, y_pred_mae, color='green', linewidth=2, label='MAE Regression (LAD)')
plt.title(f"MAE Regression on {DATASET_NAME}")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (k)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
plt.savefig('mae_regression_outliers.png')
plt.close()
print("\n")


# --- Task 4: Implement Huber Regression ---
print(f"--- Task 4: Huber Regression ({DATASET_NAME}) ---")
# Fit Huber Regressor
# epsilon=1.35 is standard; smaller epsilon makes it more resistant to outliers (closer to MAE)
huber_model = HuberRegressor(epsilon=1.35)
huber_model.fit(X_reshaped, y)
y_pred_huber = huber_model.predict(X_reshaped)

# Calculate metrics
mse_huber = mean_squared_error(y, y_pred_huber)
mae_huber = mean_absolute_error(y, y_pred_huber)

print(f"Huber Model Coefficients: Slope={huber_model.coef_[0]:.2f}, Intercept={huber_model.intercept_:.2f}")
print(f"MSE (Mean Squared Error): {mse_huber:.2f}")
print(f"MAE (Mean Absolute Error): {mae_huber:.2f}")

# Plot All Comparisons
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='gray', label='Data Points', alpha=0.5)
plt.plot(X, y_pred_mse, color='red', linestyle='--', linewidth=2, label='MSE (OLS)')
plt.plot(X, y_pred_mae, color='green', linestyle='-.', linewidth=2, label='MAE (LAD)')
plt.plot(X, y_pred_huber, color='purple', linestyle='-', linewidth=2, label='Huber')
plt.title(f"Comparison of Loss Functions on {DATASET_NAME}")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (k)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
plt.savefig('huber_regression_outliers.png')
plt.close()
print("\n")


# --- Task 5: Comparative Analysis Report ---
print("="*50)
print(f"COMPARATIVE ANALYSIS REPORT: {DATASET_NAME}")
print("="*50)
print("1. Effects of Outliers:")
print("   - The outliers significantly pull the MSE regression line towards them.")
print(f"   - MSE Slope: {mse_model.coef_[0]:.2f} (Distorted by outliers)")
print(f"   - MAE Slope: {m_mae:.2f} (Robust, ignores outliers)")
print(f"   - Huber Slope: {huber_model.coef_[0]:.2f} (Robust, similar to MAE)")

print("\n2. Strengths and Weaknesses (Context of Noisy Data):")
print("   - MSE: Highly sensitive to outliers. The squared term penalizes large errors heavily, causing the model to skew to accommodate anomalies.")
print("   - MAE: Very robust. It treats all deviations linearly, so a few extreme points don't shift the line much.")
print("   - Huber: A balanced approach. It is robust like MAE for large errors (linear loss) but differentiable at 0 like MSE (quadratic loss).")

print("\n3. Conclusion:")
print("   - For this noisy dataset, MAE or Huber Regression is most suitable.")
print("   - Reason: They provide a model that represents the majority of the data ('the trend') rather than trying to fit the anomalies.")
print("   - MSE is a poor choice here as it fails to capture the true underlying relationship due to the outliers.")
print("="*50)
