import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import cv2

# 1. Load the specific PBM image
# Ensure 'hw2_Face.pbm' is in the same folder as your script
img = cv2.imread('hw2_Face.pbm', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not find 'hw2_Face.pbm'. Check the file path.")
else:
    n_components_list = [2, 5, 10]
    
    # Setup plotting: 1 row for original, plus 3 for the reconstructions
    plt.figure(figsize=(12, 8))
    
    # Show Original
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')
    
    # 2. Loop through components and reconstruct
    for i, n in enumerate(n_components_list):
        pca = PCA(n_components=n)
        
        # PCA identifies the most important "column patterns"
        img_transformed = pca.fit_transform(img)
        img_reconstructed = pca.inverse_transform(img_transformed)
        
        # Subplot positioning
        plt.subplot(2, 2, i + 2)
        plt.imshow(img_reconstructed, cmap='gray')
        plt.title(f"PCA Reconstruction ({n} PCs)")
        plt.axis('off')
        
        # Accessing Eigenvalues and Eigenvectors for the assignment
        print(f"Components: {n}")
        print(f"Top Eigenvalue (Variance): {pca.explained_variance_[0]:.2f}")
        # pca.components_ contains the eigenvectors
        
    plt.tight_layout()
    plt.show()