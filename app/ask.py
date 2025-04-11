from rag import create_embeddings, initialize_chroma
# from transformers import pipeline
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Create embeddings and initialize ChromaDB
embeddings = create_embeddings()
db = initialize_chroma(embeddings)

# Load key from .env file
load_dotenv()
HF_TOKEN = os.getenv("HF_API_TOKEN")

# Cliet API Info
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN,
)

# # Load the model for question answering
# qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")


# Function to ask a question and get an answer
def ask_question(question):

    # search for similar documents or 3 chunks more similar to the question
    results = db.similarity_search(question, k=3)

    # join all the results into a single context
    context = "\n".join([doc.page_content for doc in results])


    # Generate the prompt for the model
    prompt = f"Contexto: {context}\n\nPregunta: {question}"

    # Generate the answer using the model by local
    # response = qa_pipeline(prompt, max_length=200)[0]['generated_text']
    # Prompt estilo instruct
    prompt = f"[INST] Usa el siguiente contexto para responder con precisión:\n{context}\n\nPregunta: {question} [/INST]"

    # Generate the answer using the model by API
    response = client.text_generation(
        prompt,
        max_new_tokens=300,
        temperature=0.7,
        do_sample=True,
        repetition_penalty=1.2
    )
    
    # Print the response
    print("\n🤖 Respuesta generada:")
    print(response.strip())

if __name__ == "__main__":
    question = input("❓ Escribe tu pregunta: ")
    ask_question(question)
