# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_list_or_404, render

# Create your views here.

def index(request):
    return render(request, "index.html")

def hello(request, username):
    return HttpResponse(f"Hola Mundo! {username}")

def about(request):
    return render(request, "about.html")

def projects(request):
    # projects = list(Project.objects.values())
    # # return HttpResponse("projectos")
    # return JsonResponse(projects, safe=False)
    return render(request, "projects.html")


def tasks(request, id):
    # return HttpResponse("tareas")
    # task = Task.objects.get(id=id)
    # task = get_list_or_404(Task, id=id)
    # return JsonResponse(task, safe=False)
    return render(request, "tasks.html")

    