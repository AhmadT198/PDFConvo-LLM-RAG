from langchain_openai import OpenAIEmbeddings
import os

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))