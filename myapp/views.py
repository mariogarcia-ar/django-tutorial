# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_list_or_404

# Create your views here.

def index(request):
    return HttpResponse(f"Home Page")

def hello(request, username):
    return HttpResponse(f"Hola Mundo! {username}")

def about(request):
    return HttpResponse("Somos programadores!!!")

def projects(request):
    projects = list(Project.objects.values())
    # return HttpResponse("projectos")
    return JsonResponse(projects, safe=False)


def tasks(request, id):
    # return HttpResponse("tareas")
    # task = Task.objects.get(id=id)
    task = get_list_or_404(Task, id=id)
    return JsonResponse(task, safe=False)

    