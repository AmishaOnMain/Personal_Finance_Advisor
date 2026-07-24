# 💰 Personal Finance AI Advisor

An AI-powered Personal Finance Advisor for Indian users that combines **Retrieval-Augmented Generation (RAG)**, **live market data**, and **voice interaction** to answer finance-related questions.

The application retrieves information from official Indian financial documents, fetches real-time precious metal prices, and provides intelligent responses using Google's Gemini model.

---

# 🚀 Features

* 📄 Search official financial documents using RAG
* 💰 Live Gold and Silver prices (INR)
* 📚 GST and financial education lookup
* 🤖 AI-powered responses using Gemini 2.5 Flash
* 🎙️ Voice input using AssemblyAI Speech-to-Text
* 🔊 Voice output using Murf AI Text-to-Speech
* 💬 Interactive Gradio interface
* ⚡ Fast semantic search with ChromaDB

---

# 🛠️ Tech Stack

### Backend

* Python 3.12
* LangChain
* ChromaDB
* HuggingFace Embeddings

### AI

* Google Gemini 2.5 Flash
* Sentence Transformers
* AssemblyAI
* Murf AI

### Frontend

* Gradio

### APIs

* Gold API
* AssemblyAI API
* Murf AI API

---

# 📂 Project Structure

```text
Personal_Finance_Advisor/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── chroma_langchain_db/
│
└── venv/
```

---

# 📚 Knowledge Base

The chatbot indexes the following official documents:

* SEBI Financial Education Booklet
* CBIC GST Ready Reckoner

These PDFs are converted into embeddings and stored inside ChromaDB for semantic retrieval.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Personal_Finance_Advisor.git

cd Personal_Finance_Advisor
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GENAI_API_KEY=YOUR_GOOGLE_API_KEY

ASSEMBLYAI_API_KEY=YOUR_ASSEMBLYAI_API_KEY

MURF_API_KEY=YOUR_MURF_API_KEY
```

---

# ▶️ Running the Project

```bash
python app.py
```

Gradio will launch locally and provide:

* Text Chat Interface
* Voice Assistant Interface

---

# 💬 Example Questions

* What is the GST rate on laptops?
* What is the current gold price?
* How much GST do I pay on a gold chain?
* Explain tax-saving investment options.
* What are the benefits of mutual funds?

---

# 🧠 How It Works

1. Official finance PDFs are loaded using LangChain.
2. Documents are split into smaller chunks.
3. HuggingFace generates embeddings.
4. ChromaDB stores the vector embeddings.
5. User questions retrieve relevant document chunks.
6. Gemini generates responses using retrieved context.
7. Live market prices are fetched through the Gold API.
8. Voice queries are transcribed using AssemblyAI.
9. Responses are converted to speech using Murf AI.

---

# 📦 Main Dependencies

* langchain
* langchain-community
* langchain-huggingface
* langchain-chroma
* sentence-transformers
* chromadb
* gradio
* requests
* python-dotenv
* assemblyai

---

# 🌟 Future Improvements

* Support for Mutual Fund NAV lookup
* Stock Market Integration
* SIP Calculator
* EMI Calculator
* Income Tax Calculator
* Personal Budget Planner
* Financial Portfolio Analysis
* Multi-language Support
* User Authentication
* Chat History

---

# 📜 License

This project is intended for educational and learning purposes.

---

# 👩‍💻 Author

**Amisha Patel**

B.Tech Computer Science Engineering (Data Science)

Passionate about AI, Full Stack Development, and Building Real-World Intelligent Applications.
