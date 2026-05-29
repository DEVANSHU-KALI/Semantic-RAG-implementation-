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

- we create two different lists, which store documents(chunks) and ids
- a counter variable to have a count of chunks, as we need ids

- for loop to loop over the folder path to get all the text files.
- read them, create chunks (documents), and ids. increment the counter by 1.

- a small message to print in the terminal
    - a example chunk to print, so that we can see how the chunk looks
    - and id of the chunks.