import os

from .embedding_model import embedding_model
from .text_chunker import text_splitter

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct


# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)


def ingest_documents(folder_path: str, collection_name: str):

    documents = []
    ids = []

    counter = 0

    for filename in os.listdir(folder_path):

        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        chunks = text_splitter.create_documents([text])

        for chunk in chunks:

            documents.append(chunk.page_content)
            ids.append(counter)

            counter += 1


    print("\n======= DOCUMENT CHUNKS =======\n")
    for doc in documents:
        print(doc)
        print("-------------")


    print("\n======= IDS =======\n")
    print(ids)


    # Convert chunks to embeddings
    embeddings = embedding_model.encode(documents)


    print("\nEmbedding vector size:", len(embeddings[0]))

    points = []

    for i in range(len(documents)):

        points.append(
            PointStruct(
                id=ids[i],
                vector=embeddings[i].tolist(),
                payload={
                    "text": documents[i],
                    "source": filename
                }
            )
        )

# Point 1:
#   id = 0
#   vector = [384 numbers]
#   payload = {"text": "chunk1"}

# Point 2:
#   id = 1
#   vector = [384 numbers]
#   payload = {"text": "chunk2"}

    # Upload to Qdrant
    client.upsert(
        collection_name=collection_name,
        points=points
    )


    print("\nDocuments successfully ingested into", collection_name)



# Run ingestion
if __name__ == "__main__":

    ingest_documents("data/ai_papers", "ai_research_papers")

    ingest_documents("data/langchain_docs", "langchain_docs")