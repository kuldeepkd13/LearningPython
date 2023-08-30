from django.shortcuts import render
from django.http import JsonResponse
import os
from dotenv import load_dotenv  # Add this import
from .forms import PdfUploadForm
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import pickle

# Load environment variables from .env file
load_dotenv()

# PDF Processing and Text Splitting
def process_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Placeholder for getting embeddings and vector store
def get_embeddings_and_vectorstore(text):
    openai_api_key = os.environ.get('OPENAI_API_KEY')  # Get the API key from environment
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    
    # Replace this with your actual text splitting logic
    chunks = [...]  
    
    chunks_list = [chunk for chunk in chunks if chunk is not Ellipsis]  # Remove ellipsis from chunks
    text = " ".join(chunks_list)  # Join the chunks into a single string
    
    if text:  # Make sure that text is not empty
        VectorStore = FAISS.from_texts(text, embedding=embeddings)
        return embeddings, VectorStore
    else:
        return None, None



# Langchain and OpenAI Integration
def process_text_with_langchain(text, query):
    embeddings, VectorStore = get_embeddings_and_vectorstore(text)
    docs = VectorStore.similarity_search(query=query, k=3)
    llm = OpenAI()
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=query)
    return response

def pdf_upload_view(request):
    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            text = process_pdf(pdf_file)
            return render(request, 'question_template.html', {'text': text})
    else:
        form = PdfUploadForm()
    return render(request, 'upload_template.html', {'form': form})

def question_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        query = request.POST.get('query', '')
        response = process_text_with_langchain(text, query)
        return JsonResponse({'response': response})
