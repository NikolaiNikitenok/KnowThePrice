from django.db import models
from django.contrib.auth.models import User


# class Category(models.Model):
#     name = models.CharField(max_length=180)
    
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
        
#     def __str__(self):
#         return self.name
    

class ToDo(models.Model):
    # profile = models.ForeignKey(User, 
    #                             on_delete=models.PROTECT,
    #                             verbose_name='Владелец')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        # ordering = ['-created']

# Create your models here.
