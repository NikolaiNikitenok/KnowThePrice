from django.db import models
from django.contrib.auth.models import User
from PIL import Image


def crop_center(pil_img, crop_width: int, crop_height: int):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                        (img_height - crop_height) // 2,
                        (img_width + crop_width) // 2,
                        (img_height + crop_height) // 2))


class Profile(models.Model):
    
    class Sex(models.TextChoices):
        FEMALE = 'f', 'Женский'
        MAN = 'm', 'Мужской'
        OTHER = 'o', 'Другой'
        __empty__ = 'Выберите ваш пол'
        
    SEX = (
        ('f', 'Женский'),
        ('m', 'Мужской'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя')
    image = models.ImageField(default='default-profile.jpg', 
                              upload_to='profile_pics', 
                              verbose_name='Фото')
    # nickname = models.CharField(max_length=15, 
    #                             verbose_name='Никнейм',
    #                             unique=True, 
    #                             null=True)
    # tariff_plan = models.ForeignKey('TariffPlan', null=True,
    #                                 on_delete=models.PROTECT, 
    #                                 verbose_name='Тарифный план')
    sex = models.CharField(max_length=50,
                            null=True,
                            blank=True,
                            choices=Sex.choices,
                            verbose_name='Пол')
    # date_of_birthday = models.DateField(auto_now=False, 
    #                                         auto_now_add=False, 
    #                                         verbose_name='Дата рождения')
    # country = models.CharField(null=True, 
    #                            max_length=50,
    #                            verbose_name='Страна')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
                
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            image_size_1, image_size_2 = img.size
            if image_size_1 > image_size_2:
                img = crop_center(img, image_size_2, image_size_2)
                
            else:
                img = crop_center(img, image_size_1, image_size_1)
                
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    
class TariffPlan(models.Model):
    plan = models.CharField(max_length=20, db_index=True, verbose_name='Тарифный план')
    
    def __str__(self):
        return self.plan
    
    class Meta:
        verbose_name_plural = 'Тарифные планы'
        verbose_name = 'Тарифный план'
        ordering = ['plan']
        
        
# class Sex(models.Model):
#     sex = models.CharField(max_length=50, db_index=True, verbose_name='Пол')
    
#     def __str__(self):
#         return self.sex
    
#     class Meta:
#         verbose_name_plural = 'Выбор пола'
#         verbose_name = 'Пол'
#         ordering = ['sex']
    
