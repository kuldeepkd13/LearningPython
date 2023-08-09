from django.shortcuts import render ,redirect
mydictionary={}
mydictionary['Name']="Kuldeep"
mydictionary['Age']=23
mydictionary['City']="Haldwani"
def create(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        mydictionary[key] = value
        return redirect('read')
    return render(request, 'create.html')

def read(request):
    # Get the data from your Python dictionary
    dictionary_data = mydictionary  # Replace with your dictionary name
    return render(request, 'read.html', {'dictionary_data': dictionary_data})

def update(request):
    if request.method == 'POST':
        key =request.POST['key']
        value = request.POST['value']

        if key in mydictionary:
            mydictionary[key]=value
            return redirect('read')
        
    return render(request, 'update.html')
        
def delete(request):
    if request.method =='POST':
        key = request.POST['key']

        if key in mydictionary:
            del mydictionary[key]
            return redirect('read')
    return render(request , 'delete.html')