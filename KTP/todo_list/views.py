from django.shortcuts import render
from .forms import ToDoCreateForm

def todo(request):
    
    todo_form = ToDoCreateForm(request.POST)
    
    context = {
        'todo_form': todo_form,
    }
    return render(request, 'todo_list/todo_home.html', context)
