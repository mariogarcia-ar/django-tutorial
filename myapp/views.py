# from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    return HttpResponse(f"Home Page")

def hello(request, username):
    return HttpResponse(f"Hola Mundo! {username}")

def about(request):
    return HttpResponse("Somos programadores!!!")