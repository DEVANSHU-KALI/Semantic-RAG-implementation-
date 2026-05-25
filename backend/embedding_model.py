from sentence_transformers import SentenceTransformer

# load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# this model has 384 dimensions, and you can go with other models too. and as mentioned, all the explanation of scripts will be available in the explanations/backend folder.

