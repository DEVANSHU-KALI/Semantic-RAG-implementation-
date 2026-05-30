## The main script which handles the rag pipeline.
- this script covers the main part of the whole system, the RAG.
- so lets go deeply to understand what's happening in the code ending with the flow.

### imports
- as we are using the gpt model here, we import the openai here.
- reason to use the async version:
    - as we want to make the calls non blocking, we use the async version of it. if you don't know what does this mean, you need to learn about the async programming, as its a fundamental concept of it.

- loading the env in to the script.
- as we are using two collections instead of one in this system, the system automatically sends the query to the query_router script, and let that script decide, which collection should be used for the query. I'll explain this clearly in the flow below.
- import the retrieve_chunks function which gets the relevant chunks for the query. Go and see the md file related to the new_retriever script to understand this more clearly.


