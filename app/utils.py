import os
import fitz
import docx

# Split text into several chunks for embedding
# and storage in ChromaDB
def split_text(text, chunk_size=200, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

# load file content based on its extension
def load_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext in [".txt", ".md", ".log"]:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    
    elif ext == ".pdf":
        text = ""
        with fitz.open(filepath) as pdf:
            for page in pdf:
                text += page.get_text()
        return text
    
    elif ext == ".docx":
        doc = docx.Document(filepath)
        return "\n".join([p.text for p in doc.paragraphs])
    
    else:
        print(f"⚠️ No se puede leer el tipo de archivo: {ext}")
        return ""