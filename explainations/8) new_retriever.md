## 🔍 new_retriever.py: Async Retrieval & Vector Space Matching

This document explains `backend/new_retriever.py` section-by-section to show how vector similarity searches are handled.

---

## 1. Code Walkthrough (Line-by-Line)

The retriever script is responsible for querying our Qdrant vector database.

### Part A: Imports & Client Setup
```python
from qdrant_client import AsyncQdrantClient
from .embedding_model import embedding_model

client = AsyncQdrantClient(host="localhost", port=6333)
```
*   **What is happening in the code:** We import Qdrant's async client and our local embedding model. We instantiate the client pointing to localhost on port 6333.

### Part B: Query Vectorization and Collection Mapping
```python
async def retrieve_chunks(query: str, collection_name: str):
    query_vector = embedding_model.encode(query).tolist()

    if collection_name == "ai":
        collection = "ai_research_papers"
    else:
        collection = "langchain_docs"
```
*   **What is happening in the code:**
    1.  We define `retrieve_chunks` as an asynchronous function.
    2.  We pass the text query to our model `embedding_model.encode(query)` to convert it to a vector. We call `.tolist()` to convert the NumPy array into a standard Python list of floating-point numbers.
    3.  We check if `collection_name` equals `"ai"`. If it does, we route the search to the `"ai_research_papers"` collection; otherwise, we route it to the `"langchain_docs"` collection.

### Part C: Database Vector Search
```python
    results = await client.query_points(
        collection_name=collection,
        query=query_vector,
        limit=3
    )
```
*   **What is happening in the code:** We query the database using `client.query_points`. We pass the mapped collection name, the query vector, and a search limit parameter (`limit=3`). This executes a nearest-neighbor vector search.

### Part D: Parsing database points & safety defaults
```python
    results_list = []
    for point in results.points:
        results_list.append({
            "text": point.payload["text"],
            "source": point.payload.get("source", "unknown")
        })
    return results_list
```
*   **What is happening in the code:**
    1.  We iterate through the returned points list.
    2.  We extract the text content (`point.payload["text"]`) and the source filename (`point.payload.get("source", "unknown")`).
    3.  **Safety Check:** Using `.get("source", "unknown")` ensures that if a point payload is missing a source file key, the system defaults to `"unknown"` instead of raising a `KeyError` and crashing the server.

---

## 2. Deep Technical Concepts

*   **Vector Similarity Search:** The process of locating the database vectors closest to a query vector. The database calculates the geometric distance between vectors to identify semantically related text chunks.
*   **Top-K Retrieval (limit=3):** Specifies the number of nearest vectors to return. Setting this parameter requires balancing detail against cost: retrieving too many chunks (e.g. 10) can exceed the LLM's context window and increase API costs, while retrieving too few (e.g. 1) might miss crucial context.

---

## 3. Architectural Choices and Alternatives

### Why use direct Qdrant APIs instead of LangChain abstractions?
*   **Native Qdrant APIs:** Lightweight, execute faster, and provide direct access to database configurations and connection lifecycle controls.
*   **Alternatives (LangChain VectorStore Wrappers):** Standard LangChain wrappers (like `Qdrant.from_existing_collection()`) simplify initial prototyping but add abstraction overhead, making debugging database connections and tracking performance issues harder.