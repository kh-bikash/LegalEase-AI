import streamlit as st
import os
import fitz
from transformers import pipeline
from io import BytesIO
from fpdf import FPDF
import time

os.environ["TRANSFORMERS_NO_TF"] = "1"

# ---------------- Load Models Once ----------------
@st.cache_resource
def load_models():
    summarizer_model = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)
    qa_model_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", device=-1)
    return summarizer_model, qa_model_model

summarizer, qa_model = load_models()

st.set_page_config(page_title="LegalEase AI", layout="wide")
st.title("📜 LegalEase AI")
st.subheader("Demystifying Legal Documents with Generative AI")

# ---------------- Upload Document ----------------
uploaded_file = st.file_uploader("Upload a legal document (PDF or TXT)", type=["pdf", "txt"])
document_text = ""
pdf_doc = None

def extract_text_from_pdf(pdf_bytes):
    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in pdf:
        text += page.get_text()
    return text, pdf

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        document_text, pdf_doc = extract_text_from_pdf(uploaded_file.read())
    elif uploaded_file.type == "text/plain":
        document_text = uploaded_file.read().decode("utf-8")

    section = st.sidebar.radio("Navigate", ["Preview PDF/TXT", "Summarize", "Ask Questions", "Download Highlighted PDF"])

    # ---------------- Preview ----------------
    if section == "Preview PDF/TXT":
        st.subheader("📖 Document Preview")
        if uploaded_file.type == "application/pdf" and pdf_doc:
            for i, page in enumerate(pdf_doc):
                st.markdown(f"### Page {i+1}")
                st.text_area(f"Page {i+1}", page.get_text(), height=300)
        else:
            st.text_area("Document Content", document_text[:5000], height=400)

    # ---------------- Summarization ----------------
    elif section == "Summarize":
        st.subheader("📝 Document Summary")
        if st.button("Generate Summary"):
            with st.spinner("Generating summary..."):
                chunk_size = 800
                overlap = 100
                text_length = len(document_text)
                summary_text = ""
                start = 0
                progress_bar = st.progress(0)
                total_chunks = (text_length // (chunk_size - overlap)) + 1
                chunk_count = 0

                while start < text_length:
                    end = min(start + chunk_size, text_length)
                    chunk = document_text[start:end]
                    summary_chunk = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
                    summary_text += summary_chunk + " "
                    start += chunk_size - overlap
                    chunk_count += 1
                    progress_bar.progress(min(chunk_count / total_chunks, 1.0))
                    time.sleep(0.1)  # slight delay to update UI

            st.success("✅ Summary Generated")
            st.write(summary_text)

            # ---------------- Download Summary as PDF ----------------
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 6, summary_text)
            pdf_bytes = pdf.output(dest='S').encode('latin1')
            pdf_buffer = BytesIO(pdf_bytes)
            st.download_button("📥 Download Summary PDF", pdf_buffer, file_name="summary.pdf", mime="application/pdf")

    # ---------------- Q&A ----------------
    elif section == "Ask Questions":
        st.subheader("💬 Ask Questions about the Document")
        if "qa_history" not in st.session_state:
            st.session_state.qa_history = []

        question = st.text_input("Enter your question")
        if st.button("Get Answer") and question:
            with st.spinner("Finding best answer from document..."):
                chunk_size = 800
                overlap = 100
                best_answer = {"score": 0, "answer": "No answer found.", "context": ""}
                start = 0
                while start < len(document_text):
                    end = min(start + chunk_size, len(document_text))
                    chunk = document_text[start:end]
                    answer = qa_model(question=question, context=chunk)
                    if answer['score'] > best_answer['score']:
                        best_answer = {"score": answer['score'], "answer": answer['answer'], "context": chunk}
                    start += chunk_size - overlap

            st.session_state.qa_history.append({"question": question, "answer": best_answer['answer'], "context": best_answer['context']})

        # ---------------- Show Q&A History ----------------
        if st.session_state.qa_history:
            st.subheader("🗂️ Q&A History")
            for i, qa in enumerate(st.session_state.qa_history):
                st.markdown(f"**Q{i+1}:** {qa['question']}")
                st.markdown(f"**A{i+1}:** {qa['answer']}")

    # ---------------- Highlighted PDF ----------------
    elif section == "Download Highlighted PDF":
        if not pdf_doc:
            st.info("PDF highlighting works only with PDF files.")
        elif st.session_state.get("qa_history"):
            pdf_copy = fitz.open()
            pdf_copy.insert_pdf(pdf_doc)

            for qa in st.session_state.qa_history:
                answer = qa['answer']
                for page in pdf_copy:
                    for inst in page.search_for(answer):
                        highlight = page.add_highlight_annot(inst)
                        highlight.update()

            pdf_bytes = pdf_copy.write()
            pdf_buffer = BytesIO(pdf_bytes)
            st.download_button("📥 Download Highlighted PDF", pdf_buffer, file_name="highlighted_QA.pdf", mime="application/pdf")
        else:
            st.info("No Q&A found to highlight in PDF.")
