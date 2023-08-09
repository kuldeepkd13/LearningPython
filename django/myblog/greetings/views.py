from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome To Home Page")

def greet(request,username):
    return HttpResponse(f"Hello {[username]}")

def farewell(request,username):
    return HttpResponse(f"Goodbye, {[username]}")