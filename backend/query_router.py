import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

client = AsyncOpenAI() 

# REFACTOR NOTE: Enforcing OpenAI Structured Outputs using Pydantic.
# Free-text classification is highly fragile; the LLM can output casing variants 
# (e.g. "AI"), conversational wrappers (e.g. "The category is: ai"), or Markdown.
# Downstream retriever collection mapping requires exactly "ai" or "langchain_docs".
# By passing a Pydantic schema and calling client.beta.chat.completions.parse, 
# the API mathematically restricts tokens to matching our strict schema structure.
class QueryClassification(BaseModel):
    category: Literal["ai", "langchain_docs"] = Field(
        description="The classification category of the query: 'ai' or 'langchain_docs'."
    )

async def route_query(query: str) -> str:
    
    prompt = f"""
    Classify the following query into one category:

    1) ai 
    description: Queries related to artificial intelligence research and other topics related to ai.
    2) langchain_docs
    description: Queries related to langchain documentation, usage, and related topics.

    Query: {query}
    """

    # Call the parsing-native beta completions endpoint, passing the Pydantic schema
    response = await client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        response_format=QueryClassification,
    )

    # Safely return the strongly-typed schema value
    return response.choices[0].message.parsed.category


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