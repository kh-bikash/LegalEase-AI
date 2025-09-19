# 📜 LegalEase-AI

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-v1.27-orange?logo=streamlit)
![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-orange?logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-green)

> **Demystifying Legal Documents with Generative AI**  
> LegalEase-AI is a sleek AI-powered tool to **summarize, question, and highlight PDF/TXT legal documents** for faster understanding and efficient document handling.

---

## 🚀 Live Demo
Experience the AI in action:  
[**🎯 LegalEase-AI on Streamlit**](https://legaleaseai.streamlit.app/)

---

## 🎬 Demo Preview
![Demo](docs/demo.gif)

> **Highlights:** Upload PDF → Summarize → Ask Questions → Download Highlighted PDF

---

## 🌟 Features

| Feature | Description |
|---------|-------------|
| 📄 Upload Documents | Upload and preview **PDF and TXT legal documents** easily |
| 📝 Summarization | Summarize documents using `facebook/bart-large-cnn` |
| ❓ Q&A | Ask questions using `distilbert-base-cased-distilled-squad` |
| 💾 Download | Save your **highlighted PDFs** and **summaries** |
| 📚 History | Keep track of **all Q&A sessions** for reference |

---

## ⚡ How It Works

1. **Upload Document** – Drag & drop PDF or TXT file.  
2. **Preview Content** – Flip through PDF pages or view full text.  
3. **Generate Summary** – AI creates a concise summary of your legal document.  
4. **Ask Questions** – Extract precise answers from the document.  
5. **Download Results** – Save the highlighted PDF with answers and summaries.

---

## 🖥 Installation (Local)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/kh-bikash/LegalEase-AI.git
cd LegalEase-AI

# 2️⃣ Create a virtual environment (Windows)
python -m venv .venv
.\.venv\Scripts\activate

# 2️⃣ Create a virtual environment (Linux/Mac)
python3 -m venv .venv
source .venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run locally
streamlit run app.py
