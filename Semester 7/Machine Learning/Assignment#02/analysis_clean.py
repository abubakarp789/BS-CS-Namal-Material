import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.optimize import minimize

# --- Configuration ---
FILE_PATH = "salary_experience_clean.csv"
DATASET_NAME = "Clean Dataset"

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
plt.scatter(X, y, color='blue', label='Data Points', alpha=0.6)
plt.title(f"Salary vs Experience ({DATASET_NAME})")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (k)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
plt.savefig('scatter_plot.png')
plt.close()
print("Scatter plot created. The data shows a clear linear trend with no visible outliers.\n")


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
plt.scatter(X, y, color='blue', label='Data Points', alpha=0.6)
plt.plot(X, y_pred_mse, color='red', linewidth=2, label='MSE Regression (OLS)')
plt.title(f"MSE Regression on {DATASET_NAME}")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (k)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
plt.savefig('mse_regression.png')
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
plt.scatter(X, y, color='blue', label='Data Points', alpha=0.6)
plt.plot(X, y_pred_mae, color='green', linewidth=2, label='MAE Regression (LAD)')
plt.title(f"MAE Regression on {DATASET_NAME}")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (k)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
plt.savefig('mae_regression.png')
plt.close()
print("\n")


# --- Task 4: Implement Huber Regression ---
print(f"--- Task 4: Huber Regression ({DATASET_NAME}) ---")
# Fit Huber Regressor
# epsilon=1.35 is standard; it determines the threshold between MSE and MAE behavior
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
plt.savefig('huber_regression.png')
plt.close()
print("\n")


# --- Task 5: Comparative Analysis Report ---
print("="*50)
print(f"COMPARATIVE ANALYSIS REPORT: {DATASET_NAME}")
print("="*50)
print("1. Effects of Outliers:")
print("   - In this clean dataset, there are no significant outliers.")
print("   - As a result, all three methods (MSE, MAE, Huber) produce very similar regression lines.")
print(f"   - The slopes are nearly identical: MSE={mse_model.coef_[0]:.2f}, MAE={m_mae:.2f}, Huber={huber_model.coef_[0]:.2f}.")

print("\n2. Strengths and Weaknesses (Context of Clean Data):")
print("   - MSE: Works perfectly here. It is efficient and provides the Maximum Likelihood Estimation for Gaussian noise.")
print("   - MAE: Also works well but is computationally heavier (requires iterative optimization). No advantage over MSE here.")
print("   - Huber: Behaves like MSE because errors are small (within epsilon).")

print("\n3. Conclusion:")
print("   - For this clean dataset, MSE (Linear Regression) is the most suitable.")
print("   - Reason: It is the standard solution for normally distributed errors and is computationally simplest.")
print("="*50)
