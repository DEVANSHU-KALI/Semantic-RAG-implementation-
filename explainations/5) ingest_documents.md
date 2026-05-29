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

- convert the chunks into embeddings.
- print the embeddings length in terminal, which will be 386 as we used that model.

- now related to points creation:
- list to store all the points and later insert that points to specific collection in qdrant database.
    - loop through length of documents
        - for each point, we are getting:
            - id
            - embeddings
            - payload:
                - chunk text
                - source (from which file did the chunk come)

- upsert is the method used to insert data into the qdrant client, and here we are inserting the points to specific collection.
- a simple message in terminal to tell, injestion is completed.

- now the main part which is related to python: 
    - the running part: when you run this code, you take each data one time, as we used two collections.
    - one collection and its folder path goes into the function at one time each.
    - if we dont write in this way, we would've got a large code, where we needed to write specific code for both the collections.
    