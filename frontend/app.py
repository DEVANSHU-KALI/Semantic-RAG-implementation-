import streamlit as st
import requests 

st.title("RAG Chatbot")

API_URL = "http://localhost:8000/chat"

query = st.text_input("Ask a question")

if query:
    
    with st.spinner("Server is thinking..."):
        try:

            payload = {"prompt": query}
            
            response = requests.post(API_URL, json=payload)
           
            if response.status_code == 200:
                data = response.json()
                st.write(data["answer"])
            else:
                st.error(f"Error: {response.status_code}")
                
        except Exception as e:
            st.error(f"Connection failed: {e}")

# import streamlit as st
# import sys
# import os

# from backend.rag_pipeline import generate_answer

# st.title("RAG Chatbot")

# query = st.text_input("Ask a question")

# if query:
#     with st.spinner("Thinking... 🤖"):
#         answer = generate_answer(query)
#         st.write(answer)