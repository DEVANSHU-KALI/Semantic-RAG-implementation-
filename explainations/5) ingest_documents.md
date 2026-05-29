## This script is meant to inject data into the qdrant database.

### imports:
- import os to get the data file
- importing embedding model from the embedding model script
- import the text_splitter function from the text_chunker.py script
- now the main part:
    - importing the normal qdrant client, because this script is not a part of rag pipeline, this comes under pre rag phase, where you just run once to inject your data into the qdrant file, and its just a simple i/o bound operation, we don't need async version of it.
- pointstruct: now as we discussed in the key concept, related to qdrant, points are the way of storing data in the qdrant database, where each point mainly contains, id, vector, payload (text, source and more if wanted).
    - so we import this to create some point structure according our project.

### connect to qdrant client
- as our qdrant is running in that locahost port, we initialize the client and connect to it.

### main function:
- this functions expects two parameters: folder path (from where to take data), and collection name (into which collection the data should be stored)