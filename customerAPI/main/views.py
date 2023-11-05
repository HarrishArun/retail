from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    api_url = 'http://localhost:5000/api/users'  # Replace with your DRF API URL
    data = requests.get(api_url)
    data=data.json()
    return render(request, 'index.html', {'data': data})
