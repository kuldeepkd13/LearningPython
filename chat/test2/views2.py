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
    store_name = pdf_file.name[:-4]  # Extract the name without the '.pdf' extension
    return chunks, store_name

def pdf_upload_view(request):
    pdf_name = None  # Initialize pdf_name
    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            chunks, pdf_name = process_pdf(pdf_file)  # Extract the PDF name
            if os.path.exists(f"{pdf_name}.pkl"):
             with open(f"{pdf_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
            # st.write('Embeddings Loaded from the Disk')s
            else:
              embeddings = OpenAIEmbeddings()
              VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
              with open(f"{pdf_name}.pkl", "wb") as f:
               pickle.dump(VectorStore, f)
    else:
        form = PdfUploadForm()
    
    context = {'form': form, 'pdf_name': pdf_name}  # Include pdf_name in the context
    return render(request, 'upload_template.html', context)