## script which can reset all you qdrant collection's data on your decision.

### imports
- as this is a option file and also not a part of the rag pipeline, we don't actually use the async version of the qdrant client.

### client initialization
- initialize the client.

### code part:
- listing this collection which we want to delete, you can customize that collection names here.

- for loop through the collections 
    - a try and except block to handle existence of collections and perform the cleaning.
- print some message to tell you the process is over.

- NOTE: you can use this when you want to add your data.