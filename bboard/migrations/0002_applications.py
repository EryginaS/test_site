# Generated by Django 3.2 on 2021-04-09 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тема заявки')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Плановая дата решения')),
                ('contract', models.CharField(blank=True, max_length=50, null=True, verbose_name='Договор')),
                ('priority', models.IntegerField(choices=[(0, 'Низкий'), (1, 'Средний'), (2, 'Высокий')], null=True, verbose_name='Приоритет')),
                ('status', models.IntegerField(choices=[(0, 'Непрочитанный'), (1, 'К исполнению'), (2, 'Выполненный')], null=True, verbose_name='Статус заявки')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.clients', verbose_name='Клиент')),
                ('responsible', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Ответсвтенный сотрудник')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
