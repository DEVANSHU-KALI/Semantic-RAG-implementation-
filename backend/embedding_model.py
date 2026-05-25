from sentence_transformers import SentenceTransformer

# load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)