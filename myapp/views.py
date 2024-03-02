# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, render, redirect

from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
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
    return render(request, "projects/projects.html",{
        'projects': projects
    })

def create_project(request):
    if request.method == 'POST':
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

    return render(request, "projects/create_project.html",{
        'form': CreateNewProject()
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html",{
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'], 
                            description=request.POST['description'],
                            project_id = 1)
        return redirect('tasks')
        
    return render(request, "tasks/create_task.html",{
        'form': CreateNewTask()
    })
