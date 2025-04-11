from utils import split_text
from rag import create_embeddings, initialize_chroma, ingest_chunks

def main():
    # Read the document
    with open("data/document.txt", "r", encoding="utf-8") as file:
        raw_text = file.read()

    # Split text into chunks
    chunks = split_text(raw_text)

    # Create embeddings and initialize ChromaDB
    embeddings = create_embeddings()
    db = initialize_chroma(embeddings)

    # save chunks to ChromaDB
    ingest_chunks(chunks, db)

    print("✅ Documento indexado correctamente en ChromaDB.")

if __name__ == "__main__":
    main()
