from backend.embedding_model import embedding_model

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


sentences = [
    "What is LangChain?",
    "Explain LangChain framework",
    "How do retrievers work in LangChain?",
    "What is a transformer model?",
    "Explain attention mechanism",
    "Machine learning algorithms"
]


embeddings = embedding_model.encode(sentences)


pca = PCA(n_components=3)

reduced_vectors = pca.fit_transform(embeddings)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for i, sentence in enumerate(sentences):

    x = reduced_vectors[i][0]
    y = reduced_vectors[i][1]
    z = reduced_vectors[i][2]

    ax.scatter(x, y, z)

    ax.text(x, y, z, sentence)


ax.set_title("3D Visualization of Sentence Embeddings")

plt.show()