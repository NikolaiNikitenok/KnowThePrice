from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=180)
    author = models.ForeignKey(User, 
                                on_delete=models.PROTECT,
                                verbose_name='Владелец')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name
    

class ToDo(models.Model):
    author = models.ForeignKey(User, 
                                on_delete=models.PROTECT,
                                verbose_name='Владелец')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    deadline = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default="general", on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['deadline']

# Create your models here.
