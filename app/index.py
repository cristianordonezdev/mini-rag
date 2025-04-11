import os
from utils import split_text, load_file
from rag import create_embeddings, initialize_chroma, ingest_chunks

def main():
    data_dir = "data"
    all_text = ""

    # read all files in the data directory
    for filename in os.listdir(data_dir):
        path = os.path.join(data_dir, filename)
        if os.path.isfile(path):
            content = load_file(path)
            if content:
                all_text += f"\n\n--- Documento: {filename} ---\n\n"
                all_text += content

    chunks = split_text(all_text)
    embeddings = create_embeddings()
    db = initialize_chroma(embeddings)
    ingest_chunks(chunks, db)

    print("✅ Archivos indexados correctamente.")
if __name__ == "__main__":
    main()