# 🧠 Mini RAG con ChromaDB, Hugging Face y Docker

Este proyecto es un ejemplo básico de un sistema **RAG (Retrieval-Augmented Generation)**.

Permite hacer preguntas sobre varios documentos  `.txt`, `.md`, `.log`, `.pdf` o `.docx` usando:

- 🧬 Embeddings generados con Hugging Face
- 🔎 Búsqueda semántica con ChromaDB
- 🧠 Generación de respuestas con un LLM (vía Hugging Face Inference API)

---

## 🚀 Tecnologías usadas

- Python
- ChromaDB (en Docker)
- Hugging Face Transformers
- LangChain
- Hugging Face Inference API

---

## 📆 Instalación

```bash
git clone https://github.com/cristianordonezdev/mini-rag.git
cd mini-rag
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt
```

---

## 🐳 Levantar ChromaDB con Docker

```bash
docker compose up -d
```

---

## 🔐 Configurar Hugging Face Token

Crea un archivo `.env` en la raíz del proyecto con:

```
HF_API_TOKEN=tu_token_de_huggingface
```

---

## 📄 Indexar documento

Coloca los documentos en `data/` y luego ejecuta:

```bash
python app/index.py
```

---

## 💬 Hacer una pregunta

```bash
python app/ask.py
```

---

## 📝 Autor

- Proyecto de práctica RAG por cristianordonezdev

