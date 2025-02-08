from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
def todolist(request):
    tasks=Task.objects.all()
    return render(request,'task/task.html',{'tasks':tasks})
def add_task(request):
    if request.method == "POST":
        title=request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('todolist')
    return render(request,'task/add_task.html')

