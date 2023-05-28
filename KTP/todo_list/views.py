from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import ToDo
# from .forms import ToDoCreateForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

def todo(request):
    todos = ToDo.objects.all()
    
    context = {
        'todos': todos,
    }
    return render(request, 'todo_list/todo_home.html', context)

def add_todo(request):
    if request == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        todo = ToDo(title = title, description = description)
        todo.save()
        
        return redirect('todo-home')
    
    else:
        return render(request, 'todo_list/todo_add.html')

# Create your views here.
