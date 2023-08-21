from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def view(request,id):
    user_data = {
        '1':{'username':"rahul", 'caption':"create"},
        '2':{'username':"roma", 'caption':"create"}
    }

    data = user_data.get(id)
    if data is None:
        return JsonResponse({'error':"No data"}, status= 404)
    return JsonResponse(data)

