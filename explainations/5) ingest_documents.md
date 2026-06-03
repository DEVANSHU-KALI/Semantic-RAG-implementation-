# 📥 ingest_documents.py: Parsing, Vector Ingestion, and Batch Uploads

This document breaks down the document ingestion script in `backend/ingest_documents.py` section-by-section.

---

## 1. Code Walkthrough (Line-by-Line)

The ingestion script is responsible for reading local documents, chunking them, vectorizing them, and inserting them into the Qdrant database.

### Part A: Imports & Client Setup
```python
import os
from .embedding_model import embedding_model
from .text_chunker import text_splitter
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)
```
*   **What is happening in the code:** We import libraries for file navigation, model encoding, chunking, and database operations. We instantiate `QdrantClient` synchronously to connect to the database on port 6333.

### Part B: Reading Files & Semantic Chunking
```python
def ingest_documents(folder_path: str, collection_name: str):
    # REFACTOR NOTE: Introduced 'sources' list to map metadata correctly.
    documents = []
    ids = []
    sources = []
    counter = 0

    for filename in os.listdir(folder_path):
        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        chunks = text_splitter.create_documents([text])
        for chunk in chunks:
            documents.append(chunk.page_content)
            ids.append(counter)
            sources.append(filename) # Dynamic source file mapping
            counter += 1
```
*   **What is happening in the code:**
    1.  We define `ingest_documents` taking a folder path and collection name.
    2.  We initialize empty lists for chunk text (`documents`), IDs (`ids`), and file names (`sources`).
    3.  We loop through all `.txt` files in the directory, open them, and read their contents.
    4.  We call `text_splitter.create_documents([text])` to split the text into semantic chunks.
    5.  We loop through each chunk and append the text, a unique numeric ID, and the file name to their respective lists.
*   **Why we do it (The Fix):** The original script did not use a `sources` list. It referenced the outer loop's `filename` variable directly in payload creation, which meant all chunks were incorrectly tagged with the name of the *last* processed file. Collecting filenames in `sources` resolves this bug.

### Part C: Vector Encoding and Point Struct Construction
```python
    # Convert chunks to embeddings
    embeddings = embedding_model.encode(documents)

    points = []
    for i in range(len(documents)):
        points.append(
            PointStruct(
                id=ids[i],
                vector=embeddings[i].tolist(),
                payload={
                    "text": documents[i],
                    "source": sources[i] # Fixed source tag binding
                }
            )
        )
```
*   **What is happening in the code:**
    1.  We pass our collected text chunks (`documents`) to the embedding model to generate vectors in a single batch.
    2.  We initialize an empty list `points`.
    3.  We loop through all chunks, creating a `PointStruct` for each. We convert the NumPy vector to a standard list using `.tolist()` and bind the text and its source file name to the metadata payload.

### Part D: Database Upsert & Execution
```python
    # Upload to Qdrant
    client.upsert(
        collection_name=collection_name,
        points=points
    )

if __name__ == "__main__":
    ingest_documents("data/ai_papers", "ai_research_papers")
    ingest_documents("data/langchain_docs", "langchain_docs")
```
*   **What is happening in the code:**
    1.  We call `client.upsert` to write all point objects to the specified collection in one request.
    2.  In the `__name__ == "__main__"` block, we execute this ingestion for both of our collections.

---

## 2. Deep Technical Concepts

*   **Point:** The basic data unit stored in Qdrant collections. It consists of an ID, a vector, and a payload.
*   **Payload:** A dictionary of metadata (such as original text, source file paths, or categories) associated with a vector point, allowing for metadata filtering during searches.
*   **Upsert:** A database operation that inserts a new record if it does not exist, or updates it if the ID matches. This makes the ingestion script idempotent (runnable multiple times without duplicating data).

---

## 3. Architectural Choices and Alternatives

*   **Batch Processing:** Instead of uploading points one by one, we batch them in the `points` list and upload them in a single call. This reduces network overhead and speeds up the ingestion process.
