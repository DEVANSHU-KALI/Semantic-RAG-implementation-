# Semantic-Rag also known as Simple-RAG

An asynchronous RAG (Retrieval-Augmented Generation) system built with FastAPI, Qdrant, and OpenAI. This system features a custom Query Router to search across multiple document collections dynamically.

## 🚀 Key Features
- **Async Backend:** Built with FastAPI and `AsyncOpenAI` for non-blocking concurrent requests.
- **Smart Routing:** Classifies user queries to search the most relevant document collection.
- **Vector Storage:** Uses Qdrant DB for high-performance semantic search.
- **Traceability:** Logs citations and source documents directly to the terminal.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **LLM:** OpenAI (GPT-4o-mini)
- **Vector DB:** Qdrant (Running via Docker)
- **Frontend:** Streamlit
- **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)

---

## 🏃 Getting Started

### 1. Setup Qdrant (Docker)
- Ensure Docker is running on your system. Use the following command to start the optimized Qdrant container:

- Open the terminal and then locate to the docker folder and type this command. 
``` bash
docker compose up -d
```
- If you want to, you can see the qdrantdb ui through the link: http://localhost:6333/dashboard. or you can also go into dockers ui through the dockers application.
- **NOTE**: you need to keep the dockers application 'ON', opened on you desktop, when you run this command, if you close it, it may not work.
- After you create this container and start it, you can safely close the dockers application if needed, as it runs on a port and the retrieval is going to happen.

### 2. Add openai api key into the .env

### 3. Install the requirements.txt

### 4. Create collections
```bash
python -m backend.qdrant_db
```
- This creates two collections in the qdrant db, see inside the qdrant_db.py file, you will have a idea about it.
- Wait for a while until you see the message like "collections are ready" in the terminal.

### 5. inject the documents into the collections.
- Instead of using one collection, I got two collections, to make the retrieval more accurate, and I also got two different types of data inside the 'data' folder.
``` bash
python -m backend.injest_docuemnts
```
- running this command will take the data which we used, chunk them and add them to the specified collections.
- wait until you see "Documents successfully ingested into, collection_names" in the terminal.

### 6. starting the backend.
- open a the terminal.
```bash
uvicorn backend.main:app --reload
```
- Wait until the script finishes execution and you see the command prompt again. This usually takes 5–10 seconds depending on your document size.
- until you have empty terminal just not getting anything running.

### 7. starting the frontend
- open another terminal.
``` bash
streamlit run frontend/app.py
```
### 8. reset you qdrant database.
``` bash
python -m backend.qdrant.py
```
- this is optional command. you can use this to erase existing data in you qdrant collections, so that you can later upload them with new data.

**NOTE: activate you venv and do this all things, if you installed all the libraries in a venv**

---

### Everything is done. you can type a query and see the answer there. for example: type "what is Neuromorphic Computing", you can see the answer, now go into the data/ai_papers/paper1.txt, you can see the information in the answer is from this paper and compare your frontend answer and the information here, you see similarity.
### It's not a rule to use the same data and collections I used, you can modify them and get you own data, and use them in the project.

### NOTE: I used the open ai models for this project, if you want, you can go and use free models from openrouter, but you need to add the api key in the .env and also customize the codes.

--- 

## Project structure 🏢
```text
simple_rag/
│
├── backend/
│   ├── __init__.py           # Empty file making 'backend' a Python module
│   ├── qdrant_db.py          # Safely initializes collections (non-destructive)
│   ├── reset_qdrant.py       # Developer tool: Wipes collections to clear test data 🔄
│   ├── ingest_documents.py   # Processes data using SemanticChunker & saves vectors
│   ├── query_router.py       # Asynchronously classifies user query intent
│   ├── new_retriever.py      # AsyncQdrantClient vector retrieval logic
│   ├── rag_pipeline.py       # Core orchestrator (prints citations & calls OpenAI) 
│   └── main.py               # FastAPI server endpoints ⭐
│
├── frontend/
│   └── app.py                # Streamlit chat interface
│
├── data/                     # Store your source documents here, store text files inside them as data.
│   ├── ai_research_papers/   
│   └── langchain_docs/       
│
├── qdrant_storage/           # Local folder mounted by Docker
├── .env                      
├── .gitignore                
├── docker-compose.yml        
├── requirements.txt          
└── README.md
```
--- 

## All the projects explainations are inside explainations folder, go check it out if you really want to learn instead of just building this project.