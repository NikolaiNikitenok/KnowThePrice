# Generated by Django 4.2.1 on 2023-06-19 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(default='2023-06-19'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(default='2023-06-19'),
        ),
    ]
