## all-miniLm-L6-v2
- the model which we used in this project, which comes with 384D (dimensions).
- now lets know what does it mean by dimensions and why are there different models with different dimensions.
    - when it says 384 dimensions, it means the model understand a word or letter or sentence based on 384 features, like tone, situations,context, syntax, and semantic meaning, all represented as numerical values in a dense vector.
    - now lets get deep into understanding dimensions.
        - Feature Vector: The model converts text into a list of 384 numbers.
        - Abstract Concepts: Dimensions do not map directly to human labels like "happy" or "past tense."
        - Mathematical Relationships: They capture complex patterns, relationships, and concepts across a geometric space.
        - Contextual Nuance: Words with similar meanings or contexts are placed close together in this 384-dimensional space. 

- and as discussed in the key_concepts, I strongly recommend to go with higher dimensions, which is the **nomic-embed-text-v1.5**, which comes with 768.
- and the import remains same here but you need to install a new library which is **pip install sentence-transformers einops**, the einpos is like a engine which process the sentence transformer behind, and this is different from normal sentence-transformer library, because this enipos works as a update as the model is new.
