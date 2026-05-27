## As we got to know about chunking from the key concepts file, here are some things to know:
- we are using the semantic chunker here as discussed, with certain configurations.
- this chunker splits data based on topic change, and to know whether the topic has changed or not, it needs embeddings.
- breakpoint_threshold_amount=75 , this means if the concept change confidence is above 75%, split and chunk to that point. 

### Hidden concept
- if you 