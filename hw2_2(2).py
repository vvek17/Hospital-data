#What is the minimal number of principal components needed to retain 80% of data variance?  

import numpy as np
import cv2
from sklearn.decomposition import PCA

# 1. Load the image
img = cv2.imread('hw2_Face.pbm', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: hw2_Face.pbm not found. Please ensure the file is in the directory.")
else:
    # 2. Fit PCA using all possible components
    pca = PCA()
    pca.fit(img)

    # 3. Calculate the cumulative sum of the explained variance ratio
    # This shows the total variance captured as we add more components
    cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

    # 4. Find the first index where cumulative variance is >= 0.80
    # We add 1 because indices start at 0
    n_components_80 = np.argmax(cumulative_variance >= 0.80) + 1

    print(f"The minimal number of components to retain 80% variance is: {n_components_80}")
    
    # Optional: Print the exact variance captured by that many components
    print(f"Exact variance retained: {cumulative_variance[n_components_80 - 1]:.4f}")




