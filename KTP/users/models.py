from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя')
    image = models.ImageField(default=default-profile.png, 
                              upload_to='profile_pics', 
                              verbose_name='Фото')
    nickname = models.CharField(max_length=15, 
                                default=Profile.user, 
                                verbose_name='Никнейм')
    tariff_plan = models.ForeignKey('TariffPlan', null=True,
                                    on_delete=models.PROTECT, 
                                    verbose_name='Тарифный план')
    sex = models.ForeignKey('Sex', 
                            on_delete=models.PROTECT, 
                            verbose_name='Пол')
    date_of_birthday = models.DateField(auto_now=False, 
                                            auto_now_add=False, 
                                            verbose_name='Дата рождения')
    country = models.CharField(null=True, 
                               max_length=50,
                               verbose_name='Страна')
    
    
class TariffPlan(models.Model):
    plan = models.CharField(max_length=20, db_index=True, verbose_name='Тарифный план')
    
    def __str__(self):
        return self.plan
    
    class Meta:
        verbose_name_plural = 'Тарифные планы'
        verbose_name = 'Тарифный план'
        ordering = ['plan']
        
        
    class Sex(models.Models):
        sex = models.CharField(db_index=True, verbose_name='Пол')
        
        def __str__(self):
            return self.sex
        
        class Meta:
            verbose_name_plural = 'Выбор пола'
            verbose_name = 'Пол'
            ordering = ['sex']
    
