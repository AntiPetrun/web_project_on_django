from django.shortcuts import render, HttpResponse

# Create your views here.

def hello_world_view(request):
    return HttpResponse('<h1>Hello World</h1>')
