import asyncio
from qdrant_client import AsyncQdrantClient
from qdrant_client.http.models import VectorParams, Distance

# REFACTOR NOTE: Wrapping collection initialization inside an asynchronous function.
# The original code imported AsyncQdrantClient but attempted to run its methods synchronously 
# (e.g. client.get_collections().collections), which throws AttributeError and coroutine warnings.
# By making this function async, we can properly await the database network calls.
async def initialize_collections():
    # Initialize connection to the Qdrant database running on local port 6333
    client = AsyncQdrantClient(host="localhost", port=6333)
    try:
        # Correctly await the async get_collections() API call
        collections_response = await client.get_collections()
        collections = collections_response.collections
        existing_collections = [c.name for c in collections]

        # Verify and asynchronously create the collection if missing
        if "ai_research_papers" not in existing_collections:
            await client.create_collection(
                collection_name="ai_research_papers",
                vectors_config=VectorParams(size=384, distance=Distance.COSINE),
            )

        if "langchain_docs" not in existing_collections:
            await client.create_collection(
                collection_name="langchain_docs",
                vectors_config=VectorParams(size=384, distance=Distance.COSINE),
            )

        print("Collections are ready.")
    finally:
        # Gracefully shut down client connection pool session
        await client.close()

if __name__ == "__main__":
    # REFACTOR NOTE: asyncio.run starts the event loop and executes our async entry point.
    # We run this check only when executed directly as a script (preventing execution on import).
    asyncio.run(initialize_collections())
