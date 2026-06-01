## a very important script which gets all the relevant chunks from the database.

### first the imports
- importing the qdrant client.
- From the embedding model script we are importing our embedding model which we initialized there in that script.

### Database client initialization":
- As the quadrant database is running on local host 6333, We are accessing that using our asyncqdrantclient.

### Now the retrieve chunks function:
- Now this function Expects the query and the collection name as the input parameters. Now the next part of the code is as follow.
- Now the first thing we are doing is converting our query into vectors using that specific line number 8 , we are using a embedding model to convert that query into embeddings And the output of embedding model will be an numpy array, we can't actually use numpy arrays efficiently in other scripts as they are only better in mathematical calculations, so we directly convert that into list, using the to list function.