from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vector_store import create_vector_store

docs = load_documents("../data/policies")
print(f"Documents loaded: {len(docs)}")

chunks = split_documents(docs)
print(f"Chunks created: {len(chunks)}")

create_vector_store(chunks)

# docs = load_documents("data/policies")

# chunks = split_documents(docs)

# create_vector_store(chunks)

# print("Knowledge base created successfully!")