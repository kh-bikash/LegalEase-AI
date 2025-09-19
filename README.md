# 📜 LegalEase-AI

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-v1.27-orange?logo=streamlit)
![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-orange?logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-green)

> **Demystifying Legal Documents with Generative AI**  
> LegalEase-AI is an AI-powered tool to summarize, question, and highlight PDF/TXT legal documents for faster understanding.

---

## 🔗 Live Demo
Check out the working demo on Hugging Face Spaces:  
[**LegalEase-AI Live**](https://huggingface.co/spaces/Bikashkh/legalease-ai)

---

## 🎬 Demo GIF
![Demo](docs/demo.gif)

> GIF shows: uploading PDF, generating summary, asking questions, and downloading highlighted PDF.

---

## 📝 Features
- ✅ Upload and preview **PDF and TXT legal documents**
- ✅ **Summarization** using `facebook/bart-large-cnn`
- ✅ **Question-Answering** using `distilbert-base-cased-distilled-squad`
- ✅ **Downloadable summary PDF**
- ✅ **Highlighted PDF** with Q&A answers
- ✅ **Q&A History** for reference

---

## ⚡ How It Works
1. Upload your legal document.
2. Preview the content page by page (PDF) or full text (TXT).
3. Generate a concise summary.
4. Ask questions to extract answers from the document.
5. Download the highlighted PDF with your Q&A results.

---

## 🛠 Installation (Local)
```bash
# Clone the repo
git clone https://github.com/kh-bikash/LegalEase-AI.git
cd LegalEase-AI

# Create virtual environment (Windows)
python -m venv .venv
.\.venv\Scripts\activate

# Create virtual environment (Linux/Mac)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
