from django.db import models
from users.models import Profile

class ToDo(models.Model):
    profile = models.ForeignKey(Profile, 
                                on_delete=models.PROTECT,
                                verbose_name='Владелец',
                                null=True
                                )
    
    # todo_id = models.IntegerField(primary_key=True,
    #                               default=0)
    
    goal = models.CharField(max_length=200,
                            verbose_name='Цель')
    
    status = models.BooleanField(default=False,
                                 blank =True,
                                 verbose_name='Статус')
    
    deadline = models.DateField(auto_now=False, 
                                auto_now_add=False,
                                verbose_name='Дата окончания')
    
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Время создания')
    
    def __str__(self):
        return f'{self.goal}'
    
    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['-created']
    
