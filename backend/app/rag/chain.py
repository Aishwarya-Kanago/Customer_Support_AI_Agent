from app.core.model import llm
from app.prompts.rag_prompt import rag_prompt
from app.rag.retriever import retriever


def ask(question: str):
    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    chain = rag_prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    # Remove duplicate source files while preserving order
    sources = list(dict.fromkeys(
        doc.metadata["source"] for doc in docs
    ))

    return {
        "answer": response.content,
        "sources": sources,
    }