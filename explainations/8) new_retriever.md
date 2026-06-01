## a very important script which gets all the relevant chunks from the database.

### first the imports
- Importing the Qdrant client.
- Importing the embedding model from the embedding_model script, which is used to convert queries into vector embeddings.

### Database client initialization
- Since the Qdrant database is running locally on port 6333, we connect to it using AsyncQdrantClient.

### Now the retrieve chunks function:
- This function takes a query and a collection name as input.
- First, the query is converted into embeddings using the embedding model. The embedding model returns a NumPy array. Since Qdrant expects the vector in a standard Python list format, we convert it using .tolist() before sending it to the database.
- This script is used by other scripts in the project. The collection name is provided by the query_router script, which classifies the user query and returns a category such as `ai` or `langchain_docs`. Based on this output, the appropriate collection (for example, `ai_research_papers` or `langchain_docs`) is searched.
- The collection name and query vector are sent to Qdrant, which performs a similarity search and returns the most relevant chunks. `limit=3` means only the top 3 matching chunks are retrieved.
- Since Qdrant stores data as points, we loop through the returned points and extract the required payload information, such as the chunk text and its source. These details are stored in a results list.
- Finally, the results list is returned and used by other scripts in the RAG pipeline.
- If this script feels difficult to understand on its own, don't worry. Its role becomes much clearer when we see how it is used by other scripts in the project and follow the complete flow of data through the system.
- a small point to mention here in the line 27  

```py
"source": point.payload.get("source", "unknown")
``` 
which actually means that if there is a source return the source name and if there's nothing written unknown which is a safety measure we used in this project instead of returning an error if there's no source for that chunk of data