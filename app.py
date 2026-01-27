import streamlit as st
from dotenv import load_dotenv
from graph.graph import app as rag_app

load_dotenv()

st.set_page_config(page_title="Corrective RAG", page_icon="🤖")

lang = st.selectbox("Dil / Language", ["Türkçe", "English"])
if lang == "Türkçe":
    title = "Corrective RAG"
    subtitle = "Sana nasıl yardımcı olabilirim?"
    question_label = "Soru"
    placeholder = "Örn: Prompt engineering nedir?"
    button_label = "Cevabı üret"
    empty_warning = "Lütfen bir soru yaz."
    thinking = "Cevap hazırlanıyor..."
    ready = "Cevap hazır"
    fallback = "Cevap üretilemedi"
else:
    title = "Corrective RAG"
    subtitle = "How can I help you?"
    question_label = "Question"
    placeholder = "e.g., What is prompt engineering?"
    button_label = "Generate answer"
    empty_warning = "Please enter a question."
    thinking = "Generating answer..."
    ready = "Answer ready"
    fallback = "No answer was generated."

st.title(title)
st.write(subtitle)

question = st.text_input(question_label, placeholder=placeholder)

if st.button(button_label):
    if not question.strip():
        st.warning(empty_warning)
    else:
        with st.spinner(thinking):
            result = rag_app.invoke({"question": question})
        st.success(ready)
        answer = result.get("generation", fallback)
        st.write(answer)
