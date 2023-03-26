# Generated by Django 4.1.7 on 2023-03-25 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(db_index=True, max_length=50, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Пол',
                'verbose_name_plural': 'Выбор пола',
                'ordering': ['sex'],
            },
        ),
        migrations.CreateModel(
            name='TariffPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(db_index=True, max_length=20, verbose_name='Тарифный план')),
            ],
            options={
                'verbose_name': 'Тарифный план',
                'verbose_name_plural': 'Тарифные планы',
                'ordering': ['plan'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default-profile.png', upload_to='profile_pics', verbose_name='Фото')),
                ('nickname', models.CharField(max_length=15, verbose_name='Никнейм')),
                ('date_of_birthday', models.DateField(verbose_name='Дата рождения')),
                ('country', models.CharField(max_length=50, null=True, verbose_name='Страна')),
                ('sex', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.sex', verbose_name='Пол')),
                ('tariff_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.tariffplan', verbose_name='Тарифный план')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя')),
            ],
        ),
    ]
