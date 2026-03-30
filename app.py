from flask import Flask
from rag_engine import initialize, ask as rag_ask

app = Flask(__name__)
rag_chain = None

@app.before_request
def load_rag():
    global rag_chain
    if rag_chain is None:
        try:
            rag_chain = initialize()
        except Exception as e:
            print(f"RAG failed: {e}")