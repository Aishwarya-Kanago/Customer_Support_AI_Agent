from backend.app.rag.loader import load_documents

docs = load_documents("data/policies")

print(f"\nTotal Pages Loaded: {len(docs)}\n")

for i, doc in enumerate(docs):
    print("=" * 60)
    print(f"Document {i+1}")
    print(f"Source : {doc.metadata['source']}")
    print(f"Page   : {doc.metadata['page']}")
    print("-" * 60)
    print(doc.page_content[:150])
    print()