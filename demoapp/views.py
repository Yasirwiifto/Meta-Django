from django.shortcuts import render

# Create your views here.
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 