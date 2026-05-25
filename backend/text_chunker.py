from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# APPROACH 1: Lower the Percentile Threshold
    # The default is 95. Dropping it to 70-80 makes the chunker much more 
    # sensitive to the topic shifts between your paragraphs.
text_splitter = SemanticChunker(
    embedding_model,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=75 
)

# APPROACH 2: Use Standard Deviation (Alternative)
    # This splits the text whenever the semantic difference between sentences 
    # is greater than 1.25 standard deviations from the document's average.
    # text_splitter = SemanticChunker(
    #     embedding_model,
    #     breakpoint_threshold_type="standard_deviation",
    #     breakpoint_threshold_amount=1.25
    # )

# or simply use the old code but in different way
    # from langchain_text_splitters import RecursiveCharacterTextSplitter
    # # This tells the splitter to prioritize splitting at double newlines first.
    # # If a paragraph is still too long, it will fall back to single newlines, then periods.
    # text_splitter = RecursiveCharacterTextSplitter(
    #     separators=["\n\n", "\n", ".", " "],
    #     chunk_size=1000, 
    #     chunk_overlap=0
    # )

    # # Then you simply pass your text to it
    # # chunks = text_splitter.split_text(your_document_text)
    # # but for this approach, ensure that each of you topic should be separated by at least a double newline in your source documents. This way, the splitter can effectively identify topic boundaries and create more semantically coherent chunks.

# before:

    # from langchain_text_splitters import RecursiveCharacterTextSplitter

    # text_splitter = RecursiveCharacterTextSplitter(
    #     chunk_size=500,
    #     chunk_overlap=100
    # )