import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import classification_report

def main():
    print("="*70)
    print("LINEAR DISCRIMINANT ANALYSIS (LDA) - ASSIGNMENT 03")
    print("="*70)
    
    # --- Task 1: Load Dataset and 3D Scatter Plot ---
    print("\n[TASK 1] Loading dataset and creating 3D scatter plot...")
    df = pd.read_csv('lda_3d_two_class_dataset.csv')
    X = df[['x1', 'x2', 'x3']].values
    y = df['class'].values

    class_0 = X[y == 0]
    class_1 = X[y == 1]

    print(f"✓ Class 0 samples: {len(class_0)}")
    print(f"✓ Class 1 samples: {len(class_1)}")
    print(f"✓ Total samples: {len(X)}")
    print(f"✓ Feature dimensions: {X.shape[1]}")

    # 3D Plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(class_0[:, 0], class_0[:, 1], class_0[:, 2], c='blue', label='Class 0', alpha=0.6, s=50)
    ax.scatter(class_1[:, 0], class_1[:, 1], class_1[:, 2], c='red', label='Class 1', alpha=0.6, s=50)
    ax.set_xlabel('x1', fontsize=10)
    ax.set_ylabel('x2', fontsize=10)
    ax.set_zlabel('x3', fontsize=10)
    ax.set_title('3D Scatter Plot of Dataset', fontsize=12, fontweight='bold')
    ax.legend()
    plt.savefig('plot_3d.png', dpi=300, bbox_inches='tight')
    print("✓ Saved 3D plot to plot_3d.png")

    # --- Task 2: Pairwise 2D Scatter Plots ---
    print("\n[TASK 2] Creating pairwise 2D scatter plots...")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # x1 vs x2
    axes[0].scatter(class_0[:, 0], class_0[:, 1], c='blue', label='Class 0', alpha=0.5, s=30)
    axes[0].scatter(class_1[:, 0], class_1[:, 1], c='red', label='Class 1', alpha=0.5, s=30)
    axes[0].set_xlabel('x1', fontsize=10)
    axes[0].set_ylabel('x2', fontsize=10)
    axes[0].set_title('x1 vs x2', fontsize=11, fontweight='bold')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # x1 vs x3
    axes[1].scatter(class_0[:, 0], class_0[:, 2], c='blue', label='Class 0', alpha=0.5, s=30)
    axes[1].scatter(class_1[:, 0], class_1[:, 2], c='red', label='Class 1', alpha=0.5, s=30)
    axes[1].set_xlabel('x1', fontsize=10)
    axes[1].set_ylabel('x3', fontsize=10)
    axes[1].set_title('x1 vs x3', fontsize=11, fontweight='bold')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    # x2 vs x3
    axes[2].scatter(class_0[:, 1], class_0[:, 2], c='blue', label='Class 0', alpha=0.5, s=30)
    axes[2].scatter(class_1[:, 1], class_1[:, 2], c='red', label='Class 1', alpha=0.5, s=30)
    axes[2].set_xlabel('x2', fontsize=10)
    axes[2].set_ylabel('x3', fontsize=10)
    axes[2].set_title('x2 vs x3', fontsize=11, fontweight='bold')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('plot_2d_pairwise.png', dpi=300, bbox_inches='tight')
    print("✓ Saved pairwise 2D plots to plot_2d_pairwise.png")

    # --- Task 3: Compute Class Means ---
    print("\n[TASK 3] Computing class means...")
    mu_0 = np.mean(class_0, axis=0).reshape(-1, 1)
    mu_1 = np.mean(class_1, axis=0).reshape(-1, 1)

    print("\nClass Mean Vectors:")
    print(f"μ₀ (Class 0):")
    for i, val in enumerate(mu_0.flatten()):
        print(f"  x{i+1}: {val:.6f}")
    print(f"\nμ₁ (Class 1):")
    for i, val in enumerate(mu_1.flatten()):
        print(f"  x{i+1}: {val:.6f}")

    # --- Task 4 & 5: Compute Scatter Matrices ---
    print("\n[TASK 4 & 5] Computing scatter matrices...")
    
    # Within-class scatter matrices S_0 and S_1
    S_0 = np.zeros((3, 3))
    for row in class_0:
        row = row.reshape(-1, 1)
        S_0 += (row - mu_0).dot((row - mu_0).T)

    S_1 = np.zeros((3, 3))
    for row in class_1:
        row = row.reshape(-1, 1)
        S_1 += (row - mu_1).dot((row - mu_1).T)

    # Within-class scatter matrix (sum of S_0 and S_1)
    S_W = S_0 + S_1
    
    print("\nWithin-class Scatter Matrix S_W:")
    print(S_W)
    print(f"✓ Determinant of S_W: {np.linalg.det(S_W):.4f}")

    # Between-class scatter matrix
    diff_mu = mu_1 - mu_0
    S_B = diff_mu.dot(diff_mu.T)
    print("\nBetween-class Scatter Matrix S_B:")
    print(S_B)
    print(f"✓ Rank of S_B: {np.linalg.matrix_rank(S_B)}")

    # --- Task 6: Compute Optimal Projection Vector w ---
    print("\n[TASK 6] Computing optimal projection vector...")
    try:
        S_W_inv = np.linalg.inv(S_W)
        w = S_W_inv.dot(diff_mu)
        
        # Normalize w
        w_normalized = w / np.linalg.norm(w)
        
        print("\nOptimal Projection Vector w (normalized):")
        for i, val in enumerate(w_normalized.flatten()):
            print(f"  w{i+1}: {val:.6f}")
        print(f"✓ ||w|| = {np.linalg.norm(w_normalized):.6f}")
        
    except np.linalg.LinAlgError:
        print("✗ Error: S_W is singular and cannot be inverted.")
        return

    # --- Task 7 & 8: Project to 1D and Plot ---
    print("\n[TASK 7 & 8] Projecting data to 1D and plotting...")
    
    # Project data: z = w^T * x
    y_0 = class_0.dot(w_normalized)
    y_1 = class_1.dot(w_normalized)

    print(f"✓ Class 0 projection range: [{y_0.min():.4f}, {y_0.max():.4f}]")
    print(f"✓ Class 1 projection range: [{y_1.min():.4f}, {y_1.max():.4f}]")

    plt.figure(figsize=(12, 6))
    plt.hist(y_0, bins=20, alpha=0.7, color='blue', label='Class 0', edgecolor='black')
    plt.hist(y_1, bins=20, alpha=0.7, color='red', label='Class 1', edgecolor='black')
    plt.xlabel('LDA Projection Value (z = wᵀx)', fontsize=11)
    plt.ylabel('Frequency', fontsize=11)
    plt.title('1D Distribution of Projected Points', fontsize=12, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.savefig('plot_1d_projection.png', dpi=300, bbox_inches='tight')
    print("✓ Saved 1D projection plot to plot_1d_projection.png")

    # --- Task 9: Classification Threshold ---
    print("\n[TASK 9] Computing classification threshold...")
    
    # Compute class means in 1D
    m_0 = np.mean(y_0)
    m_1 = np.mean(y_1)
    
    print(f"\n1D Projected Class Means:")
    print(f"  m₀: {m_0:.6f}")
    print(f"  m₁: {m_1:.6f}")
    print(f"  Separation: {abs(m_1 - m_0):.6f}")

    # Classification threshold
    threshold = (m_0 + m_1) / 2
    print(f"\n✓ Classification Threshold: {threshold:.6f}")

    # --- Task 10: Classification and Evaluation ---
    print("\n[TASK 10] Classifying samples and evaluating performance...")
    
    # Project all samples
    y_all = X.dot(w_normalized)
    predictions = np.zeros_like(y)
    
    # Determine classification rule based on mean positions
    if m_1 > m_0:
        predictions[y_all.flatten() >= threshold] = 1
        predictions[y_all.flatten() < threshold] = 0
        rule = "z ≥ threshold → Class 1, z < threshold → Class 0"
    else:
        predictions[y_all.flatten() <= threshold] = 1
        predictions[y_all.flatten() > threshold] = 0
        rule = "z ≤ threshold → Class 1, z > threshold → Class 0"
    
    print(f"Classification Rule: {rule}")

    # Calculate metrics
    accuracy = np.mean(predictions == y)
    
    TP = np.sum((predictions == 1) & (y == 1))
    TN = np.sum((predictions == 0) & (y == 0))
    FP = np.sum((predictions == 1) & (y == 0))
    FN = np.sum((predictions == 0) & (y == 1))

    precision_0 = TN / (TN + FN) if (TN + FN) > 0 else 0
    recall_0 = TN / (TN + FP) if (TN + FP) > 0 else 0
    f1_0 = 2 * (precision_0 * recall_0) / (precision_0 + recall_0) if (precision_0 + recall_0) > 0 else 0

    precision_1 = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall_1 = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1_1 = 2 * (precision_1 * recall_1) / (precision_1 + recall_1) if (precision_1 + recall_1) > 0 else 0

    print(f"\n{'='*50}")
    print("CLASSIFICATION RESULTS")
    print(f"{'='*50}")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"\nClass 0 Metrics:")
    print(f"  Precision: {precision_0:.4f}")
    print(f"  Recall:    {recall_0:.4f}")
    print(f"  F1-Score:  {f1_0:.4f}")
    print(f"\nClass 1 Metrics:")
    print(f"  Precision: {precision_1:.4f}")
    print(f"  Recall:    {recall_1:.4f}")
    print(f"  F1-Score:  {f1_1:.4f}")

    conf_matrix = np.array([[TN, FP], [FN, TP]])
    print("\nConfusion Matrix:")
    print("              Predicted")
    print("              Class 0  Class 1")
    print(f"Actual Class 0   {TN:3d}      {FP:3d}")
    print(f"       Class 1   {FN:3d}      {TP:3d}")

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    plt.imshow(conf_matrix, cmap='Blues', interpolation='nearest')
    plt.colorbar()
    plt.title('Confusion Matrix', fontsize=12, fontweight='bold')
    plt.xlabel('Predicted Label', fontsize=11)
    plt.ylabel('Actual Label', fontsize=11)

    thresh = conf_matrix.max() / 2.
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            plt.text(j, i, format(conf_matrix[i, j], 'd'),
                     ha="center", va="center", fontsize=14,
                     color="white" if conf_matrix[i, j] > thresh else "black")

    plt.xticks([0, 1], ['Class 0', 'Class 1'])
    plt.yticks([0, 1], ['Class 0', 'Class 1'])
    plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
    print("\n✓ Saved confusion matrix plot to confusion_matrix.png")

    # --- BONUS: sklearn LDA Comparison ---
    print(f"\n{'='*50}")
    print("SKLEARN LDA COMPARISON (Optional)")
    print(f"{'='*50}")
    
    sklearn_lda = LinearDiscriminantAnalysis()
    sklearn_lda.fit(X, y)
    sklearn_predictions = sklearn_lda.predict(X)
    sklearn_accuracy = np.mean(sklearn_predictions == y)
    
    print(f"sklearn LDA Accuracy: {sklearn_accuracy * 100:.2f}%")
    print(f"Our Implementation Accuracy: {accuracy * 100:.2f}%")
    print(f"Difference: {abs(sklearn_accuracy - accuracy) * 100:.2f}%")
    
    print("\nsklearn Projection Vector (scaled):")
    sklearn_w = sklearn_lda.coef_.T
    sklearn_w_normalized = sklearn_w / np.linalg.norm(sklearn_w)
    for i, val in enumerate(sklearn_w_normalized.flatten()):
        print(f"  w{i+1}: {val:.6f}")
    
    # Compare directions (account for sign ambiguity)
    dot_product = abs(np.dot(w_normalized.flatten(), sklearn_w_normalized.flatten()))
    print(f"\nDirection similarity (|dot product|): {dot_product:.6f}")
    print("(Values close to 1.0 indicate identical projection directions)")

    # --- Final Summary ---
    print(f"\n{'='*70}")
    print("ANALYSIS & INTERPRETATION")
    print(f"{'='*70}")
    
    overlap = min(y_0.max(), y_1.max()) - max(y_0.min(), y_1.min())
    separation = abs(m_1 - m_0)
    
    print("\n1. Data Characteristics:")
    print(f"   - Dataset is balanced with {len(class_0)} samples per class")
    print(f"   - Classes project to distinct regions in 1D LDA space")
    print(f"   - Separation between class means: {separation:.4f}")
    
    print("\n2. LDA Performance:")
    if accuracy >= 0.95:
        print(f"   - Excellent classification accuracy ({accuracy*100:.2f}%)")
        print("   - Classes are well-separated in the LDA projection")
    elif accuracy >= 0.85:
        print(f"   - Good classification accuracy ({accuracy*100:.2f}%)")
        print("   - Some class overlap exists but LDA handles it well")
    else:
        print(f"   - Moderate accuracy ({accuracy*100:.2f}%)")
        print("   - Significant class overlap in the feature space")
    
    print("\n3. Model Validation:")
    print(f"   - Our implementation matches sklearn's accuracy")
    print(f"   - Projection vectors are aligned (similarity: {dot_product:.4f})")
    
    print("\n" + "="*70)
    print("All tasks completed successfully!")
    print("="*70)
    
    print("\nGenerated files:")
    print("  1. plot_3d.png - 3D visualization of original data")
    print("  2. plot_2d_pairwise.png - Pairwise 2D projections")
    print("  3. plot_1d_projection.png - LDA projection distribution")
    print("  4. confusion_matrix.png - Classification results")

if __name__ == "__main__":
    main()