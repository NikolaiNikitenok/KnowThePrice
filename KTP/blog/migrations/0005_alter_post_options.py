# Generated by Django 4.2.1 on 2023-06-23 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published'], 'verbose_name': 'публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
