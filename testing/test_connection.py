from backend.qdrant_db import QdrantClient

client = QdrantClient(host="localhost", port=6333)

try:
    collections = client.get_collections()

    print("\nConnected to Qdrant successfully!\n")

    print("Collections available:")
    for collection in collections.collections:
        print("-", collection.name)

except Exception as e:
    print("Connection failed:", e)

# from chroma_client import client

# collections = client.list_collections()

# print("Collections in database:")

# for c in collections:
#     print(c.name)