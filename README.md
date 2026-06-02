# PDF Chatbot

Upload any PDF and ask questions about it. The chatbot retrieves relevant 
content from the document and answers based strictly on what's in the PDF.

## Overview

A lightweight RAG pipeline that lets you have a conversation with any PDF 
document — useful for quickly extracting information from reports, manuals, 
or research papers without reading the entire document.

## How It Works

1. **Upload** — User uploads a PDF document
2. **Chunk & Embed** — Document is split into chunks and converted to vector embeddings
3. **Retrieve** — Semantic search finds the most relevant chunks for each question
4. **Answer** — LLM generates a response grounded in the retrieved content

## Features

- Upload any PDF and start querying immediately
- Answers are strictly grounded in the document — no hallucinated responses
- Simple single-file app, easy to extend

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| PDF Processing | PyMuPDF / PyPDF |
| Embeddings | OpenAI Embeddings |
| Vector Store | FAISS |
| LLM | OpenAI GPT |
| Interface | Streamlit |
## Keywords: AI, Artificial Intelligence
