from openai import AsyncOpenAI
from dotenv import load_dotenv
from langsmith import traceable

load_dotenv()

from .query_router import route_query
from .new_retriever import retrieve_chunks

client = AsyncOpenAI() 

@traceable
async def generate_answer(query): # Add async
    collection_name = await route_query(query)

    results = await retrieve_chunks(query, collection_name)

    for r in results:
        print(f"source: {r['source']}")

    contexts = [r["text"] for r in results]
    context = "\n\n".join(contexts)

    prompt = f"Context:\n{context}\n\nQuestion: {query}"

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": response.choices[0].message.content,
        "contexts": contexts
    }

# python -m backend.rag_pipeline : cmd to run the file directly, without going into the backend folder and running it from there. 
# python -m uvicorn backend.main:app --reload