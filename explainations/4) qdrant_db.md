## qdrant_db.py
- this file is meant to have a connection with the qdrant database and create collection if there is no collection with the names mentioned there

### now let's have it part by part:
- First comes the imports:
    - asyncqdrantclient: as we are implementing the concept of async programming and mainly making the system non blocking, we import the async version of the qdrant client
    - the next imports are related to the embeddings, so that the database gets a idea about them.
        - as you can see below in the code, you can see, we initialized them for both the collections.
- initializing the client:
    - here is the connection part: this line is responsible for connecting this code to the qdrant database.

- the next two lines: 6 and 7 will check whether there are any collections existing or not, a loop through the collections.

- collection creation part:
    - code for both is same
        - we check if the collection names is inside the existing_collections list or not, and then create this collections there

- at the end, we print collection is read.

--- 

### execution part:
- after starting your qdrant database container, come into the ide and run this script, which will create the collections and then print the message.
- open your qdrant dashboard and see there, you will see both of this there/