from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ToDoCreateForm

def todo(request):
    if request.method == 'POST':
        todo_form = ToDoCreateForm(request.POST)
        
        if todo_form.is_valid():
            todo_form.save()
            
            messages.success(request, f'Твоя задача была создана!')
            return redirect('profile')
        
        
    else:
        todo_form = ToDoCreateForm()
        
    context = {
        'todo_form': todo_form,
    }
    return render(request, 'todo_list/todo_home.html', context)
