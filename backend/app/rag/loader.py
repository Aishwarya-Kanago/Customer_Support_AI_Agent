# from pathlib import Path

# from langchain_community.document_loaders import PyPDFLoader


# def load_documents(data_dir: str):
#     documents = []

#     pdf_files = Path(data_dir).glob("*.pdf")

#     for pdf in pdf_files:
#         loader = PyPDFLoader(str(pdf))
#         documents.extend(loader.load())

#     return documents

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_documents(data_dir: str):
    documents = []

    path = Path(data_dir)

    print("Current working directory:", Path.cwd())
    print("Searching in:", path.resolve())
    print("Exists:", path.exists())

    pdf_files = list(path.glob("*.pdf"))
    print("PDFs found:", pdf_files)

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    return documents