from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks,
               'form':form}
    return render(request, 'main/index.html', context)


def updateTask(request,pk):
    taski = Task.objects.get(id=pk) 
    form = TaskForm(instance=taski)
    if request.method =="POST":
        form = TaskForm(request.POST,instance=taski)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'main/update_task.html',context)


def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method =="POST":
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'main/delete.html',context)