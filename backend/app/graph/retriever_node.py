from app.rag.retriever import retriever


def retrieve_documents(state):

    question = state["messages"][-1].content

    docs = retriever.invoke(question)

    return {
        "documents": docs
    }