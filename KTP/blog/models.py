from django.db import models
from users.models import Profile
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name
    
    
class Comments(models.Model):
    author = models.ForeignKey(Profile, 
                               verbose_name=("Автор комментария"), 
                               on_delete=models.PROTECT)


class Post(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Название поста')
    author = models.ForeignKey(Profile, 
                               on_delete=models.PROTECT, 
                               verbose_name='Владелец')
    description = models.TextField(max_length=1000,
                                   verbose_name='Содержание поста')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name='Категория')
    # media = models.FileField()
    tags = models.TextField(max_length=400,
                            verbose_name='Тэги')
    published = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    # comments = 
