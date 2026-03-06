import streamlit as st
from chatbot import get_response, load_faq, build_index

# load dữ liệu
df = load_faq("faq.tsv")
vectorizer, faq_matrix = build_index(df)

st.title("🎓 CTU Chatbot")

user_input = st.text_input("Nhập câu hỏi")

if user_input:
    answer, suggestions = get_response(user_input, df, vectorizer, faq_matrix)

    st.write("Bot:", answer)

    if suggestions:
        st.write("Gợi ý:")
        for s in suggestions:
            st.write("-", s)
