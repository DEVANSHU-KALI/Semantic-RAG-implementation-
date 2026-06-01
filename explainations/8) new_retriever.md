## a very important script which gets all the relevant chunks from the database.

### first the imports
- importing the qdrant client.
- From the embedding model script we are importing our embedding model which we initialized there in that script.

### Database client initialization":
- As the quadrant database is running on local host 6333, We are accessing that using our asyncqdrantclient.

### Now the retrieve chunks function:
- Now this function Expects the query and the collection name as the input parameters. Now the next part of the code is as follow.
- Now the first thing we are doing is converting our query into vectors using that specific line number 8 , we are using a embedding model to convert that query into embeddings And the output of embedding model will be an numpy array, we can't actually use numpy arrays efficiently in other scripts as they are only better in mathematical calculations, so we directly convert that into list, using the to list function.
- this whole script is used in another scripts, Now we are classifying the query to use which collection based on collection name (we have a independent script which classifies the query into collection and give ai or langchain_docs terms as output, then this script decided which collection to use based on the output of that script, if it give ai, then ai_research_papers will be used to get data, and vise versa), given by the query_router script, which is the script which classifies and give a some output which comes into this parameter, That's the reason why I mentioned the first line as this whole script is used in another scripts. 
- Now we get the collection name the query vector which means the embeddings of that Query, send them to the database client which is our quadrant client to get all the relevant chunks To this specific vector (query vector), And the line limit equals to three tells get the top three chunks which is relevant with this query
- 