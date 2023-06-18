from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import ToDo, Category
# from .forms import ToDoCreateForm
from django.contrib.auth.models import User
# from django.views.generic import (
#     ListView, 
#     DetailView, 
#     CreateView,
#     UpdateView,
#     DeleteView
# )


def todo(request):
    todos = ToDo.objects.filter(author = request.user, completed=False)
    categories = Category.objects.all()
    check = []
    
    if request.method == 'POST':
        if "Edit" in request.POST:
            return redirect('category')
        elif "Delete" in request.POST:
            check = request.POST.getlist('check')
            for i in range(len(check)):
                    todo_del = ToDo.objects.filter(id=int(check[i]))
                    todo_del.delete()  # удаление категории
        elif "Complete" in request.POST:
            check = request.POST.getlist('check')
            for i in range(len(check)):
                ToDo.objects.filter(id=int(check[i])).update(completed=True)
        # elif "Delete_id" in request.POST:
        #         todo = ToDo.objects.filter('value')
        #         todo.delete()
    
    context = {
        'todos': todos,
        'categories': categories,
        'check': len(check), # Проблема, показывается кол-во только после отправления запроса
    }
    return render(request, 'todo_list/todo_home.html', context)


def completed_todo(request):
    completed_todos = ToDo.objects.filter(author = request.user, completed=True)
    
    if request.method == 'POST':
        if "Uncomplete" in request.POST:
            check = request.POST.getlist('check')
            for i in range(len(check)):
                ToDo.objects.filter(id=int(check[i])).update(completed=False)

    
    context = {
        'completed_todos': completed_todos,
    }
    return render(request, 'todo_list/completed_todo.html', context)


def add_todo(request):
    categories = Category.objects.filter(author=request.user)
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        deadline = request.POST['deadline']
        description = request.POST['description']
        category = request.POST['category_select']
        todo = ToDo(title=title,
                    description=description,
                    deadline=deadline,
                    category=Category.objects.get(name=category),
                    author=author)
        todo.save()
        
        context = {
            'categories': categories,
        }
        
        return redirect('todo-home')
    
    else:
        context = {
            'categories': categories,
        }
        
        return render(request, 'todo_list/todo_add.html', context)


def add_category(request):
    categories = Category.objects.filter(author = request.user)
    
    if request.method == "POST":  # проверяем что это метод POST
        author = request.user
        if "Add" in request.POST:  # если собираемся добавить
            name = request.POST["name"]  # имя нашей категории
            category = Category(name=name, author = author)  # у нашей категории есть только имя
            category.save()  # сохранение нашей категории
            return redirect("/category")
        elif "Delete" in request.POST:  # проверяем есть ли удаление
            # немного изменил название массива в отличии от todo, что бы было меньше путаницы в коде
            check = request.POST.getlist('check')
            for i in range(len(check)):
                try:
                    сateg = Category.objects.filter(id=int(check[i]))
                    сateg.delete()  # удаление категории
                except BaseException:  # вне сомнения тут нужно нормально переписать обработку ошибок,
                    # но на первое время хватит и этого
                    return HttpResponse('<h1>Сначала удалите карточки с этими категориями)</h1>')
    return render(request, "todo_list/category.html", {"categories": categories})
# Create your views here.
