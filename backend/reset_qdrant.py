from qdrant_client import QdrantClient

# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)

# List of collections to delete
collections = ["ai_research_papers", "langchain_docs"]

for collection in collections:
    try:
        client.delete_collection(collection_name=collection)
        print(f"Deleted collection: {collection}")
    except Exception as e:
        print(f"Collection {collection} not found or already deleted.")

print("\n✅ Qdrant reset complete.")