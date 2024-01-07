import os
import pandas as pd
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
import re
import numpy as np
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


# Get all pdf files from a directory
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader




def preprocess_pdf_files_for_LLM(path: str):
    pdf_docs = []
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            pdf_docs.append(os.path.join(path, file))
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore

def preprocess_csv_files_for_LLM(path: str):
    csv_docs = []
    for file in os.listdir(path):
        if file.endswith(".csv"):
            csv_docs.append(os.path.join(path, file))
    text = ""
    for csv in csv_docs:
        df = pd.read_csv(csv)
        for col in df.columns:
            text += col + "\n"
            for row in df[col]:
                text += str(row) + "\n"
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore
