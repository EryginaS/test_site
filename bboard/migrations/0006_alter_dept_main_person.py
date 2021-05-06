# Generated by Django 3.2 on 2021-04-13 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bboard', '0005_auto_20210413_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='main_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Начальник'),
        ),
    ]
