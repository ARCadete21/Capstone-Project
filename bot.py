import os
import pandas as pd
import re
import numpy as np

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader, CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.llms import CTransformers
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI


from functions import *
from
###################################### LOADING DATA FOR THE BOT #########################################

'''#LOAD TEXT DATA
loader_pdfs = DirectoryLoader('data/DataFiltered2022_2023/data filtered',
                              show_progress=True, use_multithreading=True,
                              loader_cls=TextLoader, glob='**/*.pdf')

pdfs = loader_pdfs.load()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len)

chunks = text_splitter.split_text(pdfs)

embeddings = OpenAIEmbeddings()
# embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
'''

'''#LOAD CSV DATA
loader = DirectoryLoader('data/DataFiltered2022_2023/data filtered',
                         glob="**/*.csv", loader_cls=CSVLoader)
csv_data = loader.load()

#from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

recursive_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=750,
    chunk_overlap=200,
)
text_chunks = recursive_text_splitter.split_documents(csv_data)


embeddings = OpenAIEmbeddings()
#embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")


#embeddings = OpenAIEmbeddings()
# embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
db = FAISS.from_documents(text_chunks, embeddings)
'''



########################### QUERY ############################

query = "Who won the 2023 Bahrain GP?"
docs = db.similarity_search(query, k=3)
print("Results:", docs)

#############################################################

#llm = CTransformers(model_type="gpt-3.5-turbo", temperature=0.1)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.1)

pdf_data = preprocess_pdf_files_for_LLM(path = 'data/DataFiltered2022_2023/data filtered')

qa = ConversationalRetrievalChain.from_llm(llm, retriever = pdf_data.as_retriever())

while True:
    # Give system some context
    chat_history = []
    query = input("Enter query: ")
    if query == "exit":
        break
    if query == "clear":
        chat_history = []
        continue
    if query == "":
        continue
    
    
    results = qa({"chat_history": chat_history, "question": query})
    print('User:', query)
    print("Results:", results['answer'])
    
    
    
    
    