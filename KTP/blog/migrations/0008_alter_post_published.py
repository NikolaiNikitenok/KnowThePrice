# Generated by Django 4.2.1 on 2023-06-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default='2023-06-23-18-06'),
        ),
    ]
