# 🧬 embedding_model.py: Vector Embedding Generation

This document explains the codebase logic, code structure, and core AI concepts found in `backend/embedding_model.py`. It is structured to help beginners read the code side-by-side with this explanation while learning advanced technical interview details.

---

## 1. Code Walkthrough (Line-by-Line)

The script `backend/embedding_model.py` is very concise, containing only two main execution parts:

### Part A: Importing the Library
```python
from sentence_transformers import SentenceTransformer
```
*   **What is happening in the code:** Here, we import the `SentenceTransformer` class from the `sentence-transformers` library (a Python framework built on top of PyTorch for generating state-of-the-art sentence and document embeddings).
*   **Why we do it:** This gives us access to pre-trained transformer architectures specifically optimized for semantic text matching.

### Part B: Initializing the Model
```python
# load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
```
*   **What is happening in the code:** We create an instance of the `SentenceTransformer` class, naming it `embedding_model`. We pass the string `"all-MiniLM-L6-v2"` as the model identifier.
*   **Why we do it:** When this line runs, the library checks if the model weights are already downloaded locally. If not, it downloads them from the Hugging Face hub. Once loaded, the `embedding_model` object is ready to convert any input text into vector representations.

---

## 2. Deep Technical Concepts

To explain this script in an interview, you should understand these concepts:

*   **Embeddings:** An **Embedding** (a dense vector (a list of continuous floating-point numbers representing features in a high-dimensional space)) translates human language into coordinates in a geometric space. Computes do not read characters; they analyze numbers.
*   **Dense vs. Sparse Vectors:** 
    *   **Dense Vectors:** Vectors where almost all elements are non-zero. They represent semantic concepts in a compact space (e.g. 384 numbers).
    *   **Sparse Vectors:** Vectors where most elements are zero (e.g. TF-IDF or BM25 keyword frequencies across a vocabulary of 50,000 words). They excel at keyword matching but fail at understanding synonyms or conceptual context.
*   **Dimensions (384D):** The `"all-MiniLM-L6-v2"` model maps text to a coordinate vector of **384 numbers**. Each dimension represents a latent feature (an abstract, hidden semantic attribute, such as tone, tense, domain, or subject relationship). Words or sentences with similar meanings will align close to each other in this 384-dimensional space.

---

## 3. Architectural Choices and Alternatives

In RAG development, choosing an embedding model involves balancing speed, accuracy, and operational constraints:

| Model | Dimensions | Deployment Type | Pros | Cons |
| :--- | :---: | :--- | :--- | :--- |
| **`all-MiniLM-L6-v2`** (Used Here) | 384 | Local (CPU/GPU) | Incredibly fast, runs offline, zero API costs, small memory footprint. | Shorter context window (256 tokens), lower semantic accuracy for complex syntax. |
| **`nomic-embed-text-v1.5`** | 768 | Local (CPU/GPU) | Larger context window (8192 tokens), supports Matryoshka learning. | Requires `einops` (Einstein operations for tensor manipulation) library, higher memory usage. |
| **`text-embedding-3-small`** | 1536 | Cloud API (OpenAI) | Top-tier accuracy, zero local compute overhead. | Requires active internet, incurs API costs, introduces network latency. |
