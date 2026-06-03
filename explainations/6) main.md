## ⚡ main.py: FastAPI Server and Schema Validation

This document breaks down the API endpoint implementation in `backend/main.py` section-by-section.

---

## 1. Code Walkthrough (Line-by-Line)

The backend server is responsible for exposing endpoints to receive requests from the frontend, call the RAG pipeline, and return JSON responses.

### Part A: Imports
```python
from fastapi import FastAPI
from pydantic import BaseModel
from .rag_pipeline import generate_answer
```
*   **What is happening in the code:** We import the `FastAPI` framework, the `BaseModel` data validation class from Pydantic, and the `generate_answer` function from our pipeline.

### Part B: App Setup
```python
app = FastAPI(title="RAG Chatbot API")
```
*   **What is happening in the code:** We instantiate the `FastAPI` application server and set its title. This initializes the server routing and automatically sets up interactive documentation endpoints (e.g. `/docs` or `/redoc`).

### Part C: Defining Request Schemas
```python
class QueryRequest(BaseModel):
    prompt: str
```
*   **What is happening in the code:** We declare a class `QueryRequest` that inherits from Pydantic's `BaseModel`. We define a single field `prompt` of type `str`.
*   **Why we do it:** This acts as a validator (a filter that validates request body structure and data types). If a request comes in containing a different format or missing fields, FastAPI will automatically reject it and return an error before executing any pipeline logic.

### Part D: POST Route Definition & Endpoint Handler
```python
@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    result = await generate_answer(request.prompt)
    return {"answer": result}
```
*   **What is happening in the code:**
    1.  We define an HTTP POST route at the path `/chat`.
    2.  The handler function `chat_endpoint` is declared as an asynchronous function (`async def`) and accepts a parameter `request` matching our `QueryRequest` model.
    3.  We call `await generate_answer(request.prompt)`. This triggers our RAG pipeline, pausing execution to wait for OpenAI and Qdrant database queries while releasing the thread to handle other incoming network requests.
    4.  We return a Python dictionary `{"answer": result}`, which FastAPI automatically serializes (converts) into a JSON response body.

---

## 2. Deep Technical Concepts

*   **ASGI (Asynchronous Server Gateway Interface):** A interface standard for asynchronous web servers. Unlike traditional WSGI (Web Server Gateway Interface) standards (used in Flask), ASGI supports non-blocking I/O operations and asynchronous endpoints.
*   **HTTP POST Method:** POST is used to send data in the request body to the server. Unlike GET requests, which attach data directly to the URL string, POST requests can handle large queries securely and support complex JSON payloads.

---

## 3. Architectural Choices and Alternatives

### Why FastAPI instead of Flask?
*   **FastAPI:** Built on ASGI, natively asynchronous, provides automatic validation via Pydantic, and generates documentation (Swagger) out of the box.
*   **Flask:** Simple and lightweight, but synchronous (blocking) by default. Implementing async database searches or streaming LLM completions in Flask requires additional threading structures, making it less suitable for high-concurrency AI applications.