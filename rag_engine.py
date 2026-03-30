"""
rag_engine.py
─────────────
ScholarPath RAG Pipeline using LangChain + ChromaDB + Gemini
Run once to build the vector store, then use ask() for queries.
"""

import os
from knowledge_base import SCHOLARSHIP_DOCS

# ─── LANGCHAIN IMPORTS ────────────────────────────────────────────────────────
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# ─── CONFIG ───────────────────────────────────────────────────────────────────
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "your-gemini-api-key-here")
CHROMA_DB_DIR  = "./chroma_db"          # Where ChromaDB stores its data locally
COLLECTION     = "scholarpath_kb"       # Collection name inside ChromaDB

# ─── SYSTEM PROMPT ────────────────────────────────────────────────────────────
PROMPT_TEMPLATE = """
You are ScholarBot, a helpful assistant for the ScholarPath scholarship management system.
Answer the student's question using ONLY the context provided below.
Be friendly, concise, and specific. If the answer is not in the context, say:
"I don't have that information. Please contact the admin team for help."

Context:
{context}

Student Question: {question}

Answer:
"""

# ─── BUILD VECTOR STORE ───────────────────────────────────────────────────────
def build_vector_store():
    """
    Converts SCHOLARSHIP_DOCS into LangChain Document objects,
    embeds them using Gemini embeddings, and stores in ChromaDB.
    Run this once (or whenever you update knowledge_base.py).
    """
    print("Building vector store...")

    # Convert our knowledge base dicts into LangChain Documents
    documents = [
        Document(
            page_content=doc["text"].strip(),
            metadata={**doc["metadata"], "id": doc["id"]}
        )
        for doc in SCHOLARSHIP_DOCS
    ]

    # Create embeddings using Google Gemini
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GEMINI_API_KEY
    )

    # Store in ChromaDB (persisted locally on disk)
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=COLLECTION,
        persist_directory=CHROMA_DB_DIR
    )
    vector_store.persist()
    print(f"Vector store built with {len(documents)} documents → saved to {CHROMA_DB_DIR}")
    return vector_store


# ─── LOAD EXISTING VECTOR STORE ───────────────────────────────────────────────
def load_vector_store():
    """Load an already-built ChromaDB store from disk."""
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GEMINI_API_KEY
    )
    vector_store = Chroma(
        collection_name=COLLECTION,
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_DIR
    )
    return vector_store


# ─── BUILD RAG CHAIN ─────────────────────────────────────────────────────────
def build_rag_chain(vector_store):
    """
    Builds a RetrievalQA chain:
    User question → ChromaDB retrieves top 3 relevant docs
    → Gemini generates answer grounded in those docs
    """
    # LLM: Gemini 1.5 Flash (free tier, fast)
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0.2          # Low temp = factual, consistent answers
    )

    # Retriever: fetch top 3 most relevant knowledge base chunks
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # Custom prompt
    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

    # Full RAG chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",               # "stuff" = paste all retrieved docs into prompt
        retriever=retriever,
        return_source_documents=True,     # So we can show sources in UI
        chain_type_kwargs={"prompt": prompt}
    )
    return chain


# ─── MAIN ask() FUNCTION ──────────────────────────────────────────────────────
def ask(question: str, chain) -> dict:
    """
    Main function Flask will call.
    Returns: { answer: str, sources: list[str] }
    """
    result = chain.invoke({"query": question})

    # Extract source categories for transparency
    sources = list({
        doc.metadata.get("category", "general")
        for doc in result.get("source_documents", [])
    })

    return {
        "answer": result["result"],
        "sources": sources
    }


# ─── ONE-TIME SETUP ──────────────────────────────────────────────────────────
def initialize():
    """
    Call this once when Flask app starts.
    Builds DB if it doesn't exist, loads it if it does.
    Returns the RAG chain ready to use.
    """
    import os
    if os.path.exists(CHROMA_DB_DIR) and os.listdir(CHROMA_DB_DIR):
        print("Loading existing ChromaDB...")
        vs = load_vector_store()
    else:
        vs = build_vector_store()
    return build_rag_chain(vs)


# ─── QUICK TEST ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    chain = initialize()
    test_questions = [
        "I scored 78% and my family income is Rs 2.5 lakh. Am I eligible?",
        "What documents do I need to upload?",
        "How long does approval take?",
        "My application shows PENDING. What does that mean?",
    ]
    for q in test_questions:
        print(f"\nQ: {q}")
        res = ask(q, chain)
        print(f"A: {res['answer']}")
        print(f"Sources: {res['sources']}")