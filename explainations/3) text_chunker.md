# ✂️ text_chunker.py: Semantic Chunking & Interface Adapters

This document explains the code logic, step-by-step structure, and underlying AI concepts found in `backend/text_chunker.py`.

---

## 1. Code Walkthrough (Line-by-Line)

The script is divided into three key sections: imports, model wrapping, and chunker initialization.

### Part A: Imports
```python
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
```
*   **What is happening in the code:** We import two classes. `SemanticChunker` splits documents based on semantic transitions, and `HuggingFaceEmbeddings` is a wrapper class that adapts standard transformer models to be compatible with LangChain's pipeline.

### Part B: Creating the Interface Wrapper
```python
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```
*   **What is happening in the code:** We instantiate `HuggingFaceEmbeddings` and pass the name of our embedding model.
*   **Why we do it:** This acts as an **Interface Wrapper** (a design pattern that adapts the interface of one class to match what another class expects). 
    *   Our raw `SentenceTransformer` class uses a method called `.encode()` to generate embeddings.
    *   LangChain's chunking components expect an embeddings class that implements methods called `.embed_documents()` and `.embed_query()`.
    *   By wrapping our model with `HuggingFaceEmbeddings`, we adapt our local model to be compatible with the LangChain framework.

### Part C: Instantiating the Semantic Chunker
```python
text_splitter = SemanticChunker(
    embedding_model,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=75 
)
```
*   **What is happening in the code:** We create our chunker configuration object `text_splitter`. We pass it the wrapped `embedding_model` and set how splits are determined:
    *   `breakpoint_threshold_type="percentile"`: Instructs the chunker to evaluate boundaries using a percentile distribution of sentence similarity drops.
    *   `breakpoint_threshold_amount=75`: Tells it to split text only when the semantic difference between consecutive sentences is in the top 25% of all shifts found in the document.

---

## 2. Deep Technical Concepts

*   **Semantic Chunking:** A document-splitting technique that analyzes the meaning of text. It generates vector embeddings for sentences and tracks the semantic similarity between consecutive sentences. When similarity drops sharply, it assumes a new topic has started and splits the text. This prevents paragraphs from being cut in half awkwardly.
*   **Percentile Thresholding:** To find split points, the system calculates the semantic distance (`1 - CosineSimilarity`) between consecutive sentences. The differences are grouped into a distribution. A threshold of `75` means a split is created only when the difference falls in the **upper quartile (top 25%)** of all observed shifts.

---

## 3. Architectural Choices and Alternatives

When segmenting text for RAG pipelines, developers choose between structural and semantic splitting:

### Alternative A: Recursive Character Text Splitter (Structural Splitting)
*   **How it works:** It splits text using a hierarchical list of characters—starting with double newlines `\n\n` (paragraphs), then single newlines `\n` (sentences), and finally spaces ` ` (words)—until the chunks fit a target size (e.g., 500 characters) with a slight overlap (e.g., 50 characters).
*   **Pros:** Highly predictable, fast, requires no embedding model calculations.
*   **Cons:** Can split text in the middle of a topic, losing context.

### Alternative B: Semantic Chunker (Used Here)
*   **How it works:** It uses sentence embeddings to identify natural conceptual transitions.
*   **Pros:** High semantic coherence; ensures each chunk contains a complete topic.
*   **Cons:** Slower because it requires running an embedding model for every sentence in the document.
