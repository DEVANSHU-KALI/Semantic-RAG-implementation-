## 🧪 testing_scripts: Connection Checks & PCA Embedding Projections

This document breaks down the connection test and visualization scripts under the `testing/` directory section-by-section.

---

## 1. Code Walkthrough (Line-by-Line)

### Script A: Connection Check (`test_connection.py`)

#### Step 1: Imports & Client Setup
```python
# REFACTOR NOTE: Corrected client import path.
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)
```
*   **What is happening in the code:** We import `QdrantClient` directly from `qdrant_client`. We instantiate it synchronously on port 6333.
*   **Why we do it (The Fix):** The original script imported the client from `backend.qdrant_db`, which was a bug because that file does not export a synchronous client class. Importing it directly from the library resolves this import error.

#### Step 2: Verification Loop
```python
try:
    collections = client.get_collections()

    print("\nConnected to Qdrant successfully!\n")
    print("Collections available:")
    for collection in collections.collections:
        print("-", collection.name)

except Exception as e:
    print("Connection failed:", e)
```
*   **What is happening in the code:** We call `client.get_collections()` inside a `try-except` block. If Qdrant is online, we print a success message and list all collections. If it is offline, we catch the exception and print a connection failure message.

---

### Script B: Embedding Visualization (`visualize_embeddings.py`)

#### Step 1: Imports & Sentences Definition
```python
from backend.embedding_model import embedding_model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

sentences = [
    "What is LangChain?",
    "Explain LangChain framework",
    ...
]
```
*   **What is happening in the code:** We import our local embedding model, NumPy, Matplotlib for plotting, and the PCA class from scikit-learn. We define a list of test sentences.

#### Step 2: Vectorization & PCA Dimensionality Reduction
```python
embeddings = embedding_model.encode(sentences)

pca = PCA(n_components=3)
reduced_vectors = pca.fit_transform(embeddings)
```
*   **What is happening in the code:**
    1.  We call `embedding_model.encode(sentences)` to convert our test sentences into 384-dimensional dense vectors.
    2.  We instantiate the PCA class, setting `n_components=3`.
    3.  We call `pca.fit_transform(embeddings)`. This reduces our 384-dimensional vectors into 3-dimensional coordinates.

#### Step 3: Graph Rendering
```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i, sentence in enumerate(sentences):
    x = reduced_vectors[i][0]
    y = reduced_vectors[i][1]
    z = reduced_vectors[i][2]

    ax.scatter(x, y, z)
    ax.text(x, y, z, sentence)

plt.show()
```
*   **What is happening in the code:**
    1.  We create a Matplotlib figure and set it to a 3D projection.
    2.  We loop through our sentences, retrieve the reduced coordinates ($X, Y, Z$), and plot them as points using `scatter`.
    3.  We render the corresponding text labels next to each point and display the plot window.

---

## 2. Deep Technical Concepts

*   **Principal Component Analysis (PCA):** A dimensionality reduction technique that projects high-dimensional data (e.g. 384 dimensions) onto a lower-dimensional space (e.g. 3 dimensions) by finding the directions of maximum variance in the data.
*   **Dimensionality Reduction:** Necessary for visualization because human spatial perception is limited to three dimensions, making it impossible to visualize raw 384-dimensional coordinates directly.

---

## 3. Architectural Choices and Alternatives

### Why use PCA for visualization?
*   **PCA (Used Here):** Fast, deterministic, and preserves global distances between points.
*   **Alternatives (t-SNE or UMAP):** Advanced non-linear techniques that excel at capturing local clusters in complex datasets. However, they are non-deterministic, computationally expensive, and can distort global relationships, making them less suitable for simple sanity checks.
- this is optional thing to go with, you can visualize or not. but you get a understanding on it.