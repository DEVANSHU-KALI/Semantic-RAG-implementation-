## 🖥️ app.py: Streamlit Client UI & Communication

This document breaks down the user interface implementation in `frontend/app.py` section-by-section.

---

## 1. Code Walkthrough (Line-by-Line)

The frontend script renders the user interface in the browser and handles communication with the FastAPI backend.

### Part A: Imports & Configurations
```python
import streamlit as st
import requests 

st.title("RAG Chatbot")
API_URL = "http://localhost:8000/chat"
```
*   **What is happening in the code:** We import `streamlit` for UI rendering and `requests` for making HTTP calls. We set the page title and define the backend URL route `/chat` on port 8000.

### Part B: Capture Input & State Check
```python
query = st.text_input("Ask a question")

if query:
```
*   **What is happening in the code:**
    1.  `st.text_input`: Renders a text box in the browser. 
    2.  **Execution Loop:** Streamlit runs the script from top to bottom on user interactions. When a user types a query and hits Enter, the script reruns, and the input value is stored in `query`.
    3.  `if query:`: The block executes only if the input box is not empty.

### Part C: Display Spinner & Execute API POST Request
```python
    with st.spinner("Server is thinking..."):
        try:
            payload = {"prompt": query}
            response = requests.post(API_URL, json=payload)
```
*   **What is happening in the code:**
    1.  `st.spinner`: Displays a loading spinner while the background network request resolves.
    2.  `payload = {"prompt": query}`: Wraps the query in a dictionary.
    3.  **Serialization:** The `requests.post` call converts (serializes) our Python dictionary `payload` into a JSON byte string and transmits it over the network to the backend API.

### Part D: Validation & Deserialization (Response Parsing)
```python
            if response.status_code == 200:
                data = response.json()
                st.write(data["answer"])
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Connection failed: {e}")
```
*   **What is happening in the code:**
    1.  `response.status_code == 200`: Checks if the server returned a `200 OK` success code.
    2.  **Deserialization:** `response.json()` parses the raw JSON response byte stream back into a Python dictionary (`data`).
    3.  `st.write(data["answer"])`: Renders the final text response in the browser.
    4.  **Exception Handling:** The `except` block catches connection errors if the FastAPI backend is offline.

---

## 2. Deep Technical Concepts

*   **Client-Server Architecture:** A distributed application structure where clients (the requester, e.g. Streamlit) send requests to servers (the service provider, e.g. FastAPI).
*   **Serialization:** The process of converting memory-resident structures (like Python dictionaries) into a format suitable for transmission over a network (like JSON byte strings).
*   **Deserialization:** The process of parsing serialized formats (like JSON) back into memory-resident objects (like Python dictionaries).

---

## 3. Architectural Choices and Alternatives

### Why use Streamlit instead of React/HTML/CSS?
*   **Streamlit (Used Here):** Fast, Python-native, and automatically handles UI rendering and state loops, letting developers build interfaces without writing HTML, CSS, or JavaScript.
*   **Alternatives (Custom React Frontend):** Provides design flexibility and supports client-side state caching, but requires writing extensive frontend code and setting up separate build tools.