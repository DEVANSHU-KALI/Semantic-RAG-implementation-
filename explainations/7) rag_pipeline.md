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


### initializing the open ai client
- asyncopenai is used as client here, to get the model

### now the generate_answer function: which expects query as a input parameter
- get the collection name first.
- send the query and collection to the retrieve_chunks function which returns the relevant chunks. 
- The next part here is about citation.
    - You have a for loop Through the results, get the source of that result (the source of that answer,document did that answer come from )
- Now building the context for the LLM, Here You're going to join all the text of the Chunks Which your retrieval system got from the database so that all these can be  combined and send to the LLM to let that understand what the context is, That's what a rag system does.
- Now here We are getting that context and also a query which will be sent to the llm in next code part..
- the variable response now stores the answer given by the gpt model.
    - here you may think what is that client.chat.completion.create() thing and also the things inside that.
        - the first things is the endpoint used to send questions to the gpt model(thats the interface it expects), and inside that we mention model name and the message thing is optional, just telling it we are used and the prompt contains all the things.
- now the return function, the line which you are seeing there like, response.choice... is the way to access the model's answer, its a incredible structure.
    - if you want to understand that, go to openai docs or ai to answer you query.