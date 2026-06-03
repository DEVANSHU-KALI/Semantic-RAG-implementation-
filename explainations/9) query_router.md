## 🚦 query_router.py: Schema-Enforced Intent Classification

This document breaks down the query router implementation in `backend/query_router.py` section-by-section.

---

## 1. Code Walkthrough (Line-by-Line)

The query router acts as an intelligent traffic dispatcher, sending queries to either the AI papers database or the LangChain documentation.

### Part A: Imports & Setup
```python
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()
client = AsyncOpenAI() 
```
*   **What is happening in the code:** We import our asynchronous OpenAI client and environment loader. We also import `BaseModel` and `Field` from Pydantic, along with the `Literal` type constraint from Python typing. We load the environment and instantiate our client.

### Part B: Defining the Output Schema
```python
# REFACTOR NOTE: Enforcing OpenAI Structured Outputs using Pydantic.
class QueryClassification(BaseModel):
    category: Literal["ai", "langchain_docs"] = Field(
        description="The classification category of the query: 'ai' or 'langchain_docs'."
    )
```
*   **What is happening in the code:** We declare a class `QueryClassification` that inherits from Pydantic's `BaseModel`. We define a field `category` and restrict its values to strictly `"ai"` or `"langchain_docs"` using `Literal`.
*   **Why we do it:** This acts as the validation schema for OpenAI. It prevents the model from returning conversational filler (e.g. *"I think the answer is langchain_docs"*), which would break our database routing.

### Part C: Routing Function & Completion Request
```python
async def route_query(query: str) -> str:
    prompt = f"""
    Classify the following query into one category:

    1) ai 
    description: Queries related to artificial intelligence research and other topics related to ai.
    2) langchain_docs
    description: Queries related to langchain documentation, usage, and related topics.

    Query: {query}
    """

    # Call the parsing-native beta completions endpoint, passing the Pydantic schema
    response = await client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        response_format=QueryClassification,
    )
```
*   **What is happening in the code:**
    1.  We define `route_query` as an asynchronous function.
    2.  We construct the classification prompt outlining the categories.
    3.  We call `await client.beta.chat.completions.parse(...)` to trigger a structured completions query to OpenAI. We pass the prompt and set `response_format` to our Pydantic schema class.

### Part D: Extracting the Result
```python
    # Safely return the strongly-typed schema value
    return response.choices[0].message.parsed.category
```
*   **What is happening in the code:** We retrieve the parsed category value from the response payload. The SDK handles JSON deserialization, type checks, and validates the output against the Pydantic model automatically.

---

## 2. Deep Technical Concepts

*   **OpenAI Structured Outputs:** An API feature that constraints model generation. The API maps our Pydantic schema to a JSON schema. During generation, it applies context-free grammar constraints to restrict the tokens the model can select, guaranteeing the output matches the target JSON schema.
*   **Pydantic BaseModel Validation:** A Python library for data parsing and validation. It translates natural language schema definitions into structured validation checks.

---

## 3. Architectural Choices and Alternatives

### Why use Structured Outputs instead of standard prompts?
*   **Structured Outputs (Used Here):** Guarantees that the LLM returns exactly the keys and values defined in the schema.
*   **Alternative (Free-text Prompts):** Relying on raw completions (e.g. `client.chat.completions.create`) is fragile. The LLM can return unexpected formatting, casing variants (e.g. `"AI"`), or markdown blocks, causing downstream database routing matching to fail.