# =========================
# IMPORTS
# =========================
import json
import os
import tempfile

import assemblyai as aai
import gradio as gr
import requests
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# =========================
# LOAD ENVIRONMENT VARIABLES
# =========================
load_dotenv()


# =========================
# LOAD PDF DOCUMENTS
# =========================
pdf_urls = [
    "https://investor.sebi.gov.in/pdf/downloadable-documents/Financial%20Education%20Booklet%20-%20English.pdf",
    "https://a2ztaxcorp.net/wp-content/uploads/2025/09/CBIC-GST-Ready-Reckoner-indicating-updated-Central-Goods-and-Services-Tax-CGST-rates-on-goods.pdf",
]

all_documents = []

for url in pdf_urls:
    loader = PyPDFLoader(url)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages from {url.split('/')[-1]}")
    all_documents.extend(documents)


# =========================
# SPLIT DOCUMENTS
# =========================
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = text_splitter.split_documents(all_documents)

print(f"Total chunks: {len(chunks)}")


# =========================
# CREATE EMBEDDINGS
# =========================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)


# =========================
# CREATE VECTOR DATABASE
# =========================
vector_store = Chroma(
    collection_name="finance_docs",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)

vector_store.add_documents(documents=chunks)

print("Knowledge base ready!")


# =========================
# TEST VECTOR SEARCH
# =========================
results = vector_store.similarity_search(
    "What is the GST rate on laptops?",
    k=3,
)

for doc in results:
    source = doc.metadata.get("source", "Unknown")
    page = doc.metadata.get("page", "N/A")

    print(f"Source: {source} (Page {page + 1})")
    print(f"Content: {doc.page_content[:200]}...")
    print()


# =========================
# TOOL : SEARCH FINANCE DOCUMENTS
# =========================
@tool
def search_finance_docs(question: str) -> str:
    """
    Search official Indian government financial documents for rules,
    regulations, tax rates, investment guidance,
    and financial education content.
    """

    results = vector_store.similarity_search(question, k=3)

    if not results:
        return "No relevant information found in the knowledge base."

    context = ""

    for doc in results:
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "N/A")

        context += f"Source: {source} (Page {page + 1})\n"
        context += f"Content: {doc.page_content}\n\n"

    return context


# =========================
# TEST GOLD API
# =========================
url = "https://api.gold-api.com/price/XAU/INR"

response = requests.get(url)
data = response.json()

price_per_gram = data["price"] / 31.1035

print(f"Gold: ₹{price_per_gram:.2f} per gram")


# =========================
# TOOL : MARKET PRICE
# =========================
@tool
def get_market_price(asset: str) -> str:
    """
    Get current market price for a financial asset
    in Indian Rupees.

    Supported:
    - gold
    - silver
    """

    symbols = {
        "gold": "XAU",
        "silver": "XAG",
    }

    symbol = symbols.get(asset.lower())

    if not symbol:
        return "Supported assets: gold, silver"

    url = f"https://api.gold-api.com/price/{symbol}/INR"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        price = data.get("price")

        if price:
            price_per_gram = price / 31.1035

            return (
                f"{asset.title()}: ₹{price_per_gram:.2f} per gram "
                f"(₹{price:.2f} per troy ounce). "
                f"Source: Gold-API"
            )

    return f"Could not fetch price for {asset}"


# =========================
# INITIALIZE GEMINI MODEL
# =========================
api_key = os.getenv("GENAI_API_KEY")

model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=api_key,
)


# =========================
# SYSTEM PROMPT
# =========================
system_prompt = """
You are a Personal Finance AI Advisor for Indian citizens.

You have access to these tools:

- search_finance_docs:
  Search official Indian government documents for GST rates,
  investment guidance, tax saving options,
  and financial education.

- get_market_price:
  Get live market prices for gold and silver in Indian Rupees.

Help the user by looking up relevant data using your tools
and giving clear, specific answers with actual numbers and rates.

Always mention the source of your information.

All monetary values should be in Indian Rupees (₹)
unless specified otherwise.
"""


# =========================
# CREATE AGENT
# =========================
agent = create_agent(
    model=model,
    tools=[
        search_finance_docs,
        get_market_price,
    ],
    system_prompt=system_prompt,
)


# =========================
# TEST QUERY 1
# =========================
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the current gold price?",
            }
        ]
    }
)

print(response["messages"][-1].content)


# =========================
# TEST QUERY 2
# =========================
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "I want to buy a gold chain. "
                    "What's the current gold price "
                    "and how much GST will I pay?"
                ),
            }
        ]
    }
)

print(response["messages"][-1].content)


# =========================
# TEXT CHAT FUNCTION
# =========================
def finance_advisor(question):
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    return response["messages"][-1].content


# =========================
# TEXT GRADIO UI
# =========================
demo = gr.Interface(
    fn=finance_advisor,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask a finance question...",
        label="Question",
    ),
    outputs=gr.Textbox(
        lines=10,
        label="Answer",
    ),
    title="Personal Finance AI Advisor",
    description=(
        "Ask about gold prices, silver prices, "
        "GST rates, tax saving options, and more."
    ),
)

demo.launch(debug=True)


# =========================
# API KEYS
# =========================
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
MURF_API_KEY = os.getenv("MURF_API_KEY")

aai.settings.api_key = ASSEMBLYAI_API_KEY


# =========================
# SPEECH TO TEXT
# =========================
def speech_to_text(audio_path):
    """
    Converts an audio file to text
    using AssemblyAI.
    """

    transcriber = aai.Transcriber()

    config = aai.TranscriptionConfig(
        speech_models=["universal-3-pro", "universal-2"],
        language_detection=True,
        speaker_labels=True,
    )

    transcript = transcriber.transcribe(
        audio_path,
        config=config,
    )

    return transcript.text if transcript.text else ""


# =========================
# TEXT TO SPEECH
# =========================
def text_to_speech(text):
    """
    Converts text to MP3
    using Murf AI.
    """

    url = "https://global.api.murf.ai/v1/speech/stream"

    payload = {
        "text": text,
        "voiceId": "en-US-natalie",
        "model": "FALCON",
        "multiNativeLocale": "en-US",
        "sampleRate": 24000,
        "format": "MP3",
    }

    headers = {
        "Content-Type": "application/json",
        "api-key": MURF_API_KEY,
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(payload),
    )

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3",
    )

    temp_file.write(response.content)
    temp_file.close()

    return temp_file.name


# =========================
# VOICE CHAT FUNCTION
# =========================
def finance_advisor_voice(audio):
    if audio is None:
        return (
            "No audio recorded.",
            "Please record your question first.",
            None,
        )

    question = speech_to_text(audio)

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    answer = response["messages"][-1].content

    audio_path = text_to_speech(answer)

    return (
        question,
        answer,
        audio_path,
    )


# =========================
# VOICE GRADIO UI
# =========================
voice_demo = gr.Interface(
    fn=finance_advisor_voice,
    inputs=gr.Audio(
        sources=["microphone", "upload"],
        type="filepath",
        label="Ask your question",
    ),
    outputs=[
        gr.Textbox(label="Your Question (transcribed)"),
        gr.Textbox(
            lines=10,
            label="Answer",
        ),
        gr.Audio(label="Answer (audio)"),
    ],
    title="Personal Finance AI Advisor (Voice)",
    description=(
        "Speak your finance question and get both "
        "a text and audio response."
    ),
)

voice_demo.launch(
    debug=True,
    share=True,
)