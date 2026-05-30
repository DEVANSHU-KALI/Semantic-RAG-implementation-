## As we got to know about chunking from the key concepts file, here are some things to know:
- we are using the semantic chunker here as discussed, with certain configurations.
- this chunker splits data based on topic change, and to know whether the topic has changed or not, it needs embeddings.
- breakpoint_threshold_amount=75 , this means if the concept change confidence is above 75%, split and chunk to that point. 

### Hidden concept: Interfaces (methods you get to use in code, and structure)
- if you observe one thing, you can notice that, we took our embedding model inside some wrapper, let me explain what and why is it like that.
- the main thing to know is, semantic chunker comes from langchain, so its obvious that it expects langchain's embedding format (i.e. langchain's interface), where you get .embed_document() function to create embeddings for chunks you have, and .embed_query() to create embeddings for query, and on the other hand if we use the model from sentence-transformer directly, its going to follow sentence-transformer embedding format (i.e. sentence-transformer interface), which only has .encode() for both query and doc, so we wrapped our embedding model with a langchain embedding model wrapper. 
- .embeb_document() or .embed_chunk(), literally do the same thing as .encode() from sentence-transformer interface does, but the answer is more advance level, which we don't want to explore right now.

