from flask import Flask, request, jsonify
from chatbot import load_faq, build_index, get_response

FAQPATH = "faq.tsv"

app = Flask(__name__)

df = load_faq(FAQPATH)
vectorizer, faqmatrix = build_index(df)

@app.get("/")
def home():
    return "CTU chatbot is running"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    answer, suggestions = get_response(message, df, vectorizer, faqmatrix)
    return jsonify({"answer": answer, "suggestions": suggestions})
