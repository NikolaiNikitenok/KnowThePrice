from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import ToDo
from .forms import ToDoCreateForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

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


class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = ToDo
    fields = ['status', 'goal', 'deadline']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)
