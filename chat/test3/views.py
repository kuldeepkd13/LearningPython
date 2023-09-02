from django.shortcuts import render
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from .forms import PdfUploadForm
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
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
    pdf_name = None
    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            chunks, pdf_name = process_pdf(pdf_file)
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{pdf_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)
            return render(request, 'success_template.html', {'pdf_name': pdf_name})
    else:
        form = PdfUploadForm()

    context = {'form': form}
    return render(request, 'upload_template.html', context)

def chat_view(request):
    pdf_name = request.GET.get('pdf_name')
    if pdf_name:
        with open(f"{pdf_name}.pkl", "rb") as f:
            VectorStore = pickle.load(f)
        query = request.GET.get('query', '')

        if query:
            docs = VectorStore.similarity_search(query=query, k=3)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
            response_text = response.get('output_text', "No answer found.")
        else:
            response_text = ""

        context = {'pdf_name': pdf_name, 'query': query, 'response_text': response_text}
        return render(request, 'chat_template.html', context)
    else:
        return render(request, 'error_template.html', {'error_message': 'PDF name not provided.'})
