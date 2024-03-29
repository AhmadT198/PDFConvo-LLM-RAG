import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from app.chat.embeddings.openai import embeddings

#Initialize the Pinecone client and connect it to your account by api key.
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
)
index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

#Create a vector store by wrapping pinecone and the embedding model together
vector_store = PineconeVectorStore(
    index, embeddings
) 


def build_retriever(chat_args):
    search_kwargs = {"filter":{"pdf_id": chat_args.pdf_id}}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )

