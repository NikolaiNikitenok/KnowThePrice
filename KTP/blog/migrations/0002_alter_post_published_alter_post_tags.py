# Generated by Django 4.2.1 on 2023-06-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default='2023-06-22'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.TextField(max_length=400, null=True, verbose_name='Тэги'),
        ),
    ]
