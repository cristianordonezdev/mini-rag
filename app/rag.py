from langchain_community.vectorstores.chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import chromadb

# Where ChromaDB is running
# ChromaDB is running on localhost:8000 by docker-compose
CHROMA_HOST = "http://localhost:8000"
COLLECTION_NAME = "docs"

# load IA model from huggingface 
def create_embeddings():
    # this model is special because turn text into embeddings or vectors
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Prepare ChromaDB client and collection
def initialize_chroma(embedding_function):
    chroma_client = chromadb.HttpClient(host="localhost", port=8000)
    db = Chroma(
        client=chroma_client,
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_function
    )
    return db

# Add chunks to ChromaDB
def ingest_chunks(chunks, db):

    # clear previous collection
    db.delete_collection()
    
    # turn into documents every chunk
    docs = [Document(page_content=chunk, metadata={"source": f"chunk_{i}"}) for i, chunk in enumerate(chunks)]

    # add documents to ChromaDB
    db.add_documents(docs)
    db.persist()

    print("✅ Chunks agregados")
