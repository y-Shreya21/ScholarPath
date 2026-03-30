"""
chat_route.py
─────────────
Add these sections into your existing app.py.
This gives ScholarPath a /chat API endpoint + chatbot UI.
"""

# ════════════════════════════════════════════════════════════════
# STEP 1 — Add these imports at the TOP of your app.py
# ════════════════════════════════════════════════════════════════

from rag_engine import initialize, ask as rag_ask

# ════════════════════════════════════════════════════════════════
# STEP 2 — Add this block RIGHT AFTER app = Flask(__name__)
# ════════════════════════════════════════════════════════════════

# Initialize RAG chain once when app starts (not on every request)
rag_chain = None

@app.before_request
def load_rag():
    global rag_chain
    if rag_chain is None:
        try:
            rag_chain = initialize()
            print("RAG chain loaded successfully")
        except Exception as e:
            print(f"RAG chain failed to load: {e}")
            rag_chain = None

# ════════════════════════════════════════════════════════════════
# STEP 3 — Add this route to your app.py
# ════════════════════════════════════════════════════════════════

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """Chatbot page — GET shows UI, POST returns AI answer."""
    if request.method == 'GET':
        return render_template('chat.html')

    # POST: handle AJAX question from frontend
    data = request.get_json()
    question = data.get('question', '').strip()

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    if len(question) > 500:
        return jsonify({'error': 'Question too long (max 500 characters)'}), 400

    if rag_chain is None:
        return jsonify({
            'answer': 'ScholarBot is currently unavailable. Please try again later or contact admin.',
            'sources': []
        })

    try:
        result = rag_ask(question, rag_chain)
        return jsonify(result)
    except Exception as e:
        print(f"RAG error: {e}")
        return jsonify({
            'answer': 'Sorry, I could not process your question. Please try again.',
            'sources': []
        }), 500