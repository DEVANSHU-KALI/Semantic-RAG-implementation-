## 🔗 rag_pipeline.py: Pipeline Orchestration and Synthesis

This document breaks down the RAG generation orchestration in `backend/rag_pipeline.py` section-by-section.

---

## 1. Code Walkthrough (Line-by-Line)

The orchestration script ties together routing, retrieval, and LLM text generation.

### Part A: Imports & Setup
```python
from openai import AsyncOpenAI
from dotenv import load_dotenv
from .query_router import route_query
from .new_retriever import retrieve_chunks

load_dotenv()
client = AsyncOpenAI()
```
*   **What is happening in the code:** We import modules for OpenAI API calls, environment variable loading, and our query routing and retrieval subsystems. We load variables from our `.env` file and instantiate the `AsyncOpenAI` client.

### Part B: Query Routing and Semantic Retrieval
```python
async def generate_answer(query):
    collection_name = await route_query(query)
    results = await retrieve_chunks(query, collection_name)
```
*   **What is happening in the code:** 
    1.  We define `generate_answer` as an asynchronous function.
    2.  We pass the query to the query router using `await route_query(query)`. The router returns either `"ai"` or `"langchain_docs"`.
    3.  We pass the query and target collection name to the retriever: `await retrieve_chunks(...)`. The retriever returns the top 3 semantically relevant text chunks.

### Part C: Printing Citations and Context Construction
```python
    for r in results:
        print(f"source: {r['source']}")

    context = "\n\n".join([r["text"] for r in results])
```
*   **What is happening in the code:**
    1.  We loop through our results and print the source filename for each chunk to the console, providing a clear lineage audit trace.
    2.  We construct a single string `context` by joining the retrieved chunk texts with double newlines.

### Part D: Prompt Engineering and LLM Generation
```python
    prompt = f"Context:\n{context}\n\nQuestion: {query}"

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
```
*   **What is happening in the code:**
    1.  We construct the final instruction string `prompt`, wrapping the retrieved facts (`context`) and the user's question.
    2.  We call `await client.chat.completions.create(...)`, passing the prompt to the `gpt-4o-mini` model.
    3.  We extract and return the generated text response: `response.choices[0].message.content`.

---

## 2. Deep Technical Concepts

*   **Context Injection:** The process of inserting relevant retrieved database facts directly into the model's prompt. This grounds the model, ensuring it synthesizes answers using verified facts rather than relying on its base training data.
*   **API Choices Struct:** The OpenAI API returns completions inside a structured response. `choices` is a list (allowing you to request multiple completions). We access the first generated option using index `0` and retrieve its text content using `.message.content`.

---

## 3. Architectural Choices and Alternatives

### Why use RAG instead of increasing context lengths?
*   **Retrieval-Augmented Generation (RAG):** Dynamically retrieves only the top-k relevant database entries (usually 3 to 5 chunks) and injects them into the prompt.
*   **Alternatives (Long-Context Injection):** You could send all documents (e.g. 50,000 words) inside the LLM's context window for every request. However, this is slow, expensive (due to token limits), and can cause models to ignore context in the middle of long prompts (a phenomenon known as "lost in the middle").