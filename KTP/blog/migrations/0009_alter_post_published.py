# Generated by Django 4.2.1 on 2023-06-23 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default='2023-06-23-18-06'),
        ),
    ]
