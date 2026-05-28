# 🤖 Machine Learning (CS-341)

Welcome to the **Machine Learning** course directory! This folder houses comprehensive lecture slides, the official syllabus, and **five major programming assignments** built completely from scratch during Semester 7.

The defining hallmark of this course is that **no high-level machine learning frameworks (e.g., scikit-learn, PyTorch, Keras, TensorFlow) were used**. All mathematical engines, linear algebra projections, clustering optimizations, and Recurrent Neural Network backpropagation layers were programmed strictly using base Python and Numpy.

---

## 📂 Directory Contents

This directory contains the following academic resources:

*   **📘 Course Syllabus**:
    *   [Course Outline CS-341 Machine Learning.pdf](./Course%20Outline%20CS-341%20Machine%20Learning.pdf) — Complete course roadmap covering learning milestones, grading plans, and textbook details.
*   **📑 Lecture Notes (01 Introduction to 12 FCN UNet)**:
    *   Detailed slide decks covering:
        1.  *Introduction & Linear Models*
        2.  *Neural Networks & Perceptron mathematics*
        3.  *Activation functions & Gradient Descent variations*
        4.  *Backpropagation calculations (from single nodes to deep layers)*
        5.  *Convolutional Neural Networks (CNNs) & Spatial Filters*
        6.  *Loss functions & Advanced Optimizers (SGD, Adam, RMSprop)*
        7.  *Recurrent Neural Networks (RNN) & Long Short-Term Memory (LSTM)*
        8.  *Fully Convolutional Networks (FCN) & UNet Architectures*
*   **✍️ Programming Assignments (From Scratch)**:
    *   This repository archives five highly intensive, custom-developed programming tasks:

| Assignment | Algorithm Focus | Key Implementation Features | Documentation |
| :--- | :--- | :--- | :---: |
| **[Assignment #01](./Assignment%2301/)** | K-Means, DBSCAN, & KNN | Developed clustering and classification engines to evaluate convex vs. noisy complex datasets. | [Explore](./Assignment%2301/README.md) |
| **[Assignment #02](./Assignment%2302/)** | Linear Regression & Outliers | Analyzed performance variances on clean vs. noisy salary data under MSE & MAE loss models. | [Explore](./Assignment%2302/README.md) |
| **[Assignment #03](./Assignment%2303/)** | Linear Discriminant Analysis | Calculated high-dimensional scattering matrices to project and classify multi-class datasets in 3D. | [Explore](./Assignment%2303/README.md) |
| **[Assignment #04](./Assignment%2304/)** | Principal Component Analysis | Performed covariance analysis and singular value decompositions to compress 3D dimensions to 2D/1D. | [Explore](./Assignment%2304/README.md) |
| **[Assignment #05](./Assignment%2305/)** | Long Short-Term Memory RNN | Created an entire Recurrent Neural Network with gate-states (forget, input, output) and backpropagation. | [Explore](./Assignment%2305/README.md) |

---

## 🧠 Major Learning Milestones

### 1. Hardcore Mathematical Translation
Implementing these algorithms without library abstractions required deriving and programming:
*   **Distance Metrics**: Euclidean, Manhattan, and custom spatial indices.
*   **Optimization**: Custom SGD solvers, computing partial derivatives for weights, and backpropagation chains.
*   **Matrix Algebra**: Covariance matrices, eigenvectors, eigenvalues, and projection matrices.
*   **Loss Functions**: Direct implementation of Mean Squared Error, Mean Absolute Error, Binary Cross-Entropy, and LSTMs.

### 2. High-Performance Scientific Python
*   **Vectorization**: Utilizing Numpy vectorization patterns (`np.dot`, broadcasting, advanced indexing) to replace slow Python loops.
*   **Data Analysis**: Designing custom pipelines in Pandas to load, clean, and normalize messy datasets.
*   **Advanced Visualizations**: Leveraging Matplotlib and Seaborn to construct 3D point projections, decision boundary planes, confusion matrices, and time-series loss progressions.

---

*Navigate to any of the individual Assignment folders to inspect the Python source codes, complex datasets, custom-generated plots, and comprehensive PDF reports!*
