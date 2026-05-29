from fastapi import FastAPI
from pydantic import BaseModel
from .rag_pipeline import generate_answer

app = FastAPI(title="RAG Chatbot API")

class QueryRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    
    result = await generate_answer(request.prompt)

    return {"answer": result}