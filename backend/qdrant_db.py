from qdrant_client import AsyncQdrantClient
from qdrant_client.http.models import VectorParams, Distance

client = AsyncQdrantClient(host="localhost", port=6333)

collections = client.get_collections().collections
existing_collections = [c.name for c in collections]


if "ai_research_papers" not in existing_collections:
    client.create_collection(
        collection_name="ai_research_papers",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )


if "langchain_docs" not in existing_collections:
    client.create_collection(
        collection_name="langchain_docs",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

print("Collections are ready.")