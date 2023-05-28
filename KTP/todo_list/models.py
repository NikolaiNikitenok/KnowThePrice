from django.db import models
from users.models import Profile
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=180)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name
    


class ToDo(models.Model):
    # profile = models.ForeignKey(Profile, 
    #                             on_delete=models.PROTECT,
    #                             verbose_name='Владелец',
    #                             null=True
    #                             )
    
    # todo_id = models.IntegerField(primary_key=True,
    #                               default=0)
    
    # title = models.CharField(max_length=100, 
    #                          verbose_name='Название')
    
    category = models.ForeignKey(Category, 
                                 verbose_name=("Выбор категории"), 
                                 on_delete=models.PROTECT,
                                 blank=True)
    
    goal = models.CharField(max_length=400,
                            verbose_name='Цель')
    
    deadline = models.DateField(blank=True,
                                verbose_name='Дата окончания')
    
    created = models.DateField(auto_now_add=True, 
                               verbose_name='Время создания')
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['-created']
    
