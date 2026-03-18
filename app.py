
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
#from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
#from langchain_classic.retrievers import 
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from dotenv import load_dotenv

import os


load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
#DATA INGESTION AND LOADING
#loader=PyPDFLoader("DATA605_Foleys3_final_report (3).pdf")

st.title("Simple PDF Chatbot")

if "retrieval_chain" not in st.session_state:
    st.session_state.retrieval_chain = None
if "current_file" not in st.session_state:
    st.session_state.current_file = None
# File uploader
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

#input_text = st.text_input("Search the topic you want")
if uploaded_file:
    if st.session_state.current_file != uploaded_file.name:  # ← NEW CHECK
        st.session_state.current_file = uploaded_file.name   # ← SAVE NAME
        st.session_state.retrieval_chain = None
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())
            # Load and process
    loader = PyPDFLoader("temp.pdf")
    pdf_docs = loader.load()
#DATA SPITTING
    pdf_splitting=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    documents=pdf_splitting.split_documents(pdf_docs)
#VECTOR DB AND EMBEDDINGS
    vector_db=Chroma.from_documents(documents,OpenAIEmbeddings(),collection_name="CHATBOT-PDF")

    retrivr=vector_db.as_retriever()
    llm=ChatOpenAI(
    model="gpt-3.5-turbo",temperature=0
    )

    prompt=ChatPromptTemplate.from_template(
    """Answer the following question based on the provided context.
    Think thoroughly before providing an answer.
    <context>
    {context}
    </context>
    Question:{input}
    """
    )

    document_chain = create_stuff_documents_chain(llm,prompt)
    retrieval_chain = create_retrieval_chain(retrivr,document_chain)

    input_text = st.chat_input("Ask anything about the PDF...")
    if input_text:
        response=retrieval_chain.invoke({"input":input_text})
        st.write(response['answer'])

