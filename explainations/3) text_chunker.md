## As we got to know about chunking from the key concepts file, here are some things to know:
- we are using the semantic chunker here as discussed, with certain configurations.
- this chunker splits data based on topic change, and to know whether the topic has changed or not, it needs embeddings.
- breakpoint_threshold_amount=75 , this means if the concept change confidence is above 75%, split and chunk to that point. 

### Hidden concept
- if you observe one thing, you can notice that, we took our embedding model inside some wrapper, let me explain what and why is it like that.
- the main thing to know is, semantic chunker comes from langchain, so its obvious that it expects langchian's embedding format, where you get .embed_document, 
.embed_query, and on the other hand the model follows sentence-transformer embedding format, which only has .embed_text for both query and doc, so we wrapped our embedding model with a langchian embedding model wrapper. 
- and there is also a reason why separating both, even they do the same work, .embeb_document or .embed_chunk, literally do the same thing as .embed_text does, but the answer is more advance level, which we dont want to explore right now.

