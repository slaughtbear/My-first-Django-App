from django.http import HttpResponse
from .models import Project, Tasks
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject


def index(request):
    title = 'Django curse!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'Slaughtbear'
    return render(request, 'about.html', {
        'username': username
    })

# VISTAS CON PARÁMETROS
def hello(request, id): # Parámetro de tipo entero que espera un "id"
    # Operando con el valor del argumento
    result = id + 100 * 2 # Se le asigna el valor a una nueva variable
    return HttpResponse("<h1>Hola %s<h1/>" % result) # Se concatena en la respuesta http

# VISTAS CON MODELOS
def projects(request):
    # Realizando consultas al modelo Project
    #projects = list(Project.objects.values()) # Se guarda la consulta en una lista para que pueda ser leido por el formato JSON
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    #task = get_object_or_404(Tasks, id=id)
    tasks = Tasks.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()
    })
    else:
        Tasks.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('/tasks/')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
        'form': CreateNewProject()
    }) 
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Tasks.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })
    

