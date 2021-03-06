from typing import ContextManager
from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.
def index(request):
    # tasks = Task.objects.all()
    count = Task.objects.filter(complete=False).count()
    # if 'search' in request.GET:
    #     search = request.GET['search']
    #     tasks = Task.objects.filter(title__icontains=search)
    # else:
    #     tasks = Task.objects.all()
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    # context = {'tasks':tasks,'count':count, 'search':search}
    context = {'tasks':tasks,'count':count, 'form': form}
    return render(request, 'index.html', context)

# def create(request):
#     form = TaskForm()
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#     context = {'form':form}
#     return render(request, 'create.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'update.html', context)

def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'delete.html', context)