import os
import pandas as pd
import re
import numpy as np
import warnings

warnings.filterwarnings("ignore")


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
from util import *
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

'''########################### QUERY ############################

query = "Who won the 2023 Bahrain GP?"
docs = db.similarity_search(query, k=3)
print("Results:", docs)

'''#############################################################

'''# MAIN #
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.1)

pdf_data = preprocess_pdf_files_for_LLM(path = 'data/DataFiltered2022_2023/data filtered')
csv_data = preprocess_csv_files_for_LLM(path = 'data/DataFiltered2022_2023/data filtered')


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
'''

#bot burro
'''#prompt
llm = ChatOpenAI(model_name ="gpt-3.5-turbo")

prompt = f"Which driver id has the most podiums in the file i provided u?"

response = llm(prompt, temperature = 0)

print("----- response -----")
print(response.replace("Langchain", ""))


#read pdf
pdf_data = PdfReader("data/data2223.pdf")

pdf_text = ""

for i, page in enumerate(pdf_data.pages):
    text = page.extract_text()
    if text:
        pdf_text += text

print(len(pdf_text))

#split the pdf text
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 400,
    chunk_overlap = 100
)

final_data = text_splitter.split_text(pdf_text)

print(f"""
    # of Chunks: {len(final_data)}
    Chunk 0: {final_data[0]}
    Chunk 1: {final_data[1]}
""")

from langchain.chains.question_answering import load_qa_chain

#embedding
embeddings = OpenAIEmbeddings()
document_searcher = FAISS.from_texts(final_data, embeddings)
chain = load_qa_chain(ChatOpenAI(), chain_type="stuff")

prompt = 'ze eu acabei de te dar todo um pdf com informacao, diz me so o id do driver com mais wins em 2022'

docs =  document_searcher.similarity_search(prompt)
result = chain.run(input_documents=docs, question=prompt)

print("--- 🤖 RESULT ---")
print(result)'''




model="gpt-3.5-turbo"

print("First LLM API example")
print(f"✅ OpenAI Key loaded (...{local_settings.OPENAI_API_KEY[20:-20]}...)")
print(f"✅ Model: {model}")

client = OpenAI(api_key=local_settings.OPENAI_API_KEY)

def get_completion(prompt, temperature= 0, messages = [], model=model):

    message = {"role": "user", "content": prompt}

    messages.append(message)

    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )

    return completion.choices[0].message.content

messages = [
    {
        "system" : "You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know."
    }
]









