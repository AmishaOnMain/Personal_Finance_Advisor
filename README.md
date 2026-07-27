# 💰 Personal Finance AI Advisor

An AI-powered Personal Finance Assistant for Indian users that combines **Retrieval-Augmented Generation (RAG)** with **live financial data** and **voice interaction**.

Built using **LangChain**, **Google Gemini 2.5 Flash**, **ChromaDB**, **Hugging Face Embeddings**, **Gradio**, **AssemblyAI**, and **Murf AI**.

---

## 🚀 Features

- 📄 Search official Indian financial documents using RAG
- 🏦 Get information from:
  - SEBI Financial Education Booklet
  - GST Ready Reckoner
- 🥇 Fetch live Gold & Silver prices in INR
- 🤖 AI-powered financial assistant using Gemini 2.5 Flash
- 🎙️ Voice input using AssemblyAI Speech-to-Text
- 🔊 Voice responses using Murf AI Text-to-Speech
- 🌐 Interactive Gradio web interface
- ⚡ Fast semantic search with ChromaDB

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| LLM | Google Gemini 2.5 Flash |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | Hugging Face (all-mpnet-base-v2) |
| Document Loader | PyPDFLoader |
| Text Splitter | RecursiveCharacterTextSplitter |
| UI | Gradio |
| Speech-to-Text | AssemblyAI |
| Text-to-Speech | Murf AI |
| Market Data | Gold API |

---

## 📚 Knowledge Base

The assistant uses Retrieval-Augmented Generation (RAG) over official financial documents including:

- SEBI Financial Education Booklet
- GST Ready Reckoner

Documents are:

1. Loaded using PyPDFLoader
2. Split into chunks
3. Converted into embeddings
4. Stored inside ChromaDB
5. Retrieved using semantic similarity search

---

## ⚙️ Workflow

```text
User Question
      │
      ▼
Gemini Agent
      │
      ├────────► Finance Document Search Tool (RAG)
      │
      ├────────► Live Gold/Silver Price Tool
      │
      ▼
Generated Response
      │
      ├── Text Output
      └── Voice Output (Optional)
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/AmishaOnMain/Personal-Finance-AI-Advisor.git

cd Personal-Finance-AI-Advisor
```

Install dependencies

```bash
pip install -U \
langchain \
langchain-community \
langchain-text-splitters \
langchain-huggingface \
langchain-chroma \
langchain-google-genai \
sentence-transformers \
chromadb \
gradio \
assemblyai \
pypdf
```

---

## 🔑 API Keys Required

Create the following API keys:

- Gemini API Key
- AssemblyAI API Key
- Murf AI API Key

Store them in Google Colab Secrets as:

```
GEMINI_API_KEY
ASSEMBLYAI_API_KEY
MURF_API_KEY
```

---

## ▶️ Running the Project

Run the notebook step by step.

The project will:

- Download official finance documents
- Create the vector database
- Initialize the Gemini agent
- Launch the Gradio web application
- Launch the Voice Assistant interface

---

## 💬 Example Questions

- What is the current gold price?
- What is the GST rate on laptops?
- How much GST will I pay on a gold chain?
- Explain tax-saving investment options.
- What are the basic financial planning tips according to SEBI?

---



---

## 🧠 Concepts Used

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Embeddings
- Tool Calling
- AI Agents
- Speech Recognition
- Text-to-Speech
- Prompt Engineering

---

## 📸 Preview

> Add a screenshot of your Gradio interface here.

Example:

```
images/preview.png
```

---

## 🔮 Future Improvements

- Support for Mutual Funds
- SIP Calculator
- Stock Market Integration
- Budget Planner
- Expense Tracking
- Multi-language Support
- PDF Report Generation
- Investment Recommendation Dashboard

---

## 👩‍💻 Author

**Amisha Patel**

GitHub: https://github.com/AmishaOnMain

---

## 📄 License

This project is open-source and available under the MIT License.
