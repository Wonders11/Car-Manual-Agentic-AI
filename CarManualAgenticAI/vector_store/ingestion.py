from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import AstraDB
from langchain.embeddings.openai import OpenAIEmbeddings

def ingest_pdf(pdf_path, metadata):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    
    for chunk in chunks:
        chunk.metadata.update(metadata)
    
    return chunks

def store_chunks(chunks):
    vector_store = AstraDB.from_existing_index(
        embedding=OpenAIEmbeddings(),
        collection_name="car_manuals"
    )
    vector_store.add_documents(chunks)
