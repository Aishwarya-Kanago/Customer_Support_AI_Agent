from backend.app.rag.loader import load_documents
from backend.app.rag.splitter import split_documents

docs = load_documents("data/policies")

chunks = split_documents(docs)

print(len(chunks))

print(chunks[0].page_content)