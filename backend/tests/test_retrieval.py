from app.rag.retriever import retriever

docs = retriever.invoke(
    "Can I return shoes after 30 days?"
)

print(f"Retrieved {len(docs)} documents\n")

for doc in docs:
    print("=" * 60)
    print(doc.metadata)
    print(doc.page_content)