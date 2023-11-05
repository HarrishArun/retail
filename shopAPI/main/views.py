from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    request_URL='http://localhost:8000/api/products/all'
    response=requests.get(request_URL)
    data=response.json()
    return render(request, 'index.html', {'data': data})
