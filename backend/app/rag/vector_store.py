from langchain_chroma import Chroma
from app.rag.embeddings import embeddings

VECTOR_DB = "data/chroma"

def create_vector_store(chunks):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB,
    )

def load_vector_store():
    return Chroma(
        persist_directory=VECTOR_DB,
        embedding_function=embeddings,
    )