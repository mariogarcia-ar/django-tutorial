# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_list_or_404, render

# Create your views here.

def index(request):
    title = "Hola Mundo!"
    return render(request, "index.html", {
        'title': title
    })

def hello(request, username):
    return HttpResponse(f"Hola Mundo! {username}")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html",{
        'projects': projects
    })


def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html",{
        'tasks': tasks
    })

    