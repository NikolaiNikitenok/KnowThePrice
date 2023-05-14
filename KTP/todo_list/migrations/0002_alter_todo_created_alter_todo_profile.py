# Generated by Django 4.1.7 on 2023-04-05 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_sex'),
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='profile',
            field=models.ForeignKey(default='Free', null=True, on_delete=django.db.models.deletion.PROTECT, to='users.profile', verbose_name='Владелец'),
        ),
    ]
