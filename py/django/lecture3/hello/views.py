from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

# def greet(request, name=None):
#     if name == None:
#         name = "World"
#     return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name=None):
    if name == None:
        name = "World"
    return render(request, 'hello/greet.html', {
        'name': name.capitalize()
    })