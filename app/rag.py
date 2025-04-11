from langchain_community.vectorstores.chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import chromadb
from uuid import uuid4

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

    # to delete collection
    # try:
    #     chroma_client.delete_collection(name=COLLECTION_NAME)
    #     print("🗑️ Colección anterior eliminada por completo.")
    #     return
    # except Exception as e:
    #     print(f"⚠️ No se pudo eliminar la colección (puede no existir): {e}")
        
    db = Chroma(
        client=chroma_client,
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_function
    )
    return db

# Add chunks to ChromaDB
def ingest_chunks(chunks, db):

    # try to delete all previous documents
    try:
        print("🧹 Eliminando documentos anteriores...")
        existing_docs = db.similarity_search("document", k=1000)
        print(f"📦 {len(existing_docs)} documentos encontrados antes de eliminar.")
        print("🗑️ Todos los documentos anteriores eliminados.")
    except Exception as e:
        print(f"⚠️ Error al intentar eliminar documentos: {e}")
        return

    # prepare documents for ChromaDB
    docs = [
        Document(
            page_content=chunk,
            metadata={"source": f"chunk_{uuid4()}"}
        ) for chunk in chunks
    ]
        
    # add documents to ChromaDB
    db.add_documents(docs)
    print(f"✅ {len(docs)} nuevos chunks agregados.")