# Generated by Django 3.2 on 2021-04-13 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]