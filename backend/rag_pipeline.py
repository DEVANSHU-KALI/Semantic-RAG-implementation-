from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

from .query_router import route_query
from .new_retriever import retrieve_chunks

client = AsyncOpenAI() 

async def generate_answer(query): # Add async
    collection_name = await route_query(query)

    results = await retrieve_chunks(query, collection_name)

    for r in results:
        print(f"source: {r['source']}")

    context = "\n\n".join([r["text"] for r in results])

    prompt = f"Context:\n{context}\n\nQuestion: {query}"

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# python -m backend.rag_pipeline : cmd to run the file directly, without going into the backend folder and running it from there. 
# python -m uvicorn backend.main:app --reload