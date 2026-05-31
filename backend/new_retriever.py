from qdrant_client import AsyncQdrantClient
from .embedding_model import embedding_model

client = AsyncQdrantClient(host="localhost", port=6333)

async def retrieve_chunks(query: str, collection_name: str):

    query_vector = embedding_model.encode(query).tolist()

    if collection_name == "ai":
        collection = "ai_research_papers"
    else:
        collection = "langchain_docs"

    results = await client.query_points(
        collection_name=collection,
        query=query_vector,
        limit=3
    )

    # Extract text from payload
    results_list = []

    for point in results.points:
        results_list.append({
            "text": point.payload["text"],
            "source": point.payload.get("source", "unknown")
        })

    return results_list


# from langchain_qdrant import Qdrant
# from langchain_huggingface import HuggingFaceEmbeddings
# from qdrant_client import QdrantClient


# client = QdrantClient(host="localhost", port=6333)


# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# ai_vector_store = Qdrant.from_existing_collection(
#     embedding=embeddings,
#     url="http://localhost:6333",
#     collection_name="ai_research_papers"
# )

# langchain_vector_store = Qdrant.from_existing_collection(
#     embedding=embeddings,
#     url="http://localhost:6333",
#     collection_name="langchain_docs"
# )


# ai_retriever = ai_vector_store.as_retriever(search_kwargs={"k": 3})
# langchain_retriever = langchain_vector_store.as_retriever(search_kwargs={"k": 3})


# def retrieve_chunks(query, collection_name):

#     if collection_name == "ai":
#         docs = ai_retriever.invoke(query)

#     else:
#         docs = langchain_retriever.invoke(query)

#     return [doc.page_content for doc in docs]