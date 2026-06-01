import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI() 

async def route_query(query: str) -> str:
    
    prompt = f"""
    Classify the following query into one category:

    1) ai 
    description: Queries related to artificial intelligence research and other topics related to ai.
    2) langchain_docs
    description: Queries related to langchain documentation, usage, and related topics.

    Query: {query}

    classify into one category, either "ai" or "langchain_docs".
    """

    # Standard, blocking call
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content.strip()


# past version of query_router.py.
# def route_query(query: str):

#     query = query.lower()

#     langchain_keywords = [
#         "langchain",
#         "agent",
#         "retriever",
#         "chain",
#         "tool",
#     ]

#     for word in langchain_keywords:
#         if word in query:
#             return "langchain"

#     return "ai"
#   # use llm to classify