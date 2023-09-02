from django.shortcuts import render
from django.http import JsonResponse
import os
from dotenv import load_dotenv  # Add this import
from .forms import PdfUploadForm
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import pickle

# Load environment variables from .env file
load_dotenv()

def process_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text=text)
    return chunks

def pdf_upload_view(request):
    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            chunks = process_pdf(pdf_file)
            return render(request, 'upload_template.html', {'chunks': chunks, 'form': form})
    else:
        form = PdfUploadForm()
    return render(request, 'upload_template.html', {'form': form})

def question_view(request):
    if request.method == 'POST':
        user_question = request.POST.get('user_question', '')
        pdf_file = request.FILES.get('pdf_file')
        chunks = process_pdf(pdf_file)

        if user_question and chunks:
            embeddings = OpenAIEmbeddings()
            knowledge_base = FAISS.from_texts(chunks, embeddings)

            docs = knowledge_base.similarity_search(user_question)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
            
            return render(request, 'upload_template.html', {'chunks': chunks, 'user_question': user_question, 'response': response})

    return render(request, 'upload_template.html', {'chunks': chunks})
